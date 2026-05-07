#!/usr/bin/env python3
"""
AI Power Atlas — Stage 1.5: KB Feedback Context Generator
KB 누적 데이터에서 패턴을 추출해 리포트 생성용 컨텍스트 파일을 자동 생성.
산출물: references/knowledge-base/feedback_context.md
실행: python3 scripts/kb_feedback_context.py [--days 14]
"""

import os, re, json, glob, argparse
from datetime import datetime, timedelta
from collections import defaultdict, Counter

APA_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KB_DIR   = os.path.join(APA_ROOT, 'references', 'knowledge-base')
OUTPUT   = os.path.join(KB_DIR, 'feedback_context.md')

# ── 유틸 ──────────────────────────────────────────────────────────────
def load_jsonl(path):
    records = []
    if not os.path.exists(path): return records
    with open(path) as f:
        for line in f:
            try: records.append(json.loads(line))
            except: pass
    return records

def date_within(date_str, days):
    """date_str이 오늘 기준 days일 이내인지"""
    try:
        d = datetime.strptime(date_str[:10], '%Y-%m-%d')
        return d >= datetime.now() - timedelta(days=days)
    except:
        return False

def extract_entities_from_text(text):
    """대문자 약어·고유명사 구문 추출"""
    abbrevs = set(re.findall(r'\b[A-Z]{2,6}\b', text))
    phrases = set(re.findall(r'\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)+\b', text))
    stop = {'The','This','These','That','With','From','When','They','Their',
            'After','Also','Such','Some','Into','Section','Event','Layer',
            'Score','Report','Source','Power','Flow','Signal','Impact'}
    singles = set(w for w in re.findall(r'\b[A-Z][a-zA-Z]{3,}\b', text) if w not in stop)
    return abbrevs | phrases | singles

# ── 섹션 1: Hot Layers ─────────────────────────────────────────────────
def build_hot_layers(daily_records, days=14):
    layer_counts  = Counter()
    layer_impact  = defaultdict(list)

    for rec in daily_records:
        if not date_within(rec.get('date',''), days): continue
        for ev in rec.get('s01_events', []):
            layer = ev.get('layer','').strip().upper()
            if not layer: continue
            layer_counts[layer] += 1
            try:
                layer_impact[layer].append(float(ev.get('impact_score', 0)))
            except: pass

    rows = []
    for layer, cnt in layer_counts.most_common(10):
        impacts = layer_impact[layer]
        avg_imp = round(sum(impacts)/len(impacts), 2) if impacts else 0.0
        rows.append(f"| {layer} | {cnt} | {avg_imp} |")

    header = (
        f"## Section 1 — Hot Layers (최근 {days}일)\n\n"
        "| Layer | 등장 횟수 | 평균 Impact Score |\n"
        "|-------|-----------|-------------------|\n"
    )
    return header + ('\n'.join(rows) if rows else '| (데이터 없음) | — | — |') + '\n'

# ── 섹션 2: Recurring Entities ────────────────────────────────────────
def build_recurring_entities(daily_records, days=14):
    # date → entity set
    date_entities = defaultdict(set)
    for rec in daily_records:
        d = rec.get('date','')
        if not date_within(d, days): continue
        # S01 이벤트 텍스트 수집
        for ev in rec.get('s01_events', []):
            text = ev.get('title','') + ' ' + ev.get('summary','')
            date_entities[d] |= extract_entities_from_text(text)
        # S02 power shift
        s02 = rec.get('s02_power_shift', {})
        date_entities[d] |= extract_entities_from_text(
            s02.get('from','') + ' ' + s02.get('to','')
        )

    # 2일 이상 등장한 엔티티
    entity_dates = defaultdict(set)
    for d, ents in date_entities.items():
        for e in ents:
            entity_dates[e].add(d)

    recurring = [(e, sorted(ds)) for e, ds in entity_dates.items() if len(ds) >= 2]
    recurring.sort(key=lambda x: (-len(x[1]), x[0]))

    rows = []
    for entity, dates in recurring[:20]:
        last = dates[-1]
        rows.append(f"| {entity} | {len(dates)} | {last} |")

    header = (
        f"## Section 2 — Recurring Entities (최근 {days}일, 2일+ 등장)\n\n"
        "| Entity | 등장 일수 | 최근 날짜 |\n"
        "|--------|-----------|----------|\n"
    )
    return header + ('\n'.join(rows) if rows else '| (데이터 없음) | — | — |') + '\n'

# ── 섹션 3: Prediction Accuracy Trend ────────────────────────────────
def build_accuracy_trend(score_log_path, days=14):
    records = load_jsonl(score_log_path)
    recent  = [r for r in records if date_within(r.get('date',''), days)]
    recent.sort(key=lambda x: x.get('date',''))

    rows = []
    totals, realizeds = [], []
    for r in recent:
        d     = r.get('date','?')
        acc   = r.get('accuracy_pct', 0)
        real  = r.get('realized', 0)
        total = r.get('total_signals', 0)
        ver   = r.get('scorer_version', 'v1')
        bar   = '█' * (acc // 10) + '░' * (10 - acc // 10)
        rows.append(f"| {d} | {bar} {acc}% | {real}/{total} | {ver} |")
        totals.append(total)
        realizeds.append(real)

    overall_acc = (
        round(sum(realizeds)/sum(totals)*100)
        if sum(totals) > 0 else 0
    )

    header = (
        f"## Section 3 — Prediction Accuracy Trend (최근 {days}일)\n\n"
        "| 날짜 | 정확도 | 실현/전체 | Scorer |\n"
        "|------|--------|-----------|--------|\n"
    )
    footer = f"\n**전체 평균: {overall_acc}%** ({sum(realizeds)}/{sum(totals)} 실현)\n"
    return header + ('\n'.join(rows) if rows else '| (채점 기록 없음) | — | — | — |') + '\n' + footer + '\n'

# ── 섹션 4: Open S08 Signals ─────────────────────────────────────────
def build_open_s08(daily_records, score_records, days=5):
    """최근 days일 S08 예측 중 미결(score 0~1) 신호 목록"""
    # 채점 결과 인덱스: date → {signal: score}
    score_index = {}
    for r in score_records:
        d = r.get('date','')
        score_index[d] = {s['signal']: s['score'] for s in r.get('scores', [])}

    rows = []
    for rec in sorted(daily_records, key=lambda x: x.get('date',''), reverse=True):
        pred_date = rec.get('date','')
        if not date_within(pred_date, days): continue
        # 다음날 채점 날짜 계산
        try:
            next_day = (datetime.strptime(pred_date, '%Y-%m-%d') + timedelta(days=1)).strftime('%Y-%m-%d')
        except:
            next_day = None

        scored = score_index.get(next_day, {})
        for sig in rec.get('s08_watchlist', []):
            s = sig.get('signal','')
            score = scored.get(s, None)
            if score is None:
                status = '⬜ 미채점'
            elif score <= 1:
                status = f"{'🔶' if score==1 else '❌'} {['미실현','연관'][score]}"
            else:
                continue  # 실현된 건 제외
            rows.append(f"| {pred_date} | {s[:60]} | {status} |")

    header = (
        f"## Section 4 — Open S08 Signals (최근 {days}일, 미결 신호)\n\n"
        "| 예측일 | Signal | 상태 |\n"
        "|--------|--------|------|\n"
    )
    return header + ('\n'.join(rows[:15]) if rows else '| (미결 신호 없음) | — | — |') + '\n'

# ── 섹션 5: Power Shift Direction ────────────────────────────────────
def build_power_shift(daily_records, days=7):
    """최근 days일 S02 From→To 방향 추적"""
    rows = []
    for rec in sorted(daily_records, key=lambda x: x.get('date',''), reverse=True):
        d = rec.get('date','')
        if not date_within(d, days): continue
        s02 = rec.get('s02_power_shift', {})
        frm  = s02.get('from','').strip()[:40] or '—'
        to   = s02.get('to','').strip()[:40]   or '—'
        conf = s02.get('confidence','').strip() or '—'
        rows.append(f"| {d} | {frm} | {to} | {conf} |")

    rows.reverse()  # 날짜 오름차순
    header = (
        f"## Section 5 — Power Shift Direction (최근 {days}일)\n\n"
        "| 날짜 | From | To | Confidence |\n"
        "|------|------|----|------------|\n"
    )
    return header + ('\n'.join(rows) if rows else '| (S02 데이터 없음) | — | — | — |') + '\n'

# ── 메인 ──────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--days', type=int, default=14, help='분석 기간 (일)')
    args = parser.parse_args()

    days = args.days

    kb_daily  = os.path.join(KB_DIR, 'daily_records.jsonl')
    score_log = os.path.join(KB_DIR, 'prediction_scores.jsonl')

    daily_records  = load_jsonl(kb_daily)
    score_records  = load_jsonl(score_log)

    if not daily_records:
        print(f"⚠️  {kb_daily} 없음 — Stage 1 먼저 실행 필요")
        return

    now = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
    header = (
        f"# APA KB Feedback Context\n"
        f"Generated: {now} | Window: {days} days\n\n"
        f"> 이 파일은 `kb_feedback_context.py`가 자동 생성합니다. 직접 편집 금지.\n"
        f"> Step 2(report-writer) 실행 전 반드시 로드해 아래 5개 섹션을 리포트 작성에 반영.\n\n"
        f"---\n\n"
    )

    sections = [
        build_hot_layers(daily_records, days),
        build_recurring_entities(daily_records, days),
        build_accuracy_trend(score_log, days),
        build_open_s08(daily_records, score_records, days=5),
        build_power_shift(daily_records, days=7),
    ]

    os.makedirs(KB_DIR, exist_ok=True)
    with open(OUTPUT, 'w', encoding='utf-8') as f:
        f.write(header)
        for sec in sections:
            f.write(sec + '\n---\n\n')

    print(f"Stage 1.5 완료 — {OUTPUT}")
    print(f"  일간 레코드 {len(daily_records)}개 / 채점 레코드 {len(score_records)}개 처리")

if __name__ == '__main__':
    main()
