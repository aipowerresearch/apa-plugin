# AI Industry Map v3 — 10-Layer Power Flow Framework

> **[v3.1 — 2026-03-09 업데이트]** Energy Layer 세부 설명 추가. AI Industry Map v3 HTML 인터랙티브 문서 보유 시 상세 내용 추가 보완 가능.

## 핵심 명제

> 연산(에너지·칩)을 장악한 자가 모델을 지배하고, 모델을 장악한 자가 플랫폼을 장악하며, 플랫폼을 장악한 자가 산업을 재편한다. 자본은 이를 가속하고, 지정학·규제는 이를 분절하며, 안전·리스크는 최종 한계를 그린다.

## 10-Layer Architecture

Power flows from L1 → L10. Each layer constrains and enables the layers above it.

| Layer | Name | Core Keywords | Power Direction |
|-------|------|---------------|----------------|
| L1 | Compute Infrastructure (연산 인프라) | GPU, chip, datacenter power, energy grid, nuclear/renewable, sovereign computing | Foundation — controls all above |
| L2 | Foundation Models (파운데이션 모델) | Closed vs Open, reasoning, multimodal | Determined by L1 |
| L3 | Middleware & Data (미들웨어 & 데이터) | Hidden lock-in, agent orchestration | Hidden power layer |
| L4 | Platform & Interface (플랫폼 & 인터페이스) | Agentic OS, edge AI, UX | Distribution layer |
| L5 | AI Native Apps (AI 네이티브 앱) | Consumer vs Enterprise ARR | Revenue layer |
| L6 | Vertical Penetration (산업 침투) | Physical AI, robotics, ROI | Real-world impact |
| L7 | Capital & Market (자본 & 시장) | IPO, VC, macro indicators | Acceleration layer |
| L8 | Regulation & Geopolitics (규제 & 지정학) | Export controls, bloc formation | Fragmentation layer |
| L9 | Safety & Risk (안전성 & 리스크) | Alignment, environment, deepfake | Constraint layer |
| L10 | Macro Impact (거시 영향) | Labor, inequality, education, culture | Terminal effect |

## 6 Cross-Layer Feedback Loops

These loops create non-linear dynamics. Track which are active in each report.

| Loop | Direction | Mechanism |
|------|-----------|-----------|
| Loop 1 | L9 → L3 | Security incidents force middleware architecture redesign |
| Loop 2 | L6 → L7 → L2 | ROI failure → capital withdrawal → model cost-reduction pressure |
| Loop 3 | L8 → L1 | Export controls → sovereign computing acceleration |
| Loop 4 | L3 → L2 | Pipeline lock-in → model choice reversal |
| Loop 5 | L10 → L8 | Inequality backlash → regulatory legislation acceleration |
| Loop 6 | L1 → L9 | Energy crisis → large model training constraints |

## Layer Interaction Matrix

Key relationships between layers:

- **L1 constrains L2**: Compute availability determines which models can be trained
- **L2 shapes L3**: Model capabilities determine middleware requirements
- **L3 creates L4 lock-in**: Middleware dependencies constrain platform switching
- **L4 determines L5 distribution**: Platform controls access to end-user apps
- **L5 proves L6 ROI**: App-layer success validates vertical deployment
- **L6 feeds L7**: ROI evidence attracts capital
- **L7 accelerates L1**: Capital flows back to compute infrastructure
- **L8 fragments L1**: Geopolitics creates sovereign compute silos
- **L9 constrains all**: Safety requirements limit deployment across all layers

## L1 Energy Sub-Layer Detail

L1은 GPU/칩 레이어와 **에너지 인프라 레이어**를 통합한다. 에너지는 AI 컴퓨팅의 물리적 상한선이다.

| Sub-Layer | Core Elements | Key Players | Signal Question |
|-----------|---------------|-------------|-----------------|
| L1-Compute | GPU, AI ASIC, 서버 | NVIDIA, AMD, TSMC | AI 컴퓨팅 파워는 어디에 집중되는가? |
| L1-Energy | 데이터센터 전력, 원자력, 재생에너지, 전력망 | NextEra Energy, Constellation Energy | AI가 전력 인프라를 얼마나 압박하는가? |

**통합 이유**: 에너지는 컴퓨팅과 분리된 독립 산업이 아니다. AI 데이터센터 전력 수요는 L1-Compute 투자 결정에 직접 종속된다. 에너지 신호는 L1 레이어 내에서 추적한다.

**Loop 6 연결**: L1-Energy 위기(전력 부족·가격 급등) → 대형 모델 학습 제약 → L2 Foundation Model 훈련 지연.

## Entity Type Framework

AI 산업 권력 구조는 6개 Entity Type과 그 관계(Relationship)로 구성된다. 리포트 작성 시 S01~S03에서 어떤 엔티티가 어떤 관계 변화를 보이는지 명시한다.

### 6 Entity Types

| Entity Type | 설명 | 속성 예시 |
|-------------|------|-----------|
| **Company** | AI 기업 (빅테크·스타트업·공급망) | industry, layer, market_cap, AI_focus |
| **Model** | AI 모델 | model_type, training_compute, release_date, developer |
| **Technology** | AI 기술·컴포넌트 | category, layer, maturity |
| **Capital** | 투자·자금 흐름 | amount, investor, target, date |
| **Country** | 국가·지역 블록 | AI_talent, AI_investment, AI_policy, bloc |
| **Policy** | 규제·정책·표준 | country, impact_level, affected_layers, date |

### Core Relationship Types

| Relationship | 주체 | 대상 | 신호 의미 |
|-------------|------|------|-----------|
| **develops** | Company | Model / Technology | 기술 권력 생성 |
| **supplies** | Company | Company / Technology | 공급망 종속 |
| **invests** | Company / Country / Capital | Company / Country | 자본 권력 이동 |
| **regulates** | Country / Policy | Company / Technology | 권력 제약 |
| **acquires** | Company | Company / Technology | 락인 변화 |
| **competes** | Company | Company | 권력 분산·집중 |

### 실전 예시

```
Microsoft → invests → OpenAI          (L7 Capital 신호)
NVIDIA → supplies → GPU               (L1 Compute 지배력)
EU → regulates → Foundation Models   (L8 Geopolitics 제약)
OpenAI → develops → GPT models       (L2 권력 강화)
Anthropic → competes → OpenAI        (L2 분산 신호)
```

**사용법**: S01 핵심 사건 서술 시 "어떤 Entity가 어떤 Relationship으로 변화했는가"를 명시하면 S02 권력 이동 신호가 자동으로 도출된다.

## Signal Type Definitions

Use these consistently across all reports:

- **핵심 사건 (Key Event)**: A significant discrete event that changes the state of a layer
- **권력 이동 (Power Shift)**: A change in which entity controls a layer or sub-layer
- **락인 변화 (Lock-in Change)**: A shift in switching costs — who can or can't exit a dependency
- **피드백 루프 (Feedback Loop)**: Cross-layer interaction that amplifies or dampens change

## Map v3 Indicator Definitions

For S06 of every report:

- **Hot Layer**: The layer with most significant activity in today's news (highest signal density)
- **Warning**: A layer showing stress, fragility, or early-stage disruption
- **Tension**: The primary friction point between two layers or between players within a layer
- **Bloc Drift**: Movement of countries, companies, or ecosystems toward distinct AI blocs (US/EU vs China vs Emerging)
