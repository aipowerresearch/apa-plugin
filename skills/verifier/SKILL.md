---
name: verifier
description: 자동 검수 (verify_daily.sh) 단독 실행. 트리거 — "검수", "verify", "/apa:verify", 파이프라인 Step 12 자동 호출.
---

`scripts/verify_daily.sh`를 실행하여 일간 산출물의 무결성을 자동 검사.

## 인자
- 날짜 (YYYY-MM-DD; 미지정 시 오늘)
- `--skip-server` (서버 업로드 검증 건너뜀)

## 검사 6개 영역 (29 체크포인트)
- [Step 2] 리포트 — `_en.md` + `_ko.md` 존재, 한글 비율, 번역 충실도
- [Step 3] PDF 3종 — 페이지 수 ≥ 13(결합), 크기 ≥ 200KB
- [Step 4] 뉴스레터 4종 — 각 ≥ 5KB, 본문 매칭, 직전일 회귀 차단
- [Step 6] 블로그 HTML — 8요소, prev/next 갱신
- [Step 7] 인덱스·아카이브·인텔리전스 — 오늘 날짜 포함
- [Step 11] 서버 업로드 — 블로그 HTML·PDF 서버 존재 확인

## 출력
- 종료 코드 0 = PASS, 1 = FAIL
- 보고: `verify_daily.sh PASS/TOTAL PASS` 또는 실패 항목 나열
