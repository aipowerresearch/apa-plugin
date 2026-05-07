# AI Power Shift Tracker
*AI Power Atlas 참조 파일 | v1.0 | 2026-03-10*

---

## 개요

**AI Power Shift Tracker**는 일간 리포트 S02 신호를 주단위로 누적·집계하여 AI 산업 권력 구조의 방향성 변화를 추적하는 독립 출력물이다. 단발성 이벤트가 아니라 **"이번 주 누가 권력을 얻고 누가 잃었는가"**를 레이어별·주체별로 시각화한다.

---

## 출력 주기

- **갱신**: 매일 S02 신호 자동 누적
- **발행**: 매주 일요일 `/ai-power-atlas:weekly` 실행 시 주간 종합에 포함
- **독립 발행**: 별도 요청 시 단독 섹션으로 추출 가능

---

## Power Shift 기록 형식

### 일간 누적 테이블

매일 S02에서 추출한 신호를 아래 형식으로 누적 기록한다:

| 날짜 | Layer | From (권력 이탈) | To (권력 유입) | 강도 | Horizon | Power Score 요약 |
|------|-------|-----------------|---------------|------|---------|-----------------|
| 03-09 (월) | L1+L2 | 오픈소스 진영(분산) | NVIDIA+Anthropic | High | Mid | +2 NVIDIA, +1 Anthropic |
| 03-10 (화) | L3 | 분산형 L3 생태계 | Anthropic (표준 설계자) | High | Mid | +2 Anthropic |
| 03-10 (화) | L4 | Microsoft Copilot | Google Gemini | High | Short | +2 Google, -1 Microsoft |
| 03-10 (화) | L4 | OpenAI (iOS 접근) | Apple-Google 연합 | Medium | Mid | +1 Apple+Google |

---

## 주간 집계 형식 (Weekly Summary)

```markdown
## AI Power Shift — Week [N] (YYYY-MM-DD ~ YYYY-MM-DD)

### 이번 주 최대 권력 이동

| 순위 | 수혜 주체 | 피해 주체 | 레이어 | 근거 |
|------|----------|----------|--------|------|
| 1 | Anthropic | 분산형 L3 생태계 | L3 | MCP+Agent Skills 이중 표준 장악 |
| 2 | Google | Microsoft | L4 | Gemini $14 vs Copilot $30 가격 역전 |
| 3 | Apple+Google 연합 | OpenAI | L4 | iOS 27 Gemini 통합 |

### 레이어별 권력 방향성

| Layer | 방향 | 주요 이동 |
|-------|------|----------|
| L1 | → 유지 | |
| L2 | ↓ (종속 심화) | L3→L2 Loop 4: Anthropic 표준 의존 |
| L3 | ↑ Anthropic | MCP+Agent Skills 이중 표준 |
| L4 | ⇄ 재편 중 | Google vs Microsoft 가격 전쟁 |
| L5~L10 | → 모니터링 | 이번 주 주요 신호 없음 |

### 이번 주 활성 피드백 루프

| Loop | 상태 | 영향 |
|------|------|------|
| Loop 4 (L3→L2) | 🔴 Active | L3 표준이 L2 모델 선택권 역방향 제어 |
| 나머지 | ⚪ Dormant | |

### 다음 주 예상 권력 이동 포인트

- Google Gemini $14 실적용(3월 17일) 이후 Microsoft 대응 전략 확인
- Anthropic Agent Skills 파트너 탑재 속도 (Canva·Notion 등 L5 기업)
- Apple iOS 27 WWDC 추가 발표 여부
```

---

## Power Score 누적 집계 (주간)

각 주체의 주간 Power Score 합산으로 "이번 주 가장 강해진 플레이어"를 정량화한다.

### 집계 방식

```
주간 Power Score = Σ(일간 S02 Power Score) / 발생 이벤트 수
방향: ▲ 상승 / ▼ 하락 / → 유지
```

### 예시 (Week 10 부분 집계, 월~화)

| 주체 | 월 Score | 화 Score | 주간 합산 | 방향 |
|------|---------|---------|----------|------|
| Anthropic | +1 | +2 | +3 | ▲▲ |
| Google | 0 | +2 | +2 | ▲▲ |
| NVIDIA | +2 | 0 | +2 | ▲ |
| Apple | 0 | +1 | +1 | ▲ |
| Microsoft | 0 | -1 | -1 | ▼ |
| OpenAI | -1 | 0 | -1 | ▼ |

---

## Entity 추적 범위

### 기업 (Company Power Watch 연동)

**Tier 1 고정 추적** (매주):
- NVIDIA, OpenAI, Google DeepMind, Microsoft, Meta AI, Amazon AWS, Alibaba/DeepSeek

**Tier 2 동적 추적** (이벤트 발생 시):
- Apple, Anthropic, xAI, Baidu, Samsung, Qualcomm, ARM

### 국가·지역 (Geopolitics)

- 미국, 중국, EU, 한국, 인도, 중동(UAE·사우디)

### 기술·표준 (Technology)

- MCP, Agent Skills, AAIF, 특정 모델 시리즈

---

## 발행 채널 연동

| 채널 | 형태 | 발행 시점 |
|------|------|----------|
| 주간 리포트 (W01) | 마크다운 섹션 | 일요일 weekly 실행 |
| 뉴스레터 (EN/KO) | 테이블 블록 | 일요일 발행 |
| 블로그 | 독립 섹션 | 일요일 |
| AI Power Index 연동 | Company Power Watch 업데이트 | 주간 |

---

## 관련 참조 파일

- `ai-power-index.md` — Power Score 정의, Company Power Watch
- `report-template.md` — S02 일간 신호 형식
- `scenario-tracker.md` — Weekly Intelligence W01 섹션
- `ai-industry-map-v3.md` — Layer 구조 기준

---

*v1.0 — 2026-03-10 생성*
*킬러 콘텐츠 3 반영: AI Power Shift Tracker 독립 파일화*
