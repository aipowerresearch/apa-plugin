---
name: pdf-publisher
description: PDF 3종 생성 (en, ko, en-ko 결합). 트리거 — "PDF", "pdf", "/apa:pdf", 파이프라인 Step 3 자동 호출.
---

오늘 daily report를 3종 PDF로 변환. 구독 등급별 차등 다운로드 대비.

## 산출물 (3개)
1. `outputs/pdf/en/YYYY-MM-DD_<DoW>_daily-report_en.pdf` — EN 단독 ($20 구독)
2. `outputs/pdf/ko/YYYY-MM-DD_<DoW>_daily-report_ko.pdf` — KO 단독 ($20 구독)
3. `outputs/pdf/en-ko/YYYY-MM-DD_<DoW>_daily-report_en-ko.pdf` — 결합 ($30 구독)

향후 다국어 확장 시 동일 패턴 (`_en-ja.pdf`, `_en-zh.pdf` 등).

## 입력
- `outputs/reports/en/YYYY-MM-DD_<DoW>_daily-report_en.md` (EN PDF + 결합 EN 섹션 소스)
- `outputs/reports/ko/YYYY-MM-DD_<DoW>_daily-report_ko.md` (KO PDF + 결합 KO 섹션 소스)

## 페이지 균형
- EN PDF ≥ 6페이지
- KO PDF ≥ 6페이지
- 결합 PDF ≥ 13페이지 (EN 6+ + 페이지 구분 + KO 6+)

## 한글 폰트
fontconfig 이름 `'Noto Sans CJK KR'` 사용 (file URL보다 빠름).
필요 시 `fc-cache -f ~/.local/share/fonts/` 실행.

## 웹 동기화
완료 후 각 PDF를 `web/pdf/<lang>/`에도 복사.
URL: `https://aipoweratlas.com/pdf/<lang>/YYYY-MM-DD_<DoW>_daily-report_<lang>.pdf`
