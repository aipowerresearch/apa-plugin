#!/usr/bin/env python3
"""
AI Power Atlas — Stage 3: Weekly Meta-Analysis (일요일 자동 실행)
이번 주 예측 점수 + 레이어 패턴 분석 → 다음 주 학습 메모 생성.
실행: python3 scripts/weekly_meta_analysis.py [--week 2026-W17]
"""

import os, re, json, glob, argparse
from datetime import datetime, timedelta
from collections import defaultdict, Counter

APA_ROOT  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KB_DIR    = os.path.join(APA_ROOT, 'references', 'knowledge-base')
SCORE_LOG = os.path.join(KB_DIR, 'prediction_scores.jsonl')
KB_DAILY  = os.path.join(KB_DIR, 'daily_records.jsonl')
META_DIR  = os.path.join(KB_DIR, 'meta-memos')

os.makedirs(META_DIR, exist_ok=True)

def load_jsonl(path):
    if not os.path.exists(path): return []
    records = []
    with open(path) as f:
        for line in f:
            try: records.append(json.loads(line))
            except: pass
    return records

def get_week_dates(week_str):
    """2026-W17 → 해당 주 날짜 목록 (월~일)"""
    year, week = int(week_str[:4]), int(week_str[6:])
    monday = datetime.strptime(f'{year}-W{week:02d}-1', '%G-W%V-%u')
    return [(monday + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(7)]

def analyze_layer_frequency(daily_records, week_dates):
    """이번 주 S01 이벤트에서 레이어 등장 빈도"""
    layer_count = Counter()
    high_impact = []
    for r in daily_records:
        if r.get('date') not in week_dates: continue
        for ev in r.get('events', []):
            for layer in re.findall(r'L\d+', ev.get('layer', '')):
                layer_count[layer] += 1
            if ev.get('impact_score', 0) >= 4.5:
                high_impact.append({'date': r['date'], 'title': ev['title'],
                                     'score': ev['impact_score'], 'layer': ev['layer']})
    return layer_count, high_impact

def main():
    parser = argparse.ArgumentParser()
    # 기본값: 현재 ISO 주차
    now = datetime.now()
    default_week = now.strftime('%G-W%V')
    parser.add_argument('--week', default=default_week)
    args = parser.parse_args()

    week_str  = args.week
    week_dates = get_week_dates(week_str)

    scores       = load_jsonl(SCORE_LOG)
    daily_recs   = load_jsonl(KB_DAILY)

    # 이번 주 점수만 필터
    week_scores = [s for s in scores if s.get('date') in week_dates]

    # 예측 정확도 집계
    if week_scores:
        avg_acc    = round(sum(s['accuracy_pct'] for s in week_scores) / len(week_scores))
        total_sig  = sum(s['total_signals']  for s in week_scores)
        total_real = sum(s['realized']       for s in week_scores)
    else:
        avg_acc = total_sig = total_real = 0

    # 레이어 빈도 분석
    layer_freq, high_impact = analyze_layer_frequency(daily_recs, week_dates)
    top_layers  = layer_freq.most_common(3)
    cold_layers = [l for l,_ in Counter({k:v for k,v in layer_freq.items()}).most_common()[:-4:-1]]

    # 전체 누적 정확도 트렌드 (최근 4주)
    all_weeks_acc = defaultdict(list)
    for s in scores:
        d = s.get('date','')
        if not d: continue
        wk = datetime.strptime(d, '%Y-%m-%d').strftime('%G-W%V')
        all_weeks_acc[wk].append(s['accuracy_pct'])
    trend = {w: round(sum(v)/len(v)) for w,v in sorted(all_weeks_acc.items())[-4:]}

    # ── 메모 작성 ──────────────────────────────────────
    memo_path = os.path.join(META_DIR, f'{week_str}_meta-memo.md')
    with open(memo_path, 'w') as f:
        f.write(f"""# AI Power Atlas — {week_str} 주간 메타 분석 메모
생성일: {datetime.now().strftime('%Y-%m-%d %H:%M')}

---

## 1. 예측 정확도 (Stage 2 채점 결과)

| 항목 | 값 |
|------|-----|
| 이번 주 평균 정확도 | **{avg_acc}%** |
| 총 예측 신호 수 | {total_sig}개 |
| 실현된 신호 | {total_real}개 |

### 일별 상세
""")
        for s in week_scores:
            icon = '🟢' if s['accuracy_pct']>=60 else ('🟡' if s['accuracy_pct']>=40 else '🔴')
            f.write(f"- {s['date']}: {icon} {s['accuracy_pct']}% ({s['realized']}/{s['total_signals']})\n")
            for sc in s.get('scores', []):
                tag = '✅' if sc['score']>=2 else ('🔶' if sc['score']==1 else '❌')
                f.write(f"  - {tag} {sc['signal'][:70]}\n")

        f.write(f"""
---

## 2. 레이어 활동 패턴

### 이번 주 핫 레이어 (Top 3)
""")
        for layer, cnt in top_layers:
            f.write(f"- **{layer}**: 이벤트 {cnt}건 등장\n")

        f.write(f"""
### 이번 주 고임팩트 이벤트 (Score ≥ 4.5)
""")
        for ev in high_impact:
            f.write(f"- [{ev['date']}] **{ev['title'][:70]}** — {ev['layer']} (Score: {ev['score']})\n")

        f.write(f"""
---

## 3. 4주 정확도 트렌드

| 주차 | 정확도 |
|------|--------|
""")
        for wk, acc in trend.items():
            arrow = '↑' if acc >= 60 else ('→' if acc >= 40 else '↓')
            f.write(f"| {wk} | {acc}% {arrow} |\n")

        # 다음 주 권고사항 자동 생성
        hottest_layer = top_layers[0][0] if top_layers else 'L1'
        f.write(f"""
---

## 4. 다음 주 학습 권고사항

**정확도 기반 조정:**
""")
        if avg_acc >= 70:
            f.write("- 현재 예측 패턴이 효과적입니다. S08 신호 구체성 유지 (수치 포함).\n")
        elif avg_acc >= 50:
            f.write("- 예측 정확도 중간 수준. S08 신호를 더 구체적인 기업명/수치로 작성 권장.\n")
        else:
            f.write("- 예측 정확도 낮음. S08 작성 시 레이어 연결 메커니즘 명시 강화 필요.\n")

        f.write(f"""
**레이어 집중 조정:**
- 다음 주 {hottest_layer} 관련 소스 수집 우선순위 상향 (이번 주 최다 활동 레이어)
- 크로스레이어 시나리오: {top_layers[0][0] if top_layers else 'L1'} ↔ {top_layers[1][0] if len(top_layers)>1 else 'L2'} 피드백 루프 집중 모니터링

---
*이 메모는 scripts/weekly_meta_analysis.py가 자동 생성합니다.*
*다음 생성: 다음 주 일요일 파이프라인 완료 후*
""")

    print(f"Stage 3 메타 분석 완료 — {week_str}")
    print(f"예측 정확도: {avg_acc}% | 핫 레이어: {[l for l,_ in top_layers]}")
    print(f"저장: {memo_path}")

    return memo_path

if __name__ == '__main__':
    main()
