---
name: archive-manager
description: 아카이브 인덱스 + 웹 인텔리전스 preview 갱신. 트리거 — "아카이브", "archive", "/apa:archive", 파이프라인 Step 9 자동 호출.
---

매일 파이프라인 말미에 아카이브·인덱스를 일괄 갱신.

## 갱신 대상
- `outputs/archive-index.md` — 일자별 산출물 목록
- `web/intelligence/index.html` — Latest Daily Intelligence preview (오늘로 교체)
- `outputs/execution-log.md` — append-only (references/operations/execution-log-template.md 참조)
