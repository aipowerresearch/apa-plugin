# Translation Policy — 한국어 부록

> 공통 정책: `translation-policy.md` 참조.
> 본 파일은 한국어 번역에만 적용되는 어휘 표·직역체 사례·특수 규칙.

---

## 1. 한국어 우선 원칙 (세부)

영어 그대로 둘 수 있는 5가지 외에는 모두 한글 번역.
한국어 사용자는 한자어·한글 혼용에 익숙하지만, **영어 단어 그대로 노출은 가급적 회피**.

---

## 2. 반드시 번역해야 하는 어휘 표 (영어 그대로 사용 금지)

| 영어 | 한글 (필수) |
|---|---|
| implementation | 구현 |
| framework | 프레임워크 |
| infrastructure | 인프라 |
| ecosystem | 생태계 |
| stakeholder | 이해관계자 |
| benchmark | 벤치마크 |
| deployment | 배포 |
| baseline | 기준선 |
| migration | 이전 / 마이그레이션 |
| adoption | 도입 |
| capability | 역량 |
| latency | 지연 시간 |
| throughput | 처리량 |
| cluster | 클러스터 |
| scaling | 확장 |
| feedback loop | 피드백 루프 |
| supply chain | 공급망 |
| compute | 컴퓨트 / 연산 |
| implication | 시사점 |
| revenue | 매출 |
| valuation | 기업가치 |
| churn | 이탈율 |
| moat | 해자 |
| commoditization | 범용화 |
| acquisition | 인수 |
| consolidation | 통합 / 집중 |
| disruption | 파괴적 변화 |
| inference | 추론 |
| training | 훈련 / 학습 |

---

## 3. 자주 발생하는 직역체 사례

### Bad (직역체)
- "이는 ~을 의미합니다" (영어 "This means ~"의 직역)
- "그것은 ~합니다" (대명사 "It" 직역)
- "~에 대한 영향" (전치사 "on/about" 직역)
- "전략적인 implications를 가집니다" (영어 단어 그대로)
- "AI 산업은 ~를 보고 있다" ("the industry is seeing" 직역)
- "이러한 접근은 ~을 나타낸다" ("This approach represents ~" 직역)

### Good (자연스러운 한국어)
- "즉 ~입니다" / "결과적으로 ~합니다"
- (대명사 생략 또는 구체 명사로 대체)
- "~에 미치는 영향"
- "전략적 시사점이 있습니다"
- "AI 산업이 ~를 겪고 있습니다"
- "이 방식은 ~를 보여줍니다"

---

## 4. 한국어 특수 규칙

- **격식체 일관**: 모든 종결 어미는 "~입니다 / ~습니다 / ~합니다 / ~해요"로 통일.
- **반말 절대 금지**: "~이다 / ~한다 / ~했다 / ~해라" 사용 금지.
- **한자어 적정 사용**: 너무 한자어 위주면 딱딱함, 너무 순한글이면 가벼움. 보고서 톤은 한자어 중심 + 자연스러운 한글 조합.
- **외래어 표기법**: 국립국어원 외래어 표기법 준수 ("프레임워크" O / "프레임웍" X, "벤치마크" O / "벤치마킹"은 의미 다름).

---

## 5. 자동 검수 화이트리스트 (verify_daily.sh)

다음 영문은 KO 본문에 그대로 등장해도 영문 비율 카운트에서 제외:

### 고유명사 (기업·제품·법령·지표)
OpenAI, Anthropic, NVIDIA, Microsoft, Google, Broadcom, Meta, Amazon,
GPT-5.5, GB200, NVL72, Claude, Azure, Copilot, Cursor,
Terminal-Bench, OSWorld, MRCR, MMLU, GPQA,
Stanford AI Index, Frontier, ChatGPT, Gemini,
ASD, AISI, RSP, EU AI Act, MATCH Act,
Beehiiv, FastComet, Hetzner

### 약어
AI, GPU, CPU, API, MCP, RAG, LLM, HBM, ARR, MRR, KPI, ROI,
EU, US, UK, KR, JP, CN, OECD, G7,
L1~L10, S01~S09 (레이어·섹션 코드),
PASS, FAIL, HIGH, MEDIUM, LOW,
Q1~Q4, B(billion), M(million), K(thousand), T(trillion),
USD, EUR, KRW, JPY, CNY

### 단위 기호
$, €, ¥, ₩, %, °C, MW, GW, TWh
