## 추가 수집 지침: MCP/에이전트 프로토콜 생태계 및 SaaS AI 통합 모니터링

### 배경
AI 산업에서 구조적 전환이 진행 중이다. 기존에 API(개발자가 코드로 연결)로만 
가능했던 서비스 간 연결이, MCP(Model Context Protocol) 등 에이전트 프로토콜을 
통해 AI 모델이 직접 서비스에 플러그인되는 구조로 전환되고 있다.

이것은 다음과 같은 Power Flow를 만든다:
- L3 미들웨어: API 중심 락인 구조 → MCP/에이전트 프로토콜 중심으로 재편
- L4 플랫폼: AI 에이전트가 기존 대시보드/UI를 대체하는 인터페이스 전환 가속
- L5 앱: SaaS 서비스들이 MCP 서버를 제공하지 않으면 AI 에이전트 생태계에서 배제되는 새로운 락인 구조 형성

이 전환은 "API의 점진적 대체"이자 "에이전트 오케스트레이션 지형의 근본적 변화"이며,
APA가 추적해야 할 핵심 권력 이동 신호이다.

### 추가 수집 소스 (기존 소스에 병합)

#### Tier 1: 프로토콜 및 프레임워크 공식 소스
- Anthropic MCP 공식 저장소 및 블로그 (modelcontextprotocol.io, anthropic.com/news)
- OpenAI Agents SDK / Plugins / GPT Store 업데이트 (openai.com/blog)
- Google A2A(Agent-to-Agent) 프로토콜 발표 (developers.googleblog.com)
- LangChain / LangGraph 공식 블로그 (blog.langchain.dev)
- CrewAI, AutoGen, OpenClaw 등 에이전트 프레임워크 업데이트

#### Tier 2: AI를 적극 도입하는 주요 SaaS 플랫폼 프로덕트 블로그
- Beehiiv (product.beehiiv.com)
- Notion (notion.so/blog, notion.so/product)
- Figma (figma.com/blog)
- Shopify (shopify.engineering)
- Stripe (stripe.com/blog)
- HubSpot (hubspot.com/blog)
- Slack / Salesforce (salesforce.com/blog)
- Vercel (vercel.com/blog)
- Supabase (supabase.com/blog)
- GitHub (github.blog)
- Atlassian (atlassian.com/blog)
- Zapier (zapier.com/blog) — 특히 MCP/에이전트와의 경쟁/통합 동향

#### Tier 3: 에이전트 생태계 커뮤니티
- r/MCP, r/LangChain, r/ClaudeAI, r/OpenAI 에서의 MCP 관련 논의
- Hacker News에서 "MCP", "agent protocol", "agentic" 키워드 포함 게시물
- X(Twitter)에서 주요 AI 인플루언서의 MCP/에이전트 관련 발언

### 추가 검색 키워드 (기존 검색 키워드에 병합)
- "MCP integration", "MCP server launch", "Model Context Protocol"
- "agent protocol", "A2A protocol", "agent-to-agent"
- "AI agent plugin", "AI native feature launch"
- "agentic workflow", "agent orchestration"
- "API replacement AI", "API to MCP migration"
- "[서비스명] + AI integration" (Beehiiv, Notion, Figma, Shopify 등)
- "SaaS AI agent", "AI-first platform"

### 신호 분류 기준

이 소스들에서 수집된 이벤트는 다음 기준으로 Signal Type을 태깅한다:

1. **MCP/프로토콜 확산 신호**: 새로운 서비스가 MCP 서버를 출시한 경우
   - Layer: L3 (미들웨어)
   - Signal Type: Power Shift
   - 분석 관점: "API → MCP 전환이 어느 속도로 진행되고 있는가"
   - Power Transfer: From(전통 API 생태계) → To(MCP/에이전트 프로토콜 생태계)

2. **에이전트 오케스트레이션 변화 신호**: 에이전트 프레임워크 간 경쟁 또는 통합
   - Layer: L3 (미들웨어) + L4 (플랫폼)
   - Signal Type: Lock-in Signal
   - 분석 관점: "어떤 프로토콜/프레임워크가 표준이 되어가고 있는가"
   - 락인 방향: MCP가 사실상 표준이 되면 Anthropic의 L3 영향력 ↑

3. **SaaS AI 통합 신호**: 기존 SaaS가 AI 에이전트 접근을 허용한 경우
   - Layer: L4 (플랫폼) + L5 (앱)
   - Signal Type: Power Shift
   - 분석 관점: "AI 에이전트가 기존 대시보드/UI를 대체하는 속도"
   - Power Transfer: From(인간 중심 UI/대시보드) → To(AI 에이전트 인터페이스)

4. **에이전트 인프라 투자 신호**: 에이전트 관련 스타트업 펀딩, M&A
   - Layer: L7 (자본) + L3 (미들웨어)
   - Signal Type: Capital Signal
   - 분석 관점: "자본이 에이전트 생태계의 어느 레이어에 집중되고 있는가"

### Impact Score 부여 기준 (MCP/에이전트 특화)
- 5점: Anthropic/OpenAI/Google 등 주요 LLM 제공자의 프로토콜 변경
- 5점: Fortune 500 SaaS가 MCP 서버를 공식 출시
- 4점: 주요 SaaS(사용자 1M+)의 AI 에이전트 통합 발표
- 4점: 에이전트 프레임워크 간 표준화 합의 또는 호환성 발표
- 3점: 중소 SaaS의 MCP 서버 출시
- 3점: 에이전트 관련 스타트업의 시리즈 A+ 펀딩
- 2점: 에이전트 커뮤니티에서의 프로토콜 비교/논쟁
- 1점: 개별 개발자의 MCP 활용 사례 공유

### 피드백 루프 감지 추가
기존 6개 피드백 루프에 추가로 다음을 감지한다:

- **L3 → L4 → L5 에이전트 캐스케이드**: MCP 표준 확산 → 플랫폼이 MCP 의무 지원 
  → 앱이 에이전트 친화적으로 재설계 → 인간 UI 의존도 하락
- **L3 → L2 프로토콜 락인**: MCP가 표준이 되면 → MCP를 만든 Anthropic/Claude의 
  L2 모델 레이어 영향력 강화 (프로토콜 설계자가 모델 선택을 좌우)

### 주의사항
- 단순한 "AI 기능 추가" 뉴스와 "에이전트 프로토콜을 통한 구조적 연결" 뉴스를 구분할 것.
  예: "Notion에 AI 요약 기능 추가" (일반 AI 기능) vs "Notion이 MCP 서버를 출시하여 
  Claude/ChatGPT에서 직접 Notion 데이터에 접근 가능" (에이전트 프로토콜 확산 신호)
- 후자만이 APA가 추적해야 할 권력 이동 신호이다.
