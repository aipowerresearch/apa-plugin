---
name: kb-weekly-analyzer
description: 지식 베이스 주간 메타 분석 (Stage 3). 트리거 — "주간 메타", "kb weekly", "weekly meta analysis", 매주 일요일 09:30 KST 자동 실행.
---

주간 누적된 KB 데이터에서 메타 패턴을 추출하고 시나리오 트래커를 갱신.

## Stage 3 — 주간 메타 분석
```bash
APA_ROOT=$(find /sessions -name "id_rsa" 2>/dev/null | grep -i "/mnt/.*apa.*/ssh/" | head -1 | xargs dirname | xargs dirname)
WEEK=$(date +%G-W%V)
cd $APA_ROOT && python3 plugin/scripts/weekly_meta_analysis.py --week $WEEK
```

## 산출물
- `outputs/knowledge-base/weekly_records.jsonl` (append)
- `outputs/knowledge-base/meta-memos/YYYY-WNN_meta-memo.md`
- `outputs/knowledge-base/diagnostics/YYYY-WNN_diagnostics.json`

## 의존
주중 daily KB 업데이트 (kb-daily-updater)가 4건 이상 완료되어 있어야 함.
