---
name: analysis-publisher
description: Deep research analysis 발행 (3000+ 단어, SEO/AEO/GEO 최적화). 트리거 — "analysis", "deep analysis", "/apa:analysis", 매주 수요일 08:00 KST 자동 (apa-analysis-weekly).
---

매주 수요일, 그 주의 daily/weekly 신호 중 가장 큰 것을 토픽으로 자동 선정 → 3000+ 단어 deep research 작성 → SEO/AEO/GEO 최적화 → en+ko 짝 발행.

## 입력
- 직전 7일 daily 리포트 (월~화): `outputs/reports/{en,ko}/`
- 가장 최근 weekly synthesis: `outputs/reports/weekly/{en,ko}/`
- references/operations/analysis-deep-research-spec.md (글 구조·SEO/AEO/GEO 명세)
- references/framework/* (Power Index, Shift Tracker, Glossary 활용)
- references/operations/translation-policy.md + translation-policy-ko.md

## Phase 1: 토픽 자동 선정 (방식 C)

### 토픽 선정 알고리즘
1. 직전 7일 daily의 모든 S01 이벤트 수집 (≈21개)
2. 각 이벤트의 (Power Score × Layer Tension × 횟수)로 가중 합계 계산
3. 가장 큰 클러스터 1개 선정 — 같은 주체/같은 레이어/같은 패턴이 여러 일자에 반복 등장한 신호
4. 토픽 슬러그 생성 (예: `nvidia-power-shift-may-2026`)

### 산출 메모
`outputs/_logs/analysis-topic-selection-YYYY-MM-DD.md`에 선정 사유 기록 (어떤 신호들을 합쳤는지, 가중치 점수 등).

## Phase 2: 작성

### EN 원문 작성 (3000+ 단어)
- 도입 (300-500단어): 신호의 등장과 의미
- 본문 4-6 H2 (각 500-700단어): 구조 분석 (compute → model → platform → capital → reg)
- 6개월 시사점 (300-500단어)
- 결론 + Forward View (200-300단어)

### KO 번역 (translation-policy 5-Phase)
공통 정책 적용 — 자체평가 8.0/10 이상 통과 후 발행.

## Phase 3: SEO/AEO/GEO 메타 (절대)

### 공통 (모든 페이지)
- `<title>` 60자 이내, 핵심 키워드 좌측 배치
- `<meta name="description">` 150-160자, CTA 포함
- canonical URL
- hreflang 쌍 (en ↔ ko)

### Article schema (JSON-LD)
```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "...",
  "datePublished": "YYYY-MM-DD",
  "dateModified": "YYYY-MM-DD",
  "author": {"@type":"Organization","name":"AI Power Atlas"},
  "publisher": {...},
  "wordCount": 3000+,
  "inLanguage": "en|ko"
}
```

### OpenGraph + Twitter Card
- og:type=article, og:title, og:description, og:image (1200x630)
- twitter:card=summary_large_image

### AEO (Answer Engine Optimization)
- 도입부에 핵심 질문 → 1-2문장 직답 (LLM 인용 최적화)
- FAQ 블록 1개 이상 (구조화 데이터 FAQPage schema)

### GEO (Generative Engine Optimization)
- 인용 가능한 단언 문장 명확하게 (예: "X는 Y 때문에 Z이다")
- 출처 링크 인라인 (`[Source: ...]`)

## Phase 4: 산출물

- `web/analysis/<slug>-en.html`
- `web/analysis/<slug>-ko.html`
- `outputs/blog/{en,ko}/<slug>.md` (소스 백업)

## Phase 5: 인덱스 갱신
- `web/analysis/index.html`, `index_kr.html` — 새 카드 맨 위 추가, 기존 "Coming Soon" 카드 1개 제거
- `web/blog/index.html`, `index_kr.html` — Deep Analysis 카드 8개 영역 갱신 (오늘 발행 카드 맨 앞)

## 자동 검증
- EN 본문 단어 수 ≥ 3000
- KO 본문 자체평가 ≥ 8.0/10
- 메타 태그 8종 모두 존재 (title, description, og × 3, twitter × 2, canonical)
- JSON-LD Article schema 유효
- hreflang 쌍 존재 (en ↔ ko)
