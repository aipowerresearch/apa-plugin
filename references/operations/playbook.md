# APA Operations Playbook v1.1
*Created: 2026-03-20 | Updated: 2026-03-21 | Maintainer: AI Power Research*

---

## 1. Mission Statement

> APA는 독특하면서도 정확한 방향을 제시하며, 다른 어느 소스에서도 얻을 수 없는 경험과 지식을 제공한다.
> 뉴스 큐레이션이 아니라 **구조적 권력 이동의 해석과 검증 가능한 예측**이 핵심 가치다.

---

## 2. Daily Operations

### 2.1 자동 실행 스케줄

> **기준 시간: EST (미국 동부 표준시)**. 미국 구독자 오전 6:00 AM EST 뉴스레터 수령 목표.
> 상세 타임라인: `references/publishing-schedule.md` 참조

| 요일 | KST | EST | EDT | 레이어 | 작업 |
|------|-----|-----|-----|--------|------|
| 월~토 | **17:00** | 3:00 AM | 4:00 AM | 해당일 레이어 | full-daily |
| 월 | 17:00 | 3:00 AM | 4:00 AM | L1+L2 | full-daily |
| 화 | 17:00 | 3:00 AM | 4:00 AM | L3+L4 | full-daily |
| 수 | 17:00 | 3:00 AM | 4:00 AM | L5+L6 | full-daily |
| 목 | 17:00 | 3:00 AM | 4:00 AM | L7+L8 | full-daily |
| 금 | 17:00 | 3:00 AM | 4:00 AM | L9+L10 | full-daily |
| 토 | 17:00 | 3:00 AM | 4:00 AM | 보완 스캔 | full-daily |
| 토 (주간) | **22:00** | 8:00 AM | 9:00 AM | — | weekly-synthesis |

**뉴스레터 발송**: 6:00 AM EST (= 11:00 AM UTC = 8:00 PM KST) — beehiiv 예약
**웹사이트 업로드 마감**: 5:30 AM EST (파이프라인 완료 후 30분 내)

### 2.2 자동 실행 조건
- 컴퓨터 전원 ON (전원 연결 시 자동 오프 비활성화 설정됨)
- Cowork 앱 실행 중
- 인터넷 연결 활성

### 2.3 일일 파이프라인 (5단계)

```
scan → generate → format-newsletter → format-blog → archive
 │         │              │                │            │
 ▼         ▼              ▼                ▼            ▼
sources/  reports/    newsletters/      blog/     archive-index.md
```

### 2.4 출력 파일 명명 규칙

| 유형 | 패턴 | 예시 |
|------|------|------|
| 소스 노트 | `YYYY-MM-DD_L{N}_source-notes.md` | `2026-03-20_L7L8_source-notes.md` |
| 리포트 | `YYYY-MM-DD_요일_L{N}_daily-report_v1.md` | `2026-03-20_금_L7L8_daily-report_v1.md` |
| 뉴스레터 KO | `YYYY-MM-DD_요일_newsletter_ko.html` | `2026-03-20_금_newsletter_ko.html` |
| 뉴스레터 EN | `YYYY-MM-DD_요일_newsletter_en.html` | `2026-03-20_금_newsletter_en.html` |
| 블로그 KO | `YYYY-MM-DD_요일_blog_ko.md` | `2026-03-20_금_blog_ko.md` |
| 블로그 EN | `YYYY-MM-DD_요일_blog_en.md` | `2026-03-20_금_blog_en.md` |
| 주간 종합 | `YYYY-W{NN}_weekly-synthesis.md` | `2026-W12_weekly-synthesis.md` |
| 주간 뉴스레터 | `YYYY-W{NN}_weekly-newsletter_{lang}.html` | `2026-W12_weekly-newsletter_ko.html` |

---

## 3. Quality Gates

### 3.1 소스 수집 기준
- T1 (Tier 1): 5개 이상 — Reuters, Bloomberg, FT 등 1차 보도
- T2 (Tier 2): 5개 이상 — 전문 매체, 기업 공식 발표
- T3 (Tier 3): 3개 이상 — 분석, 오피니언, 리서치
- **최소 합계: 15개 소스**

### 3.2 리포트 8섹션 필수 체크
- [ ] S01: 핵심 사건 3건 (각각 권력 이동 방향 명시)
- [ ] S02: 권력 이동 신호 (From→To, 강도)
- [ ] S03: 피드백 루프 (활성 루프 + Hot Loop 지정)
- [ ] S04: 시나리오 업데이트 (확률 변동 + 근거)
- [ ] S05: 크로스 레이어 인사이트
- [ ] S06: 신호 강도 지표 4칸
- [ ] S07: 반대 의견 (Contrarian View)
- [ ] S08: 내일 주목 신호

### 3.3 뉴스레터 v2 필수 체크
- [ ] S01 이벤트별 원문 링크 포함
- [ ] S05 크로스 레이어 섹션 포함
- [ ] S07 반대 의견 섹션 포함
- [ ] 600px 테이블 레이아웃, 인라인 CSS only

---

## 4. Scenario Verification Protocol

### 4.1 Checkpoint 설정 규칙
- 시나리오 생성 시 반드시 2개 이상의 Checkpoint 설정
- 각 Checkpoint에는 명확한 검증 기준(Criteria)과 검증 시한(Verify By) 명시
- 검증 기준은 이진(Yes/No) 판정이 가능해야 함

### 4.2 검증 실행
- 검증 시한 도래 시 해당 주간 리포트에서 판정 수행
- 결과: HIT / PARTIAL / MISS
- 판정 근거를 Evidence 컬럼에 기록

### 4.3 적중률 공개
- 월간 1회 Cumulative Score 업데이트
- 분기별 1회 적중률 분석 리포트 발행 (블로그 + 뉴스레터 특별호)

---

## 5. Feedback Loop System

### 5.1 정의된 루프

| Loop | 연결 | 의미 |
|------|------|------|
| Loop 1 | L1→L2 | 인프라 투자가 모델 개발 방향 결정 |
| Loop 2 | L6→L7→L2 | 산업 적용이 자본 흐름과 모델 수요에 영향 |
| Loop 3 | L8→L1 | 규제가 인프라 투자 구조를 변경 |
| Loop 4 | L3→L2 | 미들웨어 표준이 모델 선택을 결정 |
| Loop 5 | L10→L8 | 사회적 압력이 규제 강화로 전환 |

### 5.2 Hot Loop 판정 기준
- 해당 주에 2개 이상 레이어에서 동시 신호 감지
- 24시간 내 연쇄 반응 발생 가능성
- 시나리오 확률에 직접 영향

---

## 6. Archive & Data Accumulation

### 6.1 아카이브 구조

```
APA/
├── outputs/
│   ├── sources/          ← 일일 소스 노트
│   ├── reports/          ← 8섹션 일일 리포트
│   ├── newsletters/      ← 한영 뉴스레터 HTML
│   ├── blog/             ← 한영 블로그 마크다운
│   ├── archive-index.md  ← 주차별 완성도 추적
│   └── scenario-tracker.md ← 시나리오 확률 + 검증
└── references/           ← 프레임워크, 템플릿, 용어집
```

### 6.2 데이터 축적 가치
- 시간이 지날수록 시계열 분석 가능
- 예측 트랙레코드 = 복제 불가능한 자산
- 과거 패턴 기반 미래 시나리오 정교화

---

## 7. Evolution Roadmap

### Phase 1: Foundation (현재 ~ W16)
- [x] 10레이어 프레임워크 확립
- [x] 일일 자동 파이프라인 구축
- [x] 시나리오 트래커 + 검증 프레임워크
- [x] 뉴스레터 v2 (S05/S07/링크 추가)
- [ ] 4주간 무중단 아카이브 축적

### Phase 2: Credibility (W17 ~ W28)
- [ ] 첫 번째 Checkpoint 검증 (A-1, B-1: 2026-06-30)
- [ ] 적중률 첫 공개 발표
- [ ] AI Power Index 독자 지수 설계 및 일일 산출 시작
- [ ] 구독자 100명 달성

### Phase 3: Moat (W29 ~ W52)
- [ ] 두 번째 Checkpoint 검증 (A-2, B-2, C-1: 2026-09-30)
- [ ] 인터랙티브 대시보드 (레이어 시계열, 시나리오 추이 차트)
- [ ] 커뮤니티 시그널 도입 (구독자 투표/코멘트)
- [ ] 유료 구독 전환 (심층 분석 리포트)

### Phase 4: Scale (2027~)
- [ ] 분기별 적중률 리포트 정례화
- [ ] API/데이터 피드 (기관 고객)
- [ ] 다국어 확장 (아래 §9 국제 확장 전략 참조)
- [ ] 연간 전망 리포트 발행

---

## 9. International Expansion Strategy

> 상세: `references/international-expansion-roadmap.md` 참조

### 9.1 확장 원칙
- **EN+KO로 상위 20개국 중 10개국(점수 73.9%) 이미 커버** — 추가 언어는 ROI 기반 순차 투입
- 각 언어 추가는 GO/NO-GO 매트릭스로 판단 (유입 5%+, 기존 성장률 양수, 운영 여력 확보)
- 빈 페이지 언어 버튼 금지 — Phase 실행 시점에만 활성화

### 9.2 언어 서비스 Tier 구조

| Tier | 언어 | 시기 | 커버 국가 | 누적 커버율 |
|------|------|------|-----------|------------|
| 1차 (현재) | EN+KO | ~W28 | 미국,인도,한국,영국,싱가포르,UAE,캐나다,이스라엘,아일랜드,핀란드 | 73.9% |
| 2차 | +JA,+ES,+DE | W29~2027 Q1 | +일본,스페인,독일,스위스,룩셈부르크 | 99.0% |
| 3차 (조건부) | +FR,+PT,+AR | 2027 Q2~H2 | +프랑스,브라질,포르투갈,사우디 | 100%+ |
| 4차 (미정) | ZH-TW,ZH-CN | 데이터 기반 | 대만·홍콩·화교권 / 중국 본토 | 별도 |

### 9.3 중국 정책: 분석 대상 ≠ 서비스 대상
- **분석 대상**: 중국은 모든 리포트에 포함 (미중 AI 경쟁은 APA 분석의 핵심 축)
- **서비스 제외**: 중국어 번역·제공만 제외 (난이도 5, 검열 리스크, 콘텐츠 민감도)
- **4차 재검토**: ZH-TW(번체)부터, 화교권 유입 5%+ 시 검토 (최소 2028년 이후)

---

## 8. Competitive Defense Matrix

| 경쟁자 행동 | 우리의 방어 | 해자 유형 |
|------------|-----------|----------|
| 10레이어 구조 복제 | 축적된 시계열 데이터 + 검증 트랙레코드 | 시간 해자 |
| 뉴스레터 포맷 모방 | S05 크로스 레이어 분석의 질적 깊이 | 역량 해자 |
| AI 자동 뉴스 큐레이션 | 검증 가능한 시나리오 예측 (HIT/MISS 공개) | 신뢰 해자 |
| 저가 구독 경쟁 | 독자 지수(AI Power Index) 레퍼런스화 | 브랜드 해자 |
| 대형 미디어 진출 | 커뮤니티 네트워크 효과 + 전문가 기고 | 네트워크 해자 |

---

*이 문서는 APA 운영의 단일 진실 소스(Single Source of Truth)이며, 매월 1회 리뷰·업데이트한다.*
