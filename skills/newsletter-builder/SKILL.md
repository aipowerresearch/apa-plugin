---
name: newsletter-builder
description: 4종 뉴스레터 HTML 생성 (free-en + free-ko + pro-en + pro-ko). 트리거 — "뉴스레터", "newsletter", "/apa:newsletter", 파이프라인 Step 4 자동 호출.
---

오늘 daily report를 입력으로 받아 4종 뉴스레터 HTML을 생성한다.

## 절대 규칙
- **4개 파일 모두 생성** — 2개만 만들면 미완료
- Free와 Pro는 **구조가 명확히 다름** (Free ~14KB 요약, Pro ~36KB 풀 분석)
- STANDARD 템플릿 복사 → 본문 8섹션 모두 오늘 콘텐츠로 교체
- **직전일 회귀 차단**: D-2 S01 키워드가 오늘 산출물에 ≤ 3회 등장 (4회 이상이면 본문 미교체 의심)

## 입력
- `outputs/reports/{en,ko}/YYYY-MM-DD_<DoW>_daily-report_<lang>.md`
- references/templates/newsletter/STANDARD_newsletter_{free,pro}-{en,ko}.html
- references/operations/newsletter-conversion.md (Section Mapping, S05/S07 작성 규칙)

## PDF 링크 주입 (구독 등급 분기)
- `{{PDF_LINK_EN}}` → en 단독 구독자
- `{{PDF_LINK_KO}}` → ko 단독 구독자
- `{{PDF_LINK_BILINGUAL}}` → en-ko 결합 구독자

## 산출물
`outputs/newsletters/{free,pro}-{en,ko}/YYYY-MM-DD_<DoW>_newsletter_{free,pro}-{en,ko}.html`
