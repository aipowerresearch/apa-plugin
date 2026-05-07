#!/usr/bin/env python3
"""
AI Power Atlas — Stage 1: Knowledge Base Builder
실행: python3 scripts/build_knowledge_base.py [--date YYYY-MM-DD]
옵션 없이 실행 시 전체 기존 리포트 일괄 처리 (최초 1회)
--date 지정 시 해당 날짜만 추출 (매일 파이프라인 후 자동 실행)
"""

import os, re, json, glob, argparse
from datetime import datetime

APA_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KB_DIR   = os.path.join(APA_ROOT, 'references', 'knowledge-base')
REPORTS  = os.path.join(APA_ROOT, 'outputs', 'reports')
WEEKLY   = os.path.join(REPORTS, 'weekly')
LEGACY   = os.path.join(REPORTS, '_legacy_v1')

# ── 파서 ──────────────────────────────────────────────
def extract_events(text):
    """S01 이벤트 추출: 제목, 레이어, 임팩트 스코어, 요약(EN), 소스"""
    events = []
    for m in re.finditer(
        r'###\s+Event\s+\d+[:\s]+(.*?)\n'
        r'.*?(?:\*\*Layer\*\*|Layer)[:\s]+(.*?)\n'
        r'.*?(?:\*\*Impact Score\*\*|Impact Score)[:\s]+([\d.]+)',
        text, re.DOTALL
    ):
        title = m.group(1).strip().split('/')[0].strip()
        layer = m.group(2).strip()
        score = float(m.group(3).strip())
        # Summary EN 추출
        summary_m = re.search(r'\*\*Summary \(EN\)\*\*[:\s]+(.*?)(?=\n-|\n#|\Z)',
                               text[m.start():m.start()+2000], re.DOTALL)
        summary = summary_m.group(1).strip()[:300] if summary_m else ''
        # 소스 추출
        src_m = re.search(r'\*\*Source\*\*[:\s]+(https?://\S+)', text[m.start():m.start()+2000])
        source = src_m.group(1) if src_m else ''
        events.append({'title': title, 'layer': layer,
                       'impact_score': score, 'summary': summary, 'source': source})
    return events

def extract_section(text, section_code):
    """S02~S08 섹션 텍스트 추출 (첫 500자)"""
    m = re.search(rf'## {section_code}\s*\|.*?\n(.*?)(?=\n## |\Z)', text, re.DOTALL)
    return m.group(1).strip()[:500] if m else ''

def extract_s02_power_shift(text):
    """S02 권력 이동 신호"""
    m = re.search(r'## S02.*?\n(.*?)(?=\n## |\Z)', text, re.DOTALL)
    if not m: return {}
    s02 = m.group(1)
    from_m = re.search(r'\|\s*From\s*\|.*?\|(.*?)\|', s02)
    to_m   = re.search(r'\|\s*To\s*\|.*?\|(.*?)\|', s02)
    conf_m = re.search(r'(?:Confidence|확신도)[:\s|]+(\w+)', s02)
    return {
        'from': from_m.group(1).strip() if from_m else '',
        'to':   to_m.group(1).strip()   if to_m   else '',
        'confidence': conf_m.group(1) if conf_m else '',
        'raw': s02.strip()[:400]
    }

def extract_s03_lockin(text):
    """S03 락인 변화"""
    raw = extract_section(text, 'S03')
    direction_m = re.search(r'[↑↓→]\s*\((.+?)\)', raw)
    return {'direction': direction_m.group(1)[:100] if direction_m else '', 'raw': raw}

def extract_s04_implications(text):
    """S04 6개월 시사점"""
    raw = extract_section(text, 'S04')
    en_m = re.search(r'\*\*English\*\*[:\s]*(.*?)(?=\*\*한국어\*\*|\Z)', raw, re.DOTALL)
    return {'english': en_m.group(1).strip()[:300] if en_m else raw[:300]}

def extract_s05_strategy(text):
    """S05 전략 조정"""
    raw = extract_section(text, 'S05')
    verdict_m  = re.search(r'(?:Verdict|판정)[:\s|]+(Yes|No)', raw, re.IGNORECASE)
    direction_m = re.search(r'(?:Direction|방향)[:\s|]+(Build|Buy|Wait|Exit)', raw, re.IGNORECASE)
    return {
        'verdict':   verdict_m.group(1)   if verdict_m   else '',
        'direction': direction_m.group(1) if direction_m else '',
        'raw': raw[:200]
    }

def extract_s06_layer_map(text):
    """S06 레이어 맵 지표"""
    raw = extract_section(text, 'S06')
    hot_m  = re.search(r'🔥.*?Hot Layer.*?\|(.*?)\|', raw)
    warn_m = re.search(r'⚠️.*?Warning.*?\|(.*?)\|', raw)
    return {
        'hot_layer':     hot_m.group(1).strip()  if hot_m  else '',
        'warning_layer': warn_m.group(1).strip() if warn_m else '',
        'raw': raw[:300]
    }

def extract_s07_feedback_loops(text):
    """S07 피드백 루프"""
    raw = extract_section(text, 'S07')
    active = re.findall(r'\|\s*(L\d+→L\d+)\s*\|\s*Active', raw)
    return {'active_loops': active, 'raw': raw[:300]}

def extract_s08_watchlist(text):
    """S08 내일 주목 신호"""
    items = []
    s08_m = re.search(r'## S08.*?\n(.*?)(?=\n## |\Z)', text, re.DOTALL)
    if not s08_m: return items
    s08 = s08_m.group(1)
    for m in re.finditer(r'\d+\.\s+\*\*(.+?)\*\*\s*[—-]\s*(.+?)(?=\n\d+\.|\Z)', s08, re.DOTALL):
        items.append({'signal': m.group(1).strip(), 'detail': m.group(2).strip()[:200]})
    return items

def extract_layers_focus(filename):
    """파일명에서 집중 레이어 추출"""
    m = re.search(r'_(L[\w+]+|full|all|weekly)_', filename, re.IGNORECASE)
    return m.group(1).upper() if m else 'UNKNOWN'

def process_report(filepath):
    """단일 리포트 파일 → dict"""
    with open(filepath) as f:
        text = f.read()

    fname = os.path.basename(filepath)
    date_m = re.match(r'(\d{4}-\d{2}-\d{2})', fname)
    date_str = date_m.group(1) if date_m else 'unknown'

    # frontmatter에서 메타 추출
    fm_date = re.search(r'^date:\s*(\S+)', text, re.MULTILINE)
    fm_layer = re.search(r'^focus_layer:\s*(\S+)', text, re.MULTILINE)

    record = {
        'date':          fm_date.group(1)  if fm_date  else date_str,
        'focus_layer':   fm_layer.group(1) if fm_layer else extract_layers_focus(fname),
        'filename':      fname,
        'type':          'weekly' if 'weekly' in fname else 'daily',
        # ── 8개 섹션 전체 ──
        's01_events':    extract_events(text),
        's02_power_shift': extract_s02_power_shift(text),
        's03_lockin':    extract_s03_lockin(text),
        's04_implications': extract_s04_implications(text),
        's05_strategy':  extract_s05_strategy(text),
        's06_layer_map': extract_s06_layer_map(text),
        's07_feedback':  extract_s07_feedback_loops(text),
        's08_watchlist': extract_s08_watchlist(text),
        'extracted_at':  datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
    }
    return record

def get_existing_dates(kb_file):
    """이미 처리된 날짜 목록"""
    if not os.path.exists(kb_file): return set()
    dates = set()
    with open(kb_file) as f:
        for line in f:
            try: dates.add(json.loads(line)['date'])
            except: pass
    return dates

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--date', help='특정 날짜만 처리 (YYYY-MM-DD)')
    args = parser.parse_args()

    kb_daily   = os.path.join(KB_DIR, 'daily_records.jsonl')
    kb_weekly  = os.path.join(KB_DIR, 'weekly_records.jsonl')
    kb_summary = os.path.join(KB_DIR, 'kb_summary.json')

    # 처리할 파일 수집
    if args.date:
        # 특정 날짜만
        pattern_en = os.path.join(REPORTS, f'{args.date}_*_daily-report_en.md')
        pattern_v1 = os.path.join(LEGACY,  f'{args.date}_*_daily-report_v1.md')
        daily_files = glob.glob(pattern_en) or glob.glob(pattern_v1)
        weekly_files = []
    else:
        # 전체 배치
        daily_files  = sorted(glob.glob(os.path.join(REPORTS, '*_daily-report_en.md')) +
                               glob.glob(os.path.join(LEGACY,  '*_daily-report_v1.md')))
        weekly_files = sorted(glob.glob(os.path.join(WEEKLY, '*_weekly-synthesis_en.md')) +
                               glob.glob(os.path.join(WEEKLY, '*_weekly-synthesis.md')))

    existing_d = get_existing_dates(kb_daily)
    existing_w = get_existing_dates(kb_weekly)

    added_d, added_w, skipped = 0, 0, 0

    # 일간 리포트 처리
    for fp in daily_files:
        rec = process_report(fp)
        if rec['date'] in existing_d and args.date is None:
            skipped += 1; continue
        with open(kb_daily, 'a') as f:
            f.write(json.dumps(rec, ensure_ascii=False) + '\n')
        added_d += 1

    # 주간 리포트 처리
    for fp in weekly_files:
        rec = process_report(fp)
        if rec['date'] in existing_w and args.date is None:
            skipped += 1; continue
        with open(kb_weekly, 'a') as f:
            f.write(json.dumps(rec, ensure_ascii=False) + '\n')
        added_w += 1

    # 요약 업데이트
    summary = {
        'last_updated': datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
        'total_daily':  sum(1 for _ in open(kb_daily))  if os.path.exists(kb_daily)  else 0,
        'total_weekly': sum(1 for _ in open(kb_weekly)) if os.path.exists(kb_weekly) else 0,
    }
    with open(kb_summary, 'w') as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    print(f"KB Stage 1 완료 — 일간 +{added_d} / 주간 +{added_w} / 스킵 {skipped}")
    print(f"누적: 일간 {summary['total_daily']}개 / 주간 {summary['total_weekly']}개")

if __name__ == '__main__':
    main()
