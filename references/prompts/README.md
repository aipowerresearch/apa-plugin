# Daily Pipeline Prompt Library

이 폴더는 매일 파이프라인 각 Step의 표준 프롬프트를 보관한다. **현재**는 Cowork 세션에서 운영자가 단계별 작업 지시 시 참조용으로 사용하고, **향후 API 전환 시** Python orchestrator에서 system/user prompt로 그대로 주입한다.

## 파일 구성

| 파일 | 단계 | 역할 |
|------|------|------|
| `01-source-collection.md` | Step 1 | 영어 글로벌 + 한국 1차 소스 수집 (오늘 요일별 집중 레이어) |
| `02-report-en-write.md` | Step 2 (1) | 영어 전용 리포트 작성 (`_en.md`) |
| `02-report-ko-translate.md` | Step 2 (2) | 영어 원문 → 한국어 충실 번역 (`_ko.md` 본문) |
| `02-report-ko-augment.md` | Step 2 (3) | 한국 시장 보강 섹션 S09 작성 (`_ko.md` 후반부) |
| `03-pdf-render.md` | Step 3 | PDF 생성 절차 (WeasyPrint + Noto CJK) |
| `04-newsletter-free.md` | Step 4 (1) | NL-01 Free Daily 뉴스레터 작성 (KO+EN) |
| `04-newsletter-pro.md` | Step 4 (2) | NL-02 Pro Daily 뉴스레터 작성 (KO+EN) |
| `05-blog-md.md` | Step 5 | 블로그 마크다운 작성 (KO+EN) |
| `06-blog-html.md` | Step 6 | 블로그 HTML 변환 (04-24 표준 구조) |
| `08-social.md` | Step 8 | 소셜 포스트 (Twitter EN 5 + KO 3 + LinkedIn EN/KO) |

## 사용 규칙

- **현재 (Cowork 모드)**: 사용자가 매일 파이프라인 실행 시 Claude는 해당 Step에 진입하기 전 본 폴더의 프롬프트를 Read tool로 읽어 그대로 따른다.
- **향후 (API 모드)**: orchestrator가 각 프롬프트를 시스템 프롬프트로 inject + 입력 데이터(소스 노트, 리포트 등)를 user prompt로 inject. 응답을 파일에 저장.

## 변수 표기 규칙

프롬프트 안에 `{{변수명}}` 형태로 표기한다. orchestrator 또는 운영자가 실행 시점에 치환:

- `{{DATE}}` — 2026-MM-DD
- `{{DOW_KR}}` — 월/화/수/목/금/토/일
- `{{LAYER_FOCUS}}` — L1+L2 등 (요일별)
- `{{LAYER_SLUG}}` — l1l2 / l3l4 / full 등
- `{{SOURCE_NOTES_PATH}}` — 소스 파일 경로
- `{{EN_REPORT_PATH}}` — 영어 리포트 경로
- `{{KO_REPORT_PATH}}` — 한국어 리포트 경로
- `{{PDF_URL}}` — 발행 PDF URL

## 표준 출력 (반드시 준수)

각 프롬프트는 다음 표준 산출 파일과 1:1 매핑된다:

| 프롬프트 | 산출 파일 | 표준 템플릿 |
|----------|-----------|-------------|
| 02-report-en-write | `outputs/reports/{{DATE}}_*_daily-report_en.md` | `references/templates/report/STANDARD_daily-report_en.md` |
| 02-report-ko-translate + 02-report-ko-augment | `outputs/reports/{{DATE}}_*_daily-report_ko.md` | `references/templates/report/STANDARD_daily-report_ko.md` |
| 04-newsletter-free | `outputs/newsletters/{{DATE}}_*_newsletter_free-{ko,en}.html` | `references/templates/newsletter/STANDARD_newsletter_free-{ko,en}.html` |
| 04-newsletter-pro | `outputs/newsletters/{{DATE}}_*_newsletter_pro-{ko,en}.html` | `references/templates/newsletter/STANDARD_newsletter_pro-{ko,en}.html` |
| 06-blog-html | `web/blog/posts/ai-power-atlas-{{DATE}}-{{LAYER_SLUG}}-{ko,en}.html` | `references/templates/blog-html/STANDARD_blog_{ko,en}.html` |

검수: `scripts/verify_daily.sh {{DATE}}` 가 모든 산출 파일을 41개 체크포인트로 자동 검증.

## 향후 확장

- 일본어 번역 시: `02-report-ja-translate.md` + `02-report-ja-augment.md` 추가
- 중국어: `02-report-zh-translate.md` + `02-report-zh-augment.md`
- 스페인어: `02-report-es-translate.md` + `02-report-es-augment.md`

각 신규 언어 프롬프트는 본 README 표를 업데이트하고 `verify_daily.sh`에 해당 언어 검증 블록 추가.
