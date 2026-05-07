#!/usr/bin/env python3
"""
AI Power Atlas — Stage 2: Prediction Scorer (Daily)
어제 S08 예측이 오늘 S01에서 몇 개나 실현됐는지 자동 채점.
실행: python3 scripts/score_predictions.py --today YYYY-MM-DD
"""

import os, re, json, glob, argparse
from datetime import datetime, timedelta

APA_ROOT  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KB_DIR    = os.path.join(APA_ROOT, 'references', 'knowledge-base')
REPORTS   = os.path.join(APA_ROOT, 'outputs', 'reports')
LEGACY    = os.path.join(REPORTS, '_legacy_v1')
SCORE_LOG = os.path.join(KB_DIR, 'prediction_scores.jsonl')

LAYER_KEYWORDS = {
    'L1': ['compute','nvidia','amd','gpu','chip','h100','b200','hardware','tpu','infra'],
    'L2': ['model','llm','gpt','gemini','claude','qwen','mistral','frontier','benchmark'],
    'L3': ['middleware','api','framework','langchain','inference','deployment'],
    'L4': ['data','dataset','training','synthetic','licensing','crawl'],
    'L5': ['platform','azure','aws','gcp','cloud','enterprise','saas'],
    'L6': ['capital','investment','funding','vc','valuation','ipo','acquisition'],
    'L7': ['geopolit','sovereign','government','export','tariff','sanction','regulation policy'],
    'L8': ['regulation','law','policy','compliance','eu ai act','executive order'],
    'L9': ['labor','talent','layoff','hiring','workforce','job','union'],
    'L10':['perception','media','public','narrative','trust','safety','alignment'],
}

def load_report_text(date_str):
    """날짜 기준으로 리포트 텍스트 로드 (en 우선, v1 폴백)"""
    patterns = [
        os.path.join(REPORTS, f'{date_str}_*_daily-report_en.md'),
        os.path.join(LEGACY,  f'{date_str}_*_daily-report_v1.md'),
    ]
    for p in patterns:
        files = glob.glob(p)
        if files:
            with open(files[0]) as f:
                return f.read()
    return None

def score_signal(signal_text, today_text):
    """예측 신호 1개가 오늘 리포트에 실현됐는지 점수화 (0~3)"""
    signal_lower = signal_text.lower()
    today_lower  = today_text.lower()

    # 레이어 키워드 매칭
    matched_layers = []
    for layer, kws in LAYER_KEYWORDS.items():
        if any(k in signal_lower for k in kws):
            matched_layers.append(layer)

    # 오늘 리포트에서 해당 키워드 등장 여부
    kw_hits = sum(1 for kw in signal_lower.split()
                  if len(kw) > 4 and kw in today_lower)

    if kw_hits >= 4:   return 3  # 명확 실현
    elif kw_hits >= 2: return 2  # 부분 실현
    elif kw_hits >= 1: return 1  # 희미한 연관
    else:              return 0  # 미실현

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--today', default=datetime.now().strftime('%Y-%m-%d'))
    args = parser.parse_args()

    today_str     = args.today
    yesterday_str = (datetime.strptime(today_str, '%Y-%m-%d') - timedelta(days=1)).strftime('%Y-%m-%d')

    today_text     = load_report_text(today_str)
    yesterday_text = load_report_text(yesterday_str)

    if not today_text:
        print(f"⚠️  오늘({today_str}) 리포트 없음 — 스킵")
        return
    if not yesterday_text:
        print(f"⚠️  어제({yesterday_str}) 리포트 없음 — S08 예측 기준 없음")
        return

    # 어제 S08 추출
    s08_m = re.search(r'## S08.*?\n(.*?)(?=\n## |\Z)', yesterday_text, re.DOTALL)
    if not s08_m:
        print("⚠️  어제 S08 섹션 없음")
        return

    watchlist = []
    for m in re.finditer(r'\d+\.\s+\*\*(.+?)\*\*\s*[—-]\s*(.+?)(?=\n\d+\.|\Z)',
                          s08_m.group(1), re.DOTALL):
        watchlist.append({'signal': m.group(1).strip(), 'detail': m.group(2).strip()[:200]})

    if not watchlist:
        print("⚠️  어제 S08 예측 항목 없음")
        return

    # 채점
    scores = []
    for w in watchlist:
        combined = w['signal'] + ' ' + w['detail']
        s = score_signal(combined, today_text)
        scores.append({'signal': w['signal'], 'score': s,
                       'label': {3:'실현',2:'부분실현',1:'연관',0:'미실현'}[s]})

    total    = len(scores)
    realized = sum(1 for s in scores if s['score'] >= 2)
    accuracy = round(realized / total * 100) if total else 0

    record = {
        'date':           today_str,
        'prediction_date': yesterday_str,
        'total_signals':  total,
        'realized':       realized,
        'accuracy_pct':   accuracy,
        'scores':         scores,
        'scored_at':      datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
    }

    with open(SCORE_LOG, 'a') as f:
        f.write(json.dumps(record, ensure_ascii=False) + '\n')

    print(f"Stage 2 채점 완료 — {today_str}")
    print(f"예측 정확도: {accuracy}% ({realized}/{total} 실현)")
    for s in scores:
        icon = '✅' if s['score']>=2 else ('🔶' if s['score']==1 else '❌')
        print(f"  {icon} [{s['label']}] {s['signal'][:60]}")

if __name__ == '__main__':
    main()
