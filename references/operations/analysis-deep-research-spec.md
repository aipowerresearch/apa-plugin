# Analysis Deep Research — 작성 명세

> 매주 수요일 08:00 발행되는 deep analysis 포스트의 구조·메타 명세.
> SEO/AEO/GEO 최적화로 오가닉 트래픽 + AI 인용 + 사이트 authority 강화 목적.

## 글 구조 (3000+ 단어)

### 1. 도입 (300-500 단어)
- 핵심 질문 1개 (헤드라인과 직결)
- 1-2문장 직답 (AEO 최적화 — LLM이 인용하기 쉬운 형태)
- 왜 지금 이 토픽이 중요한가 (시그널 등장 배경)

### 2. 본문 H2 4~6개 (각 500-700 단어)
APA 10-Layer 프레임워크에 매핑하여 구조 분석:
- Compute Layer (L1-L2)
- Model Layer (L3-L4)
- Platform Layer (L5-L6)
- Capital Layer (L7)
- Geopolitics/Regulation (L8-L9)
- Macro Impact (L10)

각 H2는 사실 → 분석 → 시사점 순서.

### 3. 6개월 시사점 (300-500 단어)
이 신호가 6개월 내 어떤 구조 변화를 만들 가능성이 큰가.
시나리오 A/B/C 가중치 변화 명시.

### 4. 결론 + Forward View (200-300 단어)
- Executive 요약 3 bullet
- 다음 watch list (구체적 트리거 이벤트)

## SEO 메타 (필수)

### `<title>` 60자 이내
패턴: `<핵심 주체> <행동 동사> <레이어/구조>: <연도>`
예: `NVIDIA Locks Compute Layer 2026: Why GB200 Pricing Power Is Permanent`

### `<meta name="description">` 150-160자
도입부 핵심 직답 + CTA ("Read the full structural analysis").

### `<link rel="canonical">`
`https://aipoweratlas.com/analysis/<slug>-{en,ko}.html`

### hreflang
```html
<link rel="alternate" hreflang="en" href=".../analysis/<slug>-en.html">
<link rel="alternate" hreflang="ko" href=".../analysis/<slug>-ko.html">
<link rel="alternate" hreflang="x-default" href=".../analysis/<slug>-en.html">
```

## JSON-LD (필수 2종)

### Article schema
```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "<title>",
  "description": "<meta description>",
  "datePublished": "YYYY-MM-DD",
  "dateModified": "YYYY-MM-DD",
  "author": {"@type": "Organization", "name": "AI Power Atlas", "url": "https://aipoweratlas.com"},
  "publisher": {"@type": "Organization", "name": "AI Power Research", "logo": {"@type": "ImageObject", "url": ".../apa_logo_dark_gold.png"}},
  "image": "<og:image URL>",
  "wordCount": 3500,
  "inLanguage": "en"
}
```

### FAQPage schema (AEO)
글 끝에 FAQ 블록 (3-5개 질문) 추가:
```json
{
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "...", "acceptedAnswer": {"@type": "Answer", "text": "..."}}
  ]
}
```

## OpenGraph + Twitter Card

```html
<meta property="og:type" content="article">
<meta property="og:title" content="...">
<meta property="og:description" content="...">
<meta property="og:image" content=".../images/analysis-<slug>.png">
<meta property="og:url" content=".../analysis/<slug>-en.html">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="...">
<meta name="twitter:description" content="...">
<meta name="twitter:image" content=".../images/analysis-<slug>.png">
```

## AEO/GEO 추가 규칙

### 인용 가능한 단언
"X는 Y 때문에 Z이다" 형태의 명확한 문장. LLM이 그대로 따올 수 있도록.

### 출처 인라인
모든 사실 주장에 `[Source: ...]` 인라인 (PDF·블로그처럼 footnote 사용 안 함).

### 내부 링크
같은 사이트의 daily report·weekly synthesis로 ≥ 3개 링크 (사이트 authority 강화).

### 외부 링크
1차 출처 (회사 공식 발표, 학술 논문, 정부 문서) 우선. 2차 매체 인용 시에도 1차 URL 함께 표기.

## 토픽 선정 알고리즘 (방식 C 자동)

### 입력 데이터
- 직전 7일 daily 리포트의 S01 이벤트 (총 ≈21개)
- 가장 최근 weekly synthesis의 Dominant Narrative

### 가중치
```
weight = (Power Score) × (Layer Tension Multiplier) × (Recurrence Count)

- Power Score: S01 이벤트 점수 (0-100)
- Layer Tension Multiplier: 같은 레이어 충돌 신호가 여러 건이면 ×1.5
- Recurrence Count: 같은 주체·같은 패턴이 N일 등장 → ×N
```

### 선정 절차
1. 21개 이벤트를 (주체, 레이어, 패턴) 키로 클러스터링
2. 각 클러스터의 weight 합산
3. weight 가장 큰 클러스터 1개 선정
4. 슬러그 생성 (`<key-entity>-<key-action>-<month>-<year>`)
5. 선정 메모: `outputs/_logs/analysis-topic-selection-YYYY-MM-DD.md`

### 중복 차단
직전 12주 발행된 토픽과 슬러그 70% 이상 일치 시 차순위 클러스터로 대체.
