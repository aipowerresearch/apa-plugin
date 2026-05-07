# APA Daily Pipeline — Standard Templates

이 폴더의 파일들은 매일 파이프라인 실행 시 **반드시 참조해야 하는 표준**입니다. 신규 생성 파일은 구조·항목·변수 모두 이 표준과 일치해야 합니다.

---

## 1. Daily Report (PDF 생성 소스)

표준: 2026-04-23 (목) L7+L8 리포트

- `report/STANDARD_daily-report_en.md` — **영어 전용** 버전 (필드 라벨·본문 모두 영어) — 원본
- `report/STANDARD_daily-report_ko.md` — **한국어 전용 + 한국 시장 보강** 버전 (영어 원문 충실 번역 + S09 지역 시장 섹션)
- `report/STANDARD_daily-report_v1_bilingual.md` — **Legacy 참고용만** (더 이상 생성 금지)

**절대 규칙**: PDF 생성 시 `_en.md` + `_ko.md` 두 분리본을 사용해야 EN 섹션 / KO 섹션이 깔끔하게 분리된다.
**`_v1.md`(한영 병기) 생성 금지** — 혼선 방지 목적. 2026-04-25부터 legacy `_legacy_v1/` 폴더로 이동 처리했다.

### 매일 파이프라인 Step 2 산출 규칙 (절대)

리포트 생성 시 **두 파일만** 생성:
1. `outputs/reports/YYYY-MM-DD_[요일]_*_daily-report_en.md` (영어 전용 — PDF EN 섹션용)
2. `outputs/reports/YYYY-MM-DD_[요일]_*_daily-report_ko.md` (한국어 전용 + 한국 시장 보강 — PDF KO 섹션용)

### 지역 시장 정보 보강 규칙 (절대)

각 언어별 리포트는 영어 원문의 **충실 번역 + 해당 언어 커버리지 지역 정보 보강**으로 구성한다. 독자에게 글로벌 신호(EN)와 자국 시장 파급(지역 보강)을 동시에 전달한다.

**현재 적용**: `_ko.md` — 한국 시장 보강 필수
**향후 확장**: `_ja.md` (일본), `_zh.md` (중국), `_es.md` (스페인/라틴아메리카) — 동일 원칙

**한국 시장 보강 필수 항목**:
- 반도체 공급망: 삼성전자 HBM / SK hynix HBM3E·HBM4 / TSMC·삼성 파운드리
- 국내 AI 기업: 네이버 HyperCLOVA X / 카카오 Kanana / LG EXAONE / Upstage
- AI 정책: 과기정통부 AI 기본법 / 산업부 AI 반도체 펀드 / 국가AI위원회
- 시장 파급: 코스피 AI 섹터 / 원화 환율 / 국내 VC
- 노동 정책: 고용부 AI 직업전환 / 청년 엔트리 고용
- 규제 정렬: 한국 AI Safety Institute / EU·미 AISI 벤치마크

**보강 형식 (택 1)**:
- 인라인: 각 S01 이벤트 `Summary` 직후 `**한국 시장 파급 (KO 추가)**:` 1–2문장 블록
- 별도 섹션 (권장): S08 이후 `## S09 | 한국 시장 보강 / Regional Market Addendum (KO-specific)` 300자 이상

자동 검수: `scripts/verify_daily.sh` 의 `_ko.md 한국 시장 보강` 체크로 강제. S09 섹션 존재 OR 인라인 블록 ≥2 AND 한국 키워드(삼성·SK hynix·네이버 등) 존재 시 통과.

---

## 2. Blog HTML

표준: 2026-04-24 (금) L9+L10 블로그

- `blog-html/STANDARD_blog_en.html` — 영어 포스트 표준
- `blog-html/STANDARD_blog_ko.html` — 한국어 포스트 표준

**절대 규칙**: 매일 블로그 HTML 생성 시 이 파일을 읽고 본문/메타데이터만 교체한다. 다음 요소는 절대 빠지면 안 된다:
- `<script type="application/ld+json">` NewsArticle schema
- `theme-toggle` 버튼 + localStorage `apa-theme` JS
- `nav-cta` Subscribe 링크
- `apa_favicon` 파비콘 2곳
- `#scroll-top` 버튼 + 스크롤 이벤트 JS
- 메뉴 4개: `Blog (active)` / `10-Layer Map` / `Weekly` / `About` (EN) / `블로그` / `10-레이어 맵` / `주간 종합` / `심층분석` (KO)
- `lang-selector` **반드시 `<a href>`**, `<button onclick>` 금지
- `article-header` + `author-block` + `article-meta` + `article-desc`
- `article-body`에 실제 본문 4–6개 h2 섹션 + blockquote + hr + 향후 6개월 함의 단락
- `post-nav` (prev + next) — 다음날 포스트 생성 시 전날 파일의 next도 갱신

---

## 3. Newsletter (이메일 HTML)

표준: 2026-04-23 (목) L7+L8 뉴스레터

- `newsletter/STANDARD_newsletter_free-en.html` — 무료 영어 (NL-01 Free Daily)
- `newsletter/STANDARD_newsletter_free-ko.html` — 무료 한국어 (NL-01 Free Daily)
- `newsletter/STANDARD_newsletter_pro-en.html` — Pro 영어 (NL-02 Pro Daily)
- `newsletter/STANDARD_newsletter_pro-ko.html` — Pro 한국어 (NL-02 Pro Daily)

**절대 규칙**: 매일 파이프라인 Step 4는 **4개 파일 모두 생성**한다:
1. `outputs/newsletters/YYYY-MM-DD_[요일]_newsletter_free-ko.html`
2. `outputs/newsletters/YYYY-MM-DD_[요일]_newsletter_free-en.html`
3. `outputs/newsletters/YYYY-MM-DD_[요일]_newsletter_pro-ko.html`
4. `outputs/newsletters/YYYY-MM-DD_[요일]_newsletter_pro-en.html`

Pro만 만들고 Free를 빠뜨리는 경우가 반복되어 왔다 — 체크리스트 Step 4는 4개가 아니면 미완료 처리한다.

### 3-1. Free 템플릿 시그니처 (NL-01 Design B-2 Slate-Indigo · v3)

| 항목 | 값 |
|------|----|
| 1행 주석 | `<!-- APA TEMPLATE: NL-01 Free Daily ({KO|EN}) · Design B-2 Slate-Indigo · v3 -->` |
| 디자인 | Slate-Indigo 그라데이션 헤더(`#1e293b → #312e81`) + 컬러 이벤트 카드(#10b981 / #3b82f6 / #059669) |
| 구성 요소 | (a) `무료/FREE` 배지 · Issue # (b) 블로그 링크 제목 (c) S01 3 이벤트 카드 (짧은 2문장 요약) (d) 시나리오 확률 막대(A/B/C) — 퍼센트만, 분석은 Pro에 표시 (e) 내일 프리뷰 1줄 (f) **Pro 업그레이드 CTA** (g) 무료 구독자 footer |
| 파일 크기 | 약 **10–18KB** (표준 ~14KB) |
| 필수 문구 | `Pro로 업그레이드` / `Upgrade to Pro` · `무료 구독자로 수신` / `Free subscriber` |
| 변수 개수 | 34 |

### 3-2. Pro 템플릿 시그니처 (NL-02 Design C-5 Gold+Slate · v5)

| 항목 | 값 |
|------|----|
| 1행 주석 | `<!-- APA TEMPLATE: NL-02 Pro Daily ({KO|EN}) · Design C-5 Gold+Slate (readable) · v5 -->` |
| 디자인 | Gold(#c9a84c) + Slate(#2d3748) 컬러 시스템 · Warm beige background(#c8c4bc) · Georgia italic 헤더 |
| 구성 요소 | (a) Gold top rule + `PRO` 배지 + `Pro 에디션/Pro Edition` 라벨 · Issue # (b) Italic Georgia 제목 (c) **S01 3 이벤트** — 각 5–7문장 풀 분석 포함 (d) **S03 Cross-Layer Cascade** — 레이어 간 연쇄 효과 분석 (e) **S04 Stakeholder Power Shift** — 이해관계자 권력 이동 분석 (f) **S05 Scenario Sensitivity** — A/B/C 시나리오 + 내러티브 (g) **S06 WoW Delta** — 주간 변화량 (h) **S07 6-Month Outlook** — 6개월 구조 전망 (i) **S08 Signal Watch** — 내일 관찰 엔티티 (j) **PDF 다운로드 링크** (k) Pro 구독자 footer |
| 파일 크기 | 약 **28–40KB** (표준 ~36KB) |
| 필수 문구 | `PRO` 배지 HTML · `Pro 에디션/Pro Edition` · `Pro 구독자로 수신` / `Pro subscriber` · `/pdf/YYYY-MM-DD_daily-report.pdf` |
| 변수 개수 | 39 |

### 3-3. 자동 검수 (Step 4)

`scripts/verify_daily.sh` 는 Free/Pro 각각 다음을 검수한다:

- **Free**: NL-01 주석 + Design B-2 + 업그레이드 CTA + Free footer + 8–20KB
- **Pro**: NL-02 주석 + Design C-5 + PRO badge + Pro footer + PDF 링크(당일 날짜) + ≥25KB

하나라도 위반 시 `Pro 시그니처` / `Free 시그니처` 체크 FAIL로 표기되며 파이프라인 미완료 처리.

---

## 변경 이력

- 2026-04-25: 템플릿 저장 (04-23 리포트 + 04-24 블로그 + 04-23 뉴스레터). 그 이전 파이프라인 불일치(PDF KO 중복, 블로그 스키마 누락, 무료 뉴스레터 누락) 시정.
