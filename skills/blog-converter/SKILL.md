---
name: blog-converter
description: 블로그 MD + HTML 생성 + 인덱스·아카이브·메인·인텔리전스 매일 갱신. 트리거 — "블로그", "blog", "/apa:blog", 파이프라인 Step 5+6+7 자동 호출.
---

오늘 daily report를 블로그 형식으로 변환 (MD → HTML) + 관련 페이지 5종 동시 갱신.

## 입력
- `outputs/reports/{en,ko}/YYYY-MM-DD_<DoW>_daily-report_<lang>.md`
- references/templates/blog-html/STANDARD_blog_{en,ko}.html
- references/operations/blog-spec.md
- references/operations/blog-html-spec.md
- references/operations/web-update-targets.md (매일 갱신 페이지 정의)
- references/operations/translation-policy.md + translation-policy-ko.md

## Phase 1: 블로그 포스트 생성 (MD + HTML)

### MD
`outputs/blog/{en,ko}/YYYY-MM-DD_<DoW>_blog_<lang>.md`

### HTML 절대 규칙 (8요소 — 누락 시 미완료)
1. JSON-LD schema (Article)
2. theme-toggle (라이트/다크 + localStorage)
3. nav-cta Subscribe (KO: "구독", EN: "Subscribe")
4. apa_favicon
5. #scroll-top
6. post-nav (prev + next)
7. article-header (author-block / meta / desc)
8. article-body (4-6 h2 + blockquote + hr + 6개월 함의)

산출물: `web/blog/posts/ai-power-atlas-YYYY-MM-DD-<lang>.html`

### 한국어판 제목 절대 규칙
KO 블로그 포스트 제목은 **`outputs/reports/ko/...`의 KO 원문에서 추출** (영어 제목 자동 번역 금지).
인덱스·아카이브 카드 제목도 동일 — KO 페이지에는 KO 실제 제목, EN 페이지에는 EN 실제 제목.

## Phase 2: 블로그 인덱스 갱신 (`web/blog/index.html`, `index_kr.html`)

### 피처드 + 그리드 = 총 9개 (절대 규칙)
- **피처드 카드 (1개)**: 가장 최신 포스트 (오늘)
- **그리드 카드 (8개)**: 피처드 **전날부터 역순 8일** = 어제 + 그제 + … + 8일 전

### 중복 차단 검사 (필수)
피처드 ID == 그리드[0] ID이면 FAIL → 즉시 갱신.
검증 절차: 각 카드의 데이터 속성(`data-post-id` 또는 URL)으로 ID 추출 → 중복 시 그리드[0]을 그 다음 일자로 교체.

### Deep Analysis 카드 (8개 표시)
인덱스 하단 Deep Analysis 섹션은 최신 8개 노출 (이전 4개 → **8개**).
출처: `web/analysis/<slug>-{en,ko}.html`의 메타데이터.

## Phase 3: 블로그 아카이브 (`web/blog/archive/index.html`, `index_kr.html`)

### 월별 그루핑 + collapse/expand
- 최신 월(현재 월): expanded (펼침)
- 지난 월들: collapsed (접힘)
- 클릭 시 toggle (JS)
- 각 월 헤더에 카운트 (예: "2026년 5월 (3)")

### 정렬
최신 일자가 맨 위. 같은 일자에 여러 포스트가 있으면 발행 시각 역순.

### 한글판 제목 정합성
`index_kr.html`의 카드 제목은 `outputs/reports/ko/`의 KO 원문 제목 그대로. EN 제목 직역 사용 금지.

## Phase 4: 메인 페이지 SAMPLE INTELLIGENCE (`web/index.html`, `index_kr.html`)

### 갱신 영역
- 날짜 (FRIDAY · MAY 1, 2026 / 금요일 · 2026년 5월 1일)
- "Signal #S01-01" 첫 이벤트 카드 (오늘 daily report S01 Event 1 본문)
- POWER FLOW ANALYSIS, 6-MONTH IMPLICATION, STRATEGIC ACTION 4분면

오늘 리포트의 Event 1 (가장 큰 Power Score)를 기본 사용. EN/KO 각 페이지에 해당 언어 본문.

## Phase 5: 인텔리전스 페이지 (`web/intelligence/index.html`, `index_kr.html`)

### 갱신 영역
- 날짜 헤더 (FRIDAY · MAY 1, 2026)
- Report Structure 8섹션 카드 (S01~S08 — 오늘 리포트 실제 내용 반영)
- "Why This Structure Works" 4개 패널은 정적 (변경 안 함)

## Phase 6: 전날 next 링크 갱신
오늘 포스트 생성 후, 전날 포스트 HTML(KO+EN)의 next 링크가 비어있거나 disabled였다면 오늘 포스트 경로로 교체.

## 자동 검증
- 인덱스 9개 카드 ID 중복 없음
- 아카이브에 오늘 날짜 포함
- 메인·인텔리전스에 오늘 날짜 표시
- 한글판 카드 제목이 KO 원문과 일치
