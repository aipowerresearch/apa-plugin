# AI Power Atlas — News Source List

> news-scanner 스킬에서 참조하는 뉴스 소스 목록.
> Tier 1: 매일 스캔 / Tier 2: 격일 / Tier 3: 주간

---

## Tier 1 — Daily (15개)
> 독점 정보, Tier 1 플레이어 직접 발표, 정책 1차 소스

| # | Source | URL | Focus Layers | Type |
|---|--------|-----|-------------|------|
| 1 | OpenAI Blog | https://openai.com/blog | L2, L9 | Official |
| 2 | Anthropic News | https://www.anthropic.com/news | L2, L9 | Official |
| 3 | Google DeepMind Blog | https://deepmind.google/discover/blog | L2, L1 | Official |
| 4 | NVIDIA Blog | https://blogs.nvidia.com | L1, L2 | Official |
| 5 | The Information (AI) | https://www.theinformation.com | L2, L7 | Premium |
| 6 | SemiAnalysis | https://semianalysis.com | L1, L2 | Technical |
| 7 | Reuters Technology | https://www.reuters.com/technology | L7, L8 | News |
| 8 | Bloomberg Technology | https://www.bloomberg.com/technology | L7, L8 | News |
| 9 | White House (AI policy) | https://www.whitehouse.gov/briefing-room | L8 | Official |
| 10 | EU AI Office | https://digital-strategy.ec.europa.eu/en/policies/ai-office | L8 | Official |
| 11 | Hugging Face Blog | https://huggingface.co/blog | L2, L3 | Technical |
| 12 | Microsoft AI Blog | https://blogs.microsoft.com/ai | L2, L4 | Official |
| 13 | Meta AI Blog | https://ai.meta.com/blog | L2, L3 | Official |
| 14 | xAI Blog | https://x.ai/blog | L2 | Official |
| 15 | Mistral AI Blog | https://mistral.ai/news | L2 | Official |

---

## Tier 2 — Every Other Day (15개)
> 고품질 분석, 연구기관, 산업 전문 미디어

| # | Source | URL | Focus Layers | Type |
|---|--------|-----|-------------|------|
| 16 | Stratechery | https://stratechery.com | L4, L5, L7 | Analysis |
| 17 | Import AI (Jack Clark) | https://importai.substack.com | L2, L9 | Newsletter |
| 18 | Semafor AI | https://www.semafor.com/tech-biz | L2, L7, L8 | News |
| 19 | TechCrunch AI | https://techcrunch.com/category/artificial-intelligence | L5, L7 | News |
| 20 | Wired AI | https://www.wired.com/tag/artificial-intelligence | L5, L9, L10 | News |
| 21 | MIT Technology Review | https://www.technologyreview.com | L2, L9, L10 | Research |
| 22 | VentureBeat AI | https://venturebeat.com/ai | L5, L7 | News |
| 23 | The Batch (DeepLearning.AI) | https://www.deeplearning.ai/the-batch | L2, L3 | Newsletter |
| 24 | Andreessen Horowitz (a16z) | https://a16z.com/topics/ai-ml | L7, L5 | VC Analysis |
| 25 | Sequoia Capital AI | https://www.sequoiacap.com/topic/ai | L7 | VC Analysis |
| 26 | RAND AI Research | https://www.rand.org/topics/artificial-intelligence.html | L8, L9 | Research |
| 27 | Georgetown CSET | https://cset.georgetown.edu | L1, L8 | Research |
| 28 | AI Now Institute | https://ainowinstitute.org | L9, L10 | Research |
| 29 | Korean IITP 보도자료 | https://www.iitp.kr/kr/1/news/pressReleaseView.it | L8 (KR) | Official |
| 30 | 과학기술정보통신부 | https://www.msit.go.kr/bbs/list.do?sCode=user&mPid=60&mId=61 | L8 (KR) | Official |

---

## Tier 3 — Weekly (12개)
> 학술·리서치, 신흥 시장, 장기 트렌드

| # | Source | URL | Focus Layers | Type |
|---|--------|-----|-------------|------|
| 31 | arXiv cs.AI | https://arxiv.org/list/cs.AI/recent | L2, L3 | Academic |
| 32 | arXiv cs.LG | https://arxiv.org/list/cs.LG/recent | L2 | Academic |
| 33 | Papers With Code | https://paperswithcode.com | L2, L3 | Academic |
| 34 | AI Index (Stanford HAI) | https://aiindex.stanford.edu | L10, L7 | Research |
| 35 | World Economic Forum AI | https://www.weforum.org/agenda/artificial-intelligence | L8, L10 | Research |
| 36 | Atlantic Council GeoTech | https://www.atlanticcouncil.org/programs/geotech-center | L8 | Research |
| 37 | Brookings AI | https://www.brookings.edu/topic/artificial-intelligence | L8, L10 | Research |
| 38 | Electronics Times (KR) | https://www.etnews.com | L1 (KR) | News |
| 39 | ZDNet Korea | https://zdnet.co.kr | L4, L5 (KR) | News |
| 40 | Nikkei Asia Tech | https://asia.nikkei.com/Business/Tech | L1, L8 (Asia) | News |
| 41 | South China Morning Post Tech | https://www.scmp.com/tech | L2, L8 (CN) | News |
| 42 | Indian Express Technology | https://indianexpress.com/section/technology | L8 (IN) | News |

---

## 레이어별 핵심 소스 요약

| Layer | 핵심 Tier 1 소스 | 보조 소스 |
|-------|----------------|---------|
| L1 Compute | NVIDIA Blog, SemiAnalysis | Georgetown CSET, arXiv |
| L2 Models | OpenAI, Anthropic, DeepMind, HF | Import AI, The Batch |
| L3 Middleware | Hugging Face, Meta AI | Papers With Code |
| L4 Platform | Microsoft AI, a16z | Stratechery |
| L5 Apps | TechCrunch, VentureBeat | Wired |
| L6 Vertical | Reuters, Bloomberg | Nikkei Asia |
| L7 Capital | Bloomberg, The Information | Sequoia, a16z |
| L8 Geopolitics | White House, EU AI Office, MSIT | RAND, Atlantic Council |
| L9 Safety | Anthropic, AI Now | RAND, Wired |
| L10 Macro | MIT Tech Review, WEF | Stanford HAI, Brookings |

---

## 검색 쿼리 구성 원칙

```
[Layer Keyword] + [Tier 1 Source Domain] + [date range: past 24h or 48h]
```

예시:
- `"foundation model" site:openai.com OR site:anthropic.com`
- `"export control" OR "chip ban" site:reuters.com OR site:bloomberg.com`
- `"AI funding" OR "AI IPO" site:bloomberg.com OR site:theinformation.com`

---

---

## Key Industry Figure Tracker

> 미디어 소스 외에 핵심 인물의 X/LinkedIn 계정을 추적 소스로 활용.
> 상세 목록: `references/key-figures-tracker.md` 참조

### 활용 규칙
- 일일 스캔 시 해당 요일 레이어의 ★★★ 인물 X 포스트 확인
- SNS 발언은 Impact Score 최대 3 (공식 발표 제외)
- 검색 쿼리: `from:[handle] [layer keyword]`

### 레이어별 최우선 추적 인물 (★★★)

| Layer | 인물 | X Handle |
|-------|------|----------|
| L1 | Jensen Huang (NVIDIA) | @jensenhuang |
| L2 | Sam Altman (OpenAI) | @sama |
| L2 | Dario Amodei (Anthropic) | @DarioAmodei |
| L2 | Demis Hassabis (DeepMind) | @demishassabis |
| L2 | Elon Musk (xAI) | @elonmusk |
| L3 | Clement Delangue (HF) | @ClementDelangue |
| L4 | Kevin Scott (Microsoft) | @kevin_scott |
| L6 | Brett Adcock (Figure AI) | @adcock_brett |
| L7 | Marc Andreessen (a16z) | @pmarca |
| L9 | Jan Leike (Anthropic) | @janleike |
| L9 | Yoshua Bengio (Mila) | @Yoshua_Bengio |
| L10 | Fei-Fei Li (Stanford HAI) | @drfeifei |

---

*Last updated: 2026-03-31 | Sources: 42개 media + 40명 key figures | Tier 1: 15 / Tier 2: 15 / Tier 3: 12*
