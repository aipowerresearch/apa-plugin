# News Scanner — Supplementary Collection Rules

> news-scanner SKILL.md의 기본 프로세스에 추가로 적용하는 보완 규칙.
> news-scanner 실행 시 이 파일을 함께 참조한다.
> Created: 2026-03-31

---

## 1. Key Figure Check (Step 4 추가)

기본 웹 검색(Step 3) 이후, 핵심 인물 SNS 확인 단계를 추가한다.

### 절차
1. `references/key-figures-tracker.md`에서 오늘 집중 레이어의 ★★★ 인물 확인
2. 각 인물의 X 포스트 검색: `from:[handle] [layer keyword]` (최근 48시간)
3. 주목할 발언(발표, 의견, 제품 힌트) → 소스 노트에 "Key Figure Signal"로 추가
4. LinkedIn 공식 발표/채용 공고도 확인

### 레이어별 ★★★ 인물 빠른 참조

| 요일 | 집중 레이어 | ★★★ 인물 | X Handle |
|------|-----------|----------|----------|
| 월 | L1+L2 | Jensen Huang, Sam Altman, Dario Amodei, Demis Hassabis, Elon Musk | @jensenhuang, @sama, @DarioAmodei, @demishassabis, @elonmusk |
| 화 | L3+L4 | Clement Delangue, Kevin Scott | @ClementDelangue, @kevin_scott |
| 수 | L5 | (★★ 인물: Marc Benioff @Benioff, Bill McDermott @BillRMcDermott) | |
| 목 | L6 | Brett Adcock | @adcock_brett |
| 금 | L7+L8 | Marc Andreessen | @pmarca |
| 토 | L9+L10 | Jan Leike, Yoshua Bengio, Fei-Fei Li | @janleike, @Yoshua_Bengio, @drfeifei |

### Impact Score 규칙
- SNS 일반 발언: Impact Score **최대 3**
- SNS에서의 공식 발표 (예: 신제품 출시 언급): 통상 기준 적용 (최대 5)
- 루머/추측성 발언: Impact Score **최대 2**, `[미확인]` 태그

---

## 2. Confidence Calibration (리포트 작성 시 적용)

> `references/report-template.md`의 "Confidence Calibration Rules" 섹션 참조

소스 노트 작성 시에도 아래를 적용:
- 각 Key Event Candidate에 예비 확신도(HIGH/MEDIUM/LOW) 태깅
- 단일 소스만 있는 이벤트는 자동 MEDIUM 이하
- Tier 3 소스만 있는 이벤트는 자동 LOW

---

## 3. Prediction Tracking Integration

리포트 생성 후 아래 추가 작업 실행:
1. S08 Tomorrow Watchlist의 3개 예측을 `outputs/predictions/daily/YYYY-MM-DD-predictions.md`에 저장
2. 전일 S08 예측 파일이 있으면 당일 뉴스와 대조하여 ✅/❌/⚠️ 판정
3. 판정 결과를 해당 예측 파일에 업데이트

### 예측 기록 형식
```markdown
## [날짜] S08 Predictions

### P-[YYYYMMDD]-1
- **예측**: [내용]
- **레이어**: L[X]
- **확신도**: HIGH / MEDIUM / LOW
- **검증일**: [익일]
- **결과**: ✅ / ❌ / ⚠️ / ⏳
- **비고**: [적중/미적중 이유]
```

---

## 4. External Baseline Reference

> `references/baseline-data.md` 참조

분석 시 자체 데이터가 부족한 영역에서는 외부 기준점 데이터를 활용:
- 투자 규모 비교 → Stanford AI Index, CB Insights 수치
- 모델 순위 비교 → LMSYS Chatbot Arena
- 시장 점유율 → Fortune AIQ 50, Forbes AI 50
- 정책 동향 → OECD AI Policy Observatory

---

## 5. MCP/에이전트 프로토콜 생태계 모니터링

> `mcp-agent-scanner` 스킬 내용을 news-scanner 실행 시 자동 적용한다.
> Created: 2026-04-07

### 배경

API 중심 서비스 연결 → MCP/에이전트 프로토콜 기반 연결로 구조적 전환 진행 중.
Power Flow: L3(미들웨어 재편) → L4(에이전트가 UI 대체) → L5(MCP 미제공 SaaS 배제).

### 추가 수집 소스

#### Tier 1: 프로토콜 및 프레임워크 공식
- Anthropic MCP (modelcontextprotocol.io, anthropic.com/news)
- OpenAI Agents SDK / Plugins (openai.com/blog)
- Google A2A 프로토콜 (developers.googleblog.com)
- LangChain / LangGraph (blog.langchain.dev)
- CrewAI, AutoGen, OpenClaw

#### Tier 2: AI 도입 주요 SaaS 프로덕트 블로그
- Beehiiv, Notion, Figma, Shopify, Stripe, HubSpot
- Slack/Salesforce, Vercel, Supabase, GitHub, Atlassian, Zapier

#### Tier 3: 에이전트 커뮤니티
- r/MCP, r/LangChain, r/ClaudeAI, r/OpenAI
- Hacker News: "MCP", "agent protocol", "agentic"
- X: 주요 AI 인플루언서 MCP/에이전트 발언

### 추가 검색 키워드
- "MCP integration", "MCP server launch", "Model Context Protocol"
- "agent protocol", "A2A protocol", "agent-to-agent"
- "AI agent plugin", "AI native feature launch"
- "agentic workflow", "agent orchestration"
- "API replacement AI", "API to MCP migration"
- "[서비스명] + AI integration"
- "SaaS AI agent", "AI-first platform"

### 신호 분류 (4가지)
1. **MCP/프로토콜 확산**: L3, Power Shift — API→MCP 전환 속도
2. **에이전트 오케스트레이션 변화**: L3+L4, Lock-in Signal — 표준화 경쟁
3. **SaaS AI 통합**: L4+L5, Power Shift — 에이전트가 UI 대체하는 속도
4. **에이전트 인프라 투자**: L7+L3, Capital Signal — 자본 집중 레이어

### Impact Score (MCP 특화)
- 5점: 주요 LLM 프로토콜 변경 / Fortune 500 MCP 서버 출시
- 4점: 1M+ SaaS AI 에이전트 통합 / 프레임워크 표준화 합의
- 3점: 중소 SaaS MCP 출시 / 에이전트 스타트업 시리즈 A+
- 2점: 커뮤니티 프로토콜 비교/논쟁
- 1점: 개별 개발자 MCP 활용 사례

### 추가 피드백 루프
- **L3→L4→L5 에이전트 캐스케이드**: MCP 확산 → 플랫폼 MCP 의무지원 → 앱 에이전트 친화 재설계
- **L3→L2 프로토콜 락인**: MCP 표준화 → Anthropic/Claude L2 영향력 강화

### 핵심 구분
- ❌ "Notion에 AI 요약 기능 추가" = 일반 AI 기능 (비추적)
- ✅ "Notion이 MCP 서버 출시하여 Claude에서 직접 접근 가능" = 에이전트 프로토콜 확산 신호 (추적)
