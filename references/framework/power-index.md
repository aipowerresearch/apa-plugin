# AI Power Index — Framework Reference

> **v1.0 — 2026-03-09**
> AI Power Atlas의 킬러 기능. AI 산업 권력 구조를 수치화·시각화하는 지표 시스템.
> Phase 1: 정성적 신호 기반 (현재 운영 가능) / Phase 2: 데이터 파이프라인 연동 (추후)

---

## 핵심 개념

> AI Power Index = AI 산업의 기술·자본·지정학 권력이 **어디로 이동하는지** 추적하는 벤치마크

S&P 500이 미국 주식시장 권력을 수치화하듯, AI Power Index는 AI 산업 권력 구조를 수치화한다.

---

## 3 Mega Index 구조

```
AI Power Index
= 0.5 × Technology Power Index
+ 0.3 × Capital Power Index
+ 0.2 × Geopolitical Power Index
```

가중치 근거: 기술이 AI 산업 가치 창출의 핵심 동인. 자본은 가속자. 지정학은 분절자.

---

### Index 1 — AI Technology Power Index

AI 산업의 실질 기술 우위

| 구성 요소 | 가중치 | Phase 1 측정 방식 | Phase 2 데이터 소스 |
|-----------|--------|-------------------|---------------------|
| Compute Power | 30% | L1 레이어 신호 강도 (정성) | GPU 출하량, 데이터센터 투자 |
| Model Capability | 30% | SOTA 모델 변화 추적 (정성) | 벤치마크 스코어 (MMLU, HumanEval) |
| AI Infrastructure | 20% | L3/L4 레이어 락인 변화 | AI 플랫폼 사용량, API 호출 수 |
| Data Advantage | 20% | 데이터 접근권 변화 추적 | 학습 데이터 규모, 합성 데이터 비중 |

---

### Index 2 — AI Capital Power Index

자본의 방향이 다음 기술 사이클을 결정한다

| 구성 요소 | 가중치 | Phase 1 측정 방식 | Phase 2 데이터 소스 |
|-----------|--------|-------------------|---------------------|
| VC Funding | 40% | 주요 딜 추적 (정성) | Crunchbase, PitchBook |
| Big Tech Investment | 30% | L7 레이어 신호 (정성) | 10-K 자본지출 항목 |
| AI Startup Growth | 20% | 신규 유니콘 추적 | CB Insights |
| M&A | 10% | 주요 인수 추적 | Bloomberg, Refinitiv |

---

### Index 3 — AI Geopolitical Power Index

기술 패권 경쟁의 국가별 포지션

| 구성 요소 | 가중치 | Phase 1 측정 방식 | Phase 2 데이터 소스 |
|-----------|--------|-------------------|---------------------|
| AI Policy | 30% | L8 레이어 규제 신호 | OECD AI Policy Observatory |
| Research Output | 30% | 논문·특허 추적 (정성) | arXiv, USPTO, WIPO |
| AI Talent | 20% | 연구자 이동 추적 | Stanford HAI AI Index |
| AI Infrastructure | 20% | 국가 AI 투자 추적 | 정부 발표, IMF/WEF |

---

## Phase 1 운영 방식 (현재 즉시 가능)

**정량 데이터 없이도 운영 가능한 방식**: 각 Index 항목에 대해 주간 신호 방향(↑ / → / ↓)과 강도(1~5)를 리포터가 판단.

```
Weekly Power Index Update (S06 연계)
────────────────────────────────────
Technology Index:  ↑ (+2)  Compute 공급 긴장 완화
Capital Index:     ↑ (+1)  AI 인프라 딜 증가
Geopolitical Index: ↓ (-1)  EU 규제 강화

AI Power Index (종합): ↑ 방향
권력 이동: US Big Tech 집중 유지
```

---

## AI Company Power Watch — Top 7 주간 추적

> Phase 1 운영 방식: 방향 신호(↑ / → / ↓) + 한 줄 근거. 구체적 수치 공개는 Phase 2 이후.

| 기업 | Primary Layer | 이번 주 Power Direction | 근거 |
|------|--------------|------------------------|------|
| NVIDIA | L1 | | |
| OpenAI | L2 | | |
| Google DeepMind | L2 + L4 | | |
| Microsoft | L4 + L7 | | |
| Meta AI | L2 + L5 | | |
| Amazon (AWS) | L1 + L4 | | |
| Alibaba / DeepSeek | L2 + L8 | | |

**업데이트 주기**: 매주 일요일 `/ai-power-atlas:weekly` 실행 시 W03 섹션에서 함께 업데이트.

**해석 기준**:
- ↑ : 이번 주 해당 기업의 레이어 내 지배력/포지션 강화 (Power Score +1 이상 이벤트 존재)
- → : 변화 없음 / 유지
- ↓ : 지배력/포지션 약화 (Power Score -1 이하 이벤트 존재)

---

## 리포트 활용 위치

| 섹션 | 활용 방식 |
|------|-----------|
| S06 (Map v3 Snapshot) | Hot Layer + Power Index 방향 신호 병기 |
| Weekly Report | AI Power Index Weekly Update 독립 섹션 |
| Monthly Report | Index 추세선 및 국가/기업 순위 변화 |
| Annual Report | Global AI Power Report (플래그십 유료 콘텐츠) |

---

## 제품 확장 로드맵

| Phase | 제품 | 가격대 | 조건 |
|-------|------|--------|------|
| Phase 1 | Weekly Intelligence (Index 포함) | $15~50/월 | 즉시 가능 |
| Phase 2 | AI Power Terminal (정량 데이터) | $1,000~10,000/년 | 데이터 파이프라인 구축 후 |
| Phase 3 | AI Power Terminal Enterprise | 별도 협의 | VC·정부 고객 확보 후 |

---

## 주의사항 (운영 리스크)

1. **수치 공신력**: Phase 1에서 구체적 국가/기업 점수(예: USA 92, China 85)를 공개할 경우 방법론 검증 없이는 브랜드 신뢰도 훼손 위험. Phase 1에서는 방향·강도 신호(↑↓)로 제한.
2. **데이터 소스 의존**: Phase 2 정량화는 외부 API(Crunchbase 등) 비용 및 접근 계약 필요.
3. **주관성 리스크**: 정성 판단 기반 Index는 편집 기준(scoring rubric)을 명문화해야 일관성 유지.

---

## Weekly vs Daily 전략 노트

> "Daily Report로 독자를 획득하고, Weekly Intelligence로 유료 전환한다."

- Daily: 뉴스 큐레이션 + 레이어 신호 추적 → 무료/기본 구독
- Weekly: AI Power Index Update + Scenario 업데이트 + Power Shift 분석 → 유료 전환 핵심 콘텐츠
- Monthly: Index 추세선 → Premium 콘텐츠
- Annual: Global AI Power Report → Enterprise 플래그십

CB Insights 플레이북의 핵심이 Newsletter → Database → Intelligence Platform이듯, AI Power Atlas도 Daily → Weekly → Index → Terminal 순서로 가치 계단을 올린다.
