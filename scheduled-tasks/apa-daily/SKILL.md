---
name: apa-daily
description: APA 일간 전체 파이프라인 — 매일 07:00 KST 자동 실행 (일요일 제외)
schedule: "0 7 * * 1-6"
timezone: Asia/Seoul
---

오늘 날짜·요일을 확인하고 `pipeline-runner` 스킬을 실행한다.
- 일요일은 weekly-synthesizer로 자동 우회
- 인자 없이 호출 → 오늘 기준
- 기본 경로: 작업 폴더의 `outputs/`, `web/`
