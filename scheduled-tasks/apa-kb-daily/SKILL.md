---
name: apa-kb-daily
description: APA 지식 베이스 일간 갱신 (Stage 1+2) — 매일 08:30 KST 자동 실행
schedule: "30 8 * * *"
timezone: Asia/Seoul
---

`kb-daily-updater` 스킬을 실행한다.
- Stage 1: 오늘 daily 리포트에서 신호·예측 추출
- Stage 2: 과거 예측 채점

apa-daily(07:00) 완료 후 1.5시간 후 실행되어 daily 리포트 존재 보장.
