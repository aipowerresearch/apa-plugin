---
name: kb-daily-updater
description: 지식 베이스(KB) 일간 갱신 — Stage 1 추출 + Stage 2 예측 채점. 트리거 — "KB 업데이트", "지식 베이스", "kb update", "/apa:kb-update", 매일 08:30 KST 자동 실행.
---

오늘 daily 리포트에서 핵심 신호·예측을 추출하고, 과거 예측의 적중률을 채점.

## Stage 1 — 신호 추출
```bash
APA_ROOT=$(find /sessions -name "id_rsa" 2>/dev/null | grep -i "/mnt/.*apa.*/ssh/" | head -1 | xargs dirname | xargs dirname)
TODAY=$(date +%Y-%m-%d)
cd $APA_ROOT && python3 plugin/scripts/build_knowledge_base.py --date $TODAY
```

## Stage 2 — 예측 채점
```bash
cd $APA_ROOT && python3 plugin/scripts/score_predictions.py --date $TODAY
```

## 산출물
- `outputs/knowledge-base/daily_records.jsonl` (append)
- `outputs/knowledge-base/prediction_scores.jsonl` (append)
- `outputs/knowledge-base/kb_summary.json` (overwrite)

## Idempotency
중복 실행 시 같은 날짜 record는 1개만 유지 (덮어쓰기). 안전.
