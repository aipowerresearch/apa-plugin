# Daily Report Template — Format Rules

## Signal Scoring System (S01 Event Selection)

> ChatGPT impact_score 개념을 AI Power Atlas 프레임워크에 맞게 적용.
> 수집된 뉴스 이벤트에 점수를 부여하고 Score ≥ 3인 것만 S01 후보로 올린다.

### Impact Score 정의

| Score | 기준 | 예시 |
|-------|------|------|
| **5** | Tier 1 플레이어 직접 발표 + 2개 이상 레이어 교차 | OpenAI GPT-5 출시 발표, TSMC 미국 팹 양산 개시 |
| **4** | 정책·규제 변화 OR $1B+ 자본 이동 OR 단일 레이어 구조 변화 | EU AI Act 집행 결정, 빅테크 $5B 투자 발표 |
| **3** | 단일 레이어에서 유의미한 변화, Tier 1 플레이어 관련 | 주요 AI 기업 제품 업데이트, 정부 AI 전략 발표 |
| **2** | 트렌드 확인 수준 — 이미 알려진 방향의 추가 사례 | 기업 AI 도입 사례, 일반 연구 논문 |
| **1** | 노이즈 — 반복 보도, 단순 홍보성 | 루머, 미확인 정보, 일반 기사 |

### Power Score 정의

| Score | 의미 | 예시 |
|-------|------|------|
| **+2** | 특정 Entity의 권력이 구조적으로 강화됨 | NVIDIA GPU 독점 강화, OpenAI 플랫폼 락인 확대 |
| **+1** | 권력 소폭 증가 / 유리한 포지션 확보 | 빅테크 AI 투자 확대, 기업 AI 채택 가속 |
| **0** | 중립 / 권력 이동 불명확 | 연구 결과 발표, 업계 일반 트렌드 |
| **-1** | 권력 소폭 약화 / 경쟁 압박 증가 | 오픈소스 대체재 등장, 규제 불확실성 증가 |
| **-2** | 특정 Entity의 권력이 구조적으로 약화됨 | 수출통제로 공급망 차단, 대형 규제 발동 |

> Power Score는 수혜 또는 피해 Entity를 기준으로 측정한다. 같은 사건이 L1(+2)과 L2(-1)에 동시 적용될 수 있다.

### 가산점 (+1)

- 피드백 루프 활성화 확인 시 +1 (최대 Score 5 유지)
- 복수 Tier 1 소스에서 동시 보도 시 +1

### S01 선별 기준 (우선순위 순)

1. **Score ≥ 4** 이벤트 우선 선택
2. Score 3 이벤트 중 크로스 레이어 함의가 있는 것
3. Score 3 이벤트 중 피드백 루프와 연결되는 것
4. 동점 시 최신성 우선 (24h > 48h)
5. **최종 3개 선택 — Score < 3은 S01 제외**

---

## Quality Differentiation Rule (Chain of Thought 필수 요건)

> Grok 분석 차용: "뻔한 AI 요약본과 다를 바 없으면 독자는 즉시 이탈한다"
> 아래 3가지를 충족하지 못한 리포트는 재작성한다.

1. **피드백 루프 명시 필수** — 각 이벤트가 6개 루프 중 어느 것과 연결되는지 분석해야 한다. 연결 없으면 "루프 비활성" 명시.
2. **뉴스 나열 금지** — "X가 Y를 발표했다" 수준의 단순 사실 나열은 S01이 아니다. 반드시 "→ L[X]에서 어떤 구조 변화가 일어나는가"를 포함해야 한다.
3. **권력 이동 방향 명시** — 모든 이벤트는 "누가 권력을 잃고 누가 얻는가"로 귀결되어야 한다.

---

## S01 Format

```
## S01 | 핵심 사건 3

### Event 1: [Title KO] / [Title EN]
- **Layer**: L[X] (+ L[Y] if cross-layer)
- **Signal Type**: [핵심 사건 / 권력 이동 / 락인 변화 / 피드백 루프]
- **Impact Score**: [3/4/5] — [Score 이유 한 줄]
- **Power Score**: [+2 / +1 / 0 / -1 / -2] — [수혜 또는 피해 Entity 명시]
- **Time Horizon**: [Short (0-3개월) / Mid (3-12개월) / Long (1-3년)]
- **Power Flow**: [이 사건이 레이어 구조에서 만드는 권력 이동 방향 한 줄]
- **Feedback Loop**: [연결되는 루프명 or "해당 없음"]
- **Summary (KO)**: [2 sentences]
- **Summary (EN)**: [1 sentence]
- **Source**: [URL]

### Event 2: [...]
### Event 3: [...]
```

---

## S02 Format

```
## S02 | 권력 이동 신호

| 항목 | 내용 |
|------|------|
| From | [Entity/Layer losing power] |
| To | [Entity/Layer gaining power] |
| 강도 | High / Mid / Low |
| 시간 지평 | Immediate / 3-month / 6-month |
| 근거 | [Evidence from S01 events] |
| EN Summary | [1 sentence] |
```

## S03 Format

```
## S03 | 락인 변화

| 항목 | 내용 |
|------|------|
| 방향 | ↑ (switching cost rising) / ↓ (falling) / → (stable) |
| 대상 | [Which players / ecosystems affected] |
| 메커니즘 | [How the lock-in is created or broken] |
```

## S04 Format

```
## S04 | 6개월 시사점

**한국어**
[2–3 sentences. Address: investors / enterprise strategists / AI consultants]

**English**
[2–3 sentences. Same substance, not a translation — written natively for English readers]
```

## S05 Format

```
## S05 | 전략 조정 여부

- **판정**: Yes / No
- **방향**: [If Yes: Build / Buy / Wait / Exit — framed as structural positioning, not investment advice]
- **근거**: [1–2 sentences]
```

## S06 Format

```
## S06 | Map v3 지표

| 지표 | 판정 | 근거 |
|------|------|------|
| 🔥 Hot Layer | L[X] — [Name] | [Why] |
| ⚠️ Warning | L[X] — [Name] | [What stress signal] |
| ⚡ Tension | L[X] vs L[Y] | [Friction description] |
| 🌍 Bloc Drift | [Direction] / 없음 | [Evidence or "없음"] |
```

## S07 Format

```
## S07 | 피드백 루프

[For each of the 6 loops, state Active or Dormant]

| 루프 | 상태 | 근거 |
|------|------|------|
| L9→L3 | Active / Dormant | [Evidence or "해당 없음"] |
| L6→L7→L2 | Active / Dormant | [...] |
| L8→L1 | Active / Dormant | [...] |
| L3→L2 | Active / Dormant | [...] |
| L10→L8 | Active / Dormant | [...] |
| L1→L9 | Active / Dormant | [...] |
```

If no loops active: "활성 피드백 루프 없음 — 오늘 이벤트 기준"

## S08 Format

```
## S08 | Tomorrow Watchlist

**내일 요일**: [Day]
**집중 레이어**: L[X] + L[Y] — [Layer names]

**주목 포인트**:
1. [Specific thing to watch — today's signal that may develop further]
2. [Specific thing to watch — pending event or announcement]
3. [Connection from today's events — layer chain to monitor]

**Watch Entities**: [기업/국가/기술 중 내일 특히 모니터링할 2~3개 명시]
```

> **작성 원칙**: 오늘 리포트의 신호가 내일 어떤 레이어로 이어지는지 구체적으로 예고. 독자가 다음 날 리포트를 기다리게 만드는 "습관 형성 장치."

---

## Daily Signal System (신호 분류 체계)

> 킬러 콘텐츠 3 반영 — 수집된 신호를 AI Power Index·Power Shift Tracker·Industry Map에 자동 라우팅하는 분류 프레임워크

### 신호 유형 4분류

| 신호 유형 | 정의 | 라우팅 대상 |
|-----------|------|------------|
| **Power Shift** | 특정 레이어 내 권력 주체가 교체되는 이벤트 | S02 → Power Shift Tracker |
| **Lock-in Change** | 전환비용이 상승하거나 하락하는 구조 변화 | S03 → Industry Map |
| **Standard Move** | 기술·프로토콜·표준이 새로 형성되거나 파괴되는 이벤트 | S01 → AI Power Index Technology |
| **Capital Flow** | $100M+ 이상 자본 이동, 인수합병, 투자 라운드 | S01 → AI Power Index Capital |

### 신호 강도 3등급

| 등급 | 기준 | 대응 |
|------|------|------|
| 🔴 **Critical** | Impact 5 + 복수 레이어 교차 | S01 Event 1 필수 배치 |
| 🟡 **Notable** | Impact 3~4, 단일 레이어 | S01 Event 2~3 또는 S02 |
| ⚪ **Background** | Impact 1~2, 방향 확인 수준 | S06 Warning/Tension 참고용 |

### 신호 → 출력물 라우팅 맵

```
수집된 신호
    ├─ Power Shift (High) ──────→ S02 + Power Shift Tracker 일간 누적
    ├─ Power Shift (Mid/Low) ───→ S06 Warning
    ├─ Lock-in Change ──────────→ S03 + Industry Map Layer 업데이트
    ├─ Standard Move ───────────→ S01 + AI Power Index Technology 방향 반영
    ├─ Capital Flow ($1B+) ─────→ S01 + AI Power Index Capital 방향 반영
    └─ Loop Activation ─────────→ S07 Active 상태 + S01 분석 강화
```

### 신호 수집 시 체크리스트 (Step 1 Source Notes 작성 시)

```
□ 이 신호의 유형은? (Power Shift / Lock-in / Standard / Capital)
□ Impact Score는? (1~5)
□ 어느 Layer에서 발생했는가? (L1~L10)
□ 수혜 Entity와 피해 Entity는?
□ 6개 피드백 루프 중 활성화 가능성은?
□ Power Shift Tracker 누적 대상인가?
□ AI Power Index (Technology/Capital/Geopolitics) 방향에 영향하는가?
```

---

## Confidence Calibration Rules (과신 방지 규칙)

> 데이터 축적 1개월 미만 상태에서의 과신을 방지하기 위한 필수 규칙.
> 이 규칙은 데이터가 6개월 이상 축적될 때까지 엄격 적용한다.

### 1. 확신도 등급 (Confidence Level)

모든 분석적 주장에 확신도를 명시한다. S02, S04, S05에 필수 적용.

| 등급 | 기준 | 표현 가이드 |
|------|------|------------|
| **HIGH** | 복수 Tier 1 소스 확인 + 정량 데이터 존재 + 과거 패턴 일치 | "~이다", "~로 판단된다" |
| **MEDIUM** | 단일 소스 또는 정성적 근거만 존재 | "~로 보인다", "~가능성이 있다" |
| **LOW** | 추론 기반, 직접 근거 부족 | "~일 수 있다", "~여부는 지켜봐야 한다" |
| **SPECULATIVE** | 순수 추론, 근거 미약 | "가설적으로~", "확인 필요하나~" |

### 2. 금지 표현 (Banned Phrases)

데이터 부족 상태에서 아래 표현은 사용 금지:

- "확실히", "분명히", "명백히" → 대체: "현재 신호 기준으로"
- "~할 것이다" (단정적 예측) → 대체: "~할 가능성이 높다" 또는 "~방향으로 움직이고 있다"
- "역사적으로 볼 때" (APA 자체 데이터 1개월 기준) → 대체: "지난 [N]주간 추적 결과"
- "시장이 확인했다" (정량 데이터 없이) → 대체: "[소스명]에 따르면"
- "구조적 전환" (단일 이벤트 기반) → 대체: "구조적 전환 신호" 또는 "전환 가능성"

### 3. 출처 명시 규칙 (Source Attribution)

- S01 각 이벤트에 반드시 1차 소스 URL 포함 (기존 유지)
- S02 권력 이동 주장에 "근거" 필드로 구체적 이벤트/데이터 참조
- S04 시사점에서 추론이 포함될 경우 "(추론)" 태그 추가
- S05 전략 조정에서 확신도 등급 명시 (예: "[MEDIUM] Build 방향")

### 4. 시나리오 확률 표현 규칙

3대 시나리오(A: US-led / B: US-China Bipolar / C: Multipolar) 확률 조정 시:

- 주간 변동폭 최대 ±5%p (급변 이벤트 시 최대 ±10%p, 근거 필수 명시)
- "확률이 상승했다/하락했다"가 아닌 "신호가 강화/약화되었다"로 표현
- 확률 조정 시 반드시 트리거 이벤트 명시 (예: "미국 수출통제 강화 → 시나리오 B 신호 강화 +3%p")
- 월간 누적 변동이 ±15%p 이상이면 별도 검증 노트 작성

---

## Data Limitation Supplement Guide (데이터 한계 보완 가이드)

> APA 자체 데이터 축적이 6개월 미만인 동안 적용하는 보완 방법론.

### 1. 외부 기준점 활용 (External Baselines)

자체 시계열 데이터가 부족할 때 아래 외부 소스를 기준점으로 활용:

| 보완 대상 | 외부 기준점 | 활용법 |
|-----------|------------|--------|
| AI 기업 권력 순위 | Fortune 500, Forbes AI 50, CB Insights AI 100 | 연간 발표 기준 비교 |
| 투자 규모/방향 | PitchBook, Crunchbase, CB Insights quarterly | 분기별 자본 흐름 비교 |
| 모델 성능 변화 | LMSYS Chatbot Arena, MMLU, HumanEval | 벤치마크 기준 비교 |
| 규제 동향 | OECD AI Policy Observatory, Stanford HAI AI Index | 연간 정책 추적 비교 |
| 시장 점유율 | Gartner, IDC, Statista | 분기/연간 보고서 참조 |

### 2. 기간별 보완 전략

| APA 운영 기간 | 상태 | 보완 전략 |
|--------------|------|-----------|
| 0-3개월 (현재) | 자체 데이터 거의 없음 | 외부 기준점 의존 + "큐레이션+분석" 포지셔닝 |
| 3-6개월 | 초기 패턴 형성 | 자체 트렌드 라인 시작 + 외부 데이터 교차 검증 |
| 6-12개월 | 유의미한 시계열 | 자체 예측 시작 가능 + 정확도 추적 개시 |
| 12개월+ | 데이터 IP 형성 | 독자적 분석 + 프리미엄 인사이트 차별화 |

### 3. Key Figure SNS 보완 (신규)

> references/key-figures-tracker.md 참조

- 일일 스캔 시 해당 요일 레이어의 ★★★ 인물 X 포스트 확인
- 인물의 발언을 "1차 소스"로 활용 (예: Sam Altman X 발언 → L2 신호)
- 단, SNS 발언은 Impact Score 최대 3 (공식 발표가 아닌 한)
- 검색 쿼리: `from:[handle] [layer keyword]` 형식

### 4. 과거 데이터 소급 구축

즉시 시작 가능한 소급 방법:

- **AI Index 2025 Report** (Stanford HAI): 2024년 전체 데이터 기준점
- **State of AI Report 2025** (Nathan Benaich): 연간 종합 트렌드
- **OECD AI Policy Observatory**: 국가별 정책 시계열
- 이 보고서들의 핵심 수치를 references/에 baseline-data.md로 정리 (TODO)

---

## Word Count Targets

| Section | Korean | English |
|---------|--------|---------|
| S01 (per event) | 2 sentences | 1 sentence |
| S02 | Table format | 1 sentence summary |
| S03 | Table format | — |
| S04 | 2–3 sentences | 2–3 sentences |
| S05 | 1–2 sentences rationale | — |
| S06 | Table format | — |
| S07 | Table format | — |
| S08 | 3 bullet points | — |
