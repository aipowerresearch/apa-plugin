# APA Owner Operations Guide

> 대표님이 직접 관여해야 하는 업무와 자동화 영역의 구분, 유료/무료 서비스 구현, 블로그 관리 전략
> 작성: 2026-03-21

---

## 1. 일간/주간 파이프라인에서 대표님이 개입하는 업무

### 1.1 현재 파이프라인 흐름

```
07:00 자동 실행 (full-daily)
 ├── ① 뉴스 수집 (news-scanner) .................. 자동
 ├── ② 소스 노트 생성 ............................. 자동
 ├── ③ 8섹션 리포트 생성 (report-generator) ....... 자동
 ├── ④ 블로그 변환 (blog-converter) ............... 자동
 ├── ⑤ 뉴스레터 변환 (newsletter-formatter) ....... 자동
 └── ⑥ 아카이빙 (archive-manager) ................ 자동
```

### 1.2 대표님이 반드시 개입해야 하는 업무

| # | 업무 | 소요 시간 | 빈도 | 왜 자동화 불가인가 |
|---|------|-----------|------|-------------------|
| A | **리포트 품질 검수** | 10~15분 | 매일 | Judgment Axis(S00)의 방향성이 APA의 고유 관점에 맞는지 확인. 자동 생성된 분석이 "뉴스 요약"이 아니라 "권력 이동 해석"인지 판단하는 것은 사람만 가능 |
| B | **시나리오 확률 승인** | 5분 | 매일 | S04 시나리오 확률 변동이 근거에 부합하는지 최종 판단. 자동 생성 시 과민 반응(하루 만에 10% 변동 등)이 나올 수 있음 |
| C | **beehiiv 발송 승인** | 3분 | 매일 | 뉴스레터 최종 발송 전 1회 확인. 오류/오탈자/민감 표현 체크 |
| D | **블로그 포스트 업로드** | 5분 | 매일 | 블로그 HTML 파일을 웹서버에 배포 + blog/index.html 목록에 추가 (아래 §4 참조) |
| E | **주간 시나리오 리뷰** | 20분 | 일요일 | 주간 종합에서 시나리오 방향 전환 여부, 새 시나리오 추가/삭제 판단 |

**합계: 매일 약 25~30분, 일요일 추가 20분**

### 1.3 현재는 개입하지만 향후 자동화 가능한 업무

| 업무 | 자동화 조건 | 예상 시기 |
|------|------------|----------|
| 블로그 HTML 업로드 | 웹서버 자동 배포 설정 (Git push → Netlify/Vercel 자동 빌드) | 호스팅 결정 후 즉시 |
| blog/index.html 목록 갱신 | blog-converter가 목록 페이지도 자동 업데이트하도록 개선 | Phase 2 |
| beehiiv 발송 | beehiiv API 연동으로 자동 발송 (현재 수동 또는 예약) | 구독자 100+ 달성 후 |
| 시나리오 확률 미세 조정 | 과거 데이터 기반 자동 보정 모델 (±3% 이내 자동 승인) | Phase 3 |

### 1.4 절대 자동화해서는 안 되는 업무

- **Judgment Axis (S00) 최종 방향**: APA의 정체성이 걸린 부분. "이건 자동화하면 뉴스 큐레이션 서비스와 차별점이 없어진다"
- **시나리오 신규 추가/삭제**: 분기 단위의 전략적 판단
- **위기 상황 대응**: 예) AI 관련 대형 사건 발생 시 긴급 특별호 발행 여부

---

## 2. 뉴스레터 ↔ 블로그 연계 구조

### 2.1 콘텐츠 관계

```
뉴스레터 (함축적, 모바일 스크롤 3~4회)
 │
 │  모든 섹션 요약 포함 (S01~S08)
 │  각 이벤트에 원문 소스 링크 📎
 │
 └──→ 하단 Blog CTA 블록
       "전체 분석 읽기 →" (KO)
       "Read in English →" (EN)
       │
       ▼
블로그 (풍부한 설명, ~7분 읽기)
 │
 │  동일 8섹션 but 각각 3~5문장으로 확장
 │  S05 크로스 레이어 인사이트 상세
 │  S07 반대 의견 상세
 │  모든 이벤트에 원문 링크
 │
 └──→ 하단 구독 CTA
       "무료 뉴스레터 구독 →"
```

### 2.2 파이프라인 순서 (중요)

뉴스레터가 블로그 URL을 포함하므로, 반드시 블로그가 먼저 생성되어야 합니다:

```
① report 생성 → ② blog 변환 (URL 확정) → ③ newsletter 변환 (blog URL 삽입) → ④ 발송
```

### 2.3 뉴스레터 템플릿 변수 (v2.1 추가분)

| 변수 | 설명 | 예시 |
|------|------|------|
| `{{BLOG_HEADLINE}}` | 블로그 포스트 헤드라인 | "미국 AI 칩 허가제와 Meta $60B AMD 계약" |
| `{{BLOG_URL_KO}}` | KO 블로그 포스트 URL | `/blog/posts/ai-power-atlas-2026-03-21-l9l10.html` |
| `{{BLOG_URL_EN}}` | EN 블로그 포스트 URL | `/blog/posts/ai-power-atlas-2026-03-21-l9l10-en.html` |

---

## 3. 유료/무료 서비스 구분 및 결제 구현

### 3.1 서비스 구분

| 항목 | Free (무료) | Pro ($150/년) | Team ($500/월) |
|------|------------|--------------|----------------|
| 일간 뉴스레터 | ✅ 전문 | ✅ 전문 | ✅ 전문 |
| 블로그 | ✅ 전문 | ✅ 전문 | ✅ 전문 |
| 주간 종합 (Weekly Synthesis) | ❌ | ✅ | ✅ |
| PDF 리포트 (일간+주간) | ❌ | ✅ | ✅ |
| AI Power Index | ❌ | ✅ (출시 시) | ✅ |
| 6개월 시나리오 상세 분석 | ❌ | ✅ | ✅ |
| 팀 대시보드 | ❌ | ❌ | ✅ |
| 맞춤 레이어 브리핑 | ❌ | ❌ | ✅ |
| Slack/이메일 통합 | ❌ | ❌ | ✅ |
| 월간 전략 콜 | ❌ | ❌ | ✅ |

### 3.2 구현 방법: beehiiv 유료 구독 기능

**가장 현실적이고 즉시 가능한 방법: beehiiv Premium Subscription**

beehiiv는 자체 유료 구독 기능을 지원합니다:

1. **beehiiv에서 유료 플랜 설정**
   - Settings → Monetization → Premium Subscriptions 활성화
   - Free tier / Pro tier ($150/yr) 설정
   - Stripe 연동 (결제 처리)

2. **콘텐츠 게이팅 방식**
   - 뉴스레터 발송 시 "Premium-only" 섹션 태그 가능
   - Weekly Synthesis는 Pro 전용으로 태그
   - 일간 뉴스레터는 전체 공개 (획득 채널이므로)

3. **결제 흐름**
   - 구독자 → beehiiv Pro 업그레이드 링크 클릭 → Stripe 결제 → 자동 Pro 뱃지 부여
   - 웹사이트 Pricing 섹션의 "Join Pro" 버튼 → beehiiv 유료 구독 페이지로 연결

### 3.3 Team 플랜 결제

Team 플랜($500/월)은 beehiiv로 처리하기 어렵습니다. 별도 처리가 필요합니다:

- **방법 1 (현재 적합)**: 이메일/폼 문의 → 직접 계약 → Stripe 수동 인보이스
- **방법 2 (향후)**: 자체 대시보드 구축 시 Stripe 결제 통합

### 3.4 웹사이트 Pricing 섹션 변경 필요사항

현재 Pricing 섹션의 버튼은 `mailto:` 링크입니다. 변경 필요:

| 플랜 | 현재 | 변경 후 |
|------|------|---------|
| Free | `#subscribe` 스크롤 | 유지 |
| Pro | `mailto:info@aipoweratlas.com` | beehiiv 유료 구독 URL (Stripe 연동 후) |
| Team | `mailto:info@aipoweratlas.com` | 유지 (고액이므로 직접 소통) |

**구현 순서**:
1. beehiiv Premium Subscription 활성화 + Stripe 연동
2. Pro 전용 콘텐츠 (Weekly Synthesis) 첫 발행
3. 웹사이트 Pro 버튼 URL 교체
4. 뉴스레터 하단에 "Upgrade to Pro" CTA 추가

### 3.5 PDF 리포트 유료 배포

PDF 리포트는 Pro 구독자에게만 제공:
- beehiiv 유료 구독자에게만 발송되는 이메일에 PDF 첨부
- 또는 PDF 다운로드 페이지를 beehiiv 유료 구독자 전용 링크로 제공
- pdf-publisher 스킬이 이미 존재하므로 생성 자체는 자동화 가능

---

## 4. 블로그 관리 단계별 전략

### Phase 1: 수동 관리 (현재 ~ W20)

**현재 상태**: 블로그 포스트는 `blog/posts/` 디렉토리에 개별 HTML 파일로 존재. `blog/index.html` 목록은 수동 갱신.

**매일 할 일**:
1. full-daily 파이프라인이 생성한 `outputs/blog/YYYY-MM-DD_요일_blog_ko.md`, `_en.md` 확인
2. 품질 검수 (리포트 검수와 동시 진행, 추가 5분)
3. blog-converter가 생성한 HTML을 `blog/posts/`에 배치
4. `blog/index.html`과 `blog/index_kr.html` 목록에 새 포스트 항목 추가
5. 웹서버에 업로드

**관리 포인트**:
- 파일명 규칙 준수: `ai-power-atlas-YYYY-MM-DD-lXlY.html` (KO), `-en.html` (EN)
- 태그 일관성: 레이어 번호 + 주제 키워드
- 이전 포스트와 연결: 관련 분석 내부 링크 (선택사항)

### Phase 2: 반자동 관리 (W20 ~ W28)

**목표**: blog/index.html 갱신을 자동화하여 대표님 개입을 최소화

**구현 내용**:
1. blog-converter 스킬 개선: HTML 포스트 생성 시 `blog/index.html`과 `blog/index_kr.html`의 post-list에 자동으로 항목 추가
2. 포스트 메타데이터 JSON 도입: `blog/posts/manifest.json`에 모든 포스트 목록 관리

```json
{
  "posts": [
    {
      "date": "2026-03-21",
      "slug": "ai-power-atlas-2026-03-21-l9l10",
      "title_ko": "...",
      "title_en": "...",
      "tags": ["L9", "L10", "AI Power Atlas"],
      "layer_focus": "L9+L10"
    }
  ]
}
```

3. 목록 페이지가 manifest.json을 읽어 동적으로 포스트 카드를 렌더링 (간단한 JS)

**대표님 개입**: 리포트 품질 검수만 (5분/일). 목록 갱신은 자동.

### Phase 3: 완전 자동 + SEO 최적화 (W28 ~ W40)

**목표**: 블로그가 검색 유입의 주요 채널이 되도록 SEO 강화

1. **정적 사이트 생성기 도입 검토**: 11ty, Astro, Hugo 등
   - 마크다운 → HTML 자동 빌드
   - 태그별, 레이어별 필터링 페이지 자동 생성
   - sitemap.xml, RSS 피드 자동 생성

2. **SEO 요소 추가**:
   - 각 포스트에 meta description, og:image, structured data (Article schema)
   - 레이어별 카테고리 페이지 (예: `/blog/layer/l1/`)
   - 내부 링크 전략: 관련 과거 포스트 자동 추천

3. **자동 배포**:
   - Git push → Netlify/Vercel/GitHub Pages 자동 빌드
   - full-daily 파이프라인이 git commit+push까지 수행
   - 대표님은 "아침에 일어나면 이미 발행되어 있는" 상태

**대표님 개입**: 주 1회 품질 스팟체크 (10분/주). 나머지 완전 자동.

### Phase 4: 성장 최적화 (W40~)

1. **인기 포스트 분석**: Google Analytics 기반 어떤 레이어/주제가 가장 많이 읽히는지 파악
2. **시리즈 콘텐츠**: 특정 주제에 대한 심층 시리즈 (예: "중국 AI 칩 자립 로드맵 5부작")
3. **게스트 분석**: 외부 전문가 기고 수용
4. **인터랙티브 요소**: 시나리오 트래커 실시간 차트, 레이어 히트맵 등

---

## 5. 주간 업무 캘린더 (대표님 기준)

| 요일 | 자동 실행 | 대표님 업무 | 소요 시간 |
|------|-----------|------------|----------|
| 월~토 | 07:00 full-daily | ① 리포트 품질 검수 ② 시나리오 확률 확인 ③ 블로그 업로드 ④ beehiiv 발송 확인 | ~25분 |
| 일 | 08:00 weekly-synthesis | ① 주간 시나리오 방향 리뷰 ② Weekly PDF 검수 ③ Pro 구독자 전용 발송 | ~30분 |

**월간 추가 업무**:
- Operations Playbook 리뷰 (1회, 30분)
- 구독자 데이터 분석 — 언어별 유입, 성장률 (1회, 20분)
- 시나리오 Checkpoint 검증 (해당 월에 기한이 있는 경우)

---

## 6. 즉시 실행 필요 사항 체크리스트

```
□ beehiiv Premium Subscription 활성화 (Settings → Monetization)
□ Stripe 계정 연동
□ Pro 플랜 상품 생성 ($150/년)
□ Weekly Synthesis를 Pro-only 콘텐츠로 태그 설정
□ 웹사이트 Pricing "Join Pro" 버튼 URL → beehiiv 유료 구독 URL로 교체
□ 웹서버/호스팅 결정 (Netlify / Vercel / GitHub Pages / 기존 호스팅)
□ 도메인 연결 확인 (aipoweratlas.com)
□ 첫 Pro-only Weekly Synthesis 테스트 발행
```

---

*Last updated: 2026-03-21 | AI Power Atlas Internal Reference*
