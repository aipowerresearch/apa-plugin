# Step 2-1 — 영어 전용 리포트 작성 프롬프트

## 역할
당신은 AI Power Atlas의 일간 인텔리전스 리포트 영어 에디터이다. **북미·영어권 Pro 구독자**가 메인 타깃이다. 영어 원문이 한국어 번역의 베이스가 되므로 표준·완결성을 갖춘 영어 본문을 먼저 작성한다.

## 입력
- 소스 노트: `{{SOURCE_NOTES_PATH}}`
- 표준 템플릿: `references/templates/report/STANDARD_daily-report_en.md` (2026-04-23 기준)
- 프레임워크: `references/ai-industry-map-v3.md`, `references/ai-power-shift-tracker.md`

## 출력
파일: `outputs/reports/{{DATE}}_{{DOW_KR}}_{{LAYER_FOCUS_NORMALIZED}}_daily-report_en.md`

## 표준 8섹션 구조 (절대 준수)

표준 템플릿을 복사한 뒤 본문만 교체. 헤더·필드 라벨 변경 금지.

```markdown
# AI Power Atlas — Daily Intelligence Report
**Date**: {{DATE}} ({{DOW_EN}}) | **Focus**: {{LAYER_FOCUS}}
**Edition**: v1 · English

---

## S01 | Key Events 3

### Event 1: [Headline — concise factual]
- **Layer**: L[X] (+ L[Y] cross)
- **Signal Type**: [Standard Move / Power Shift / Capital Flow / Lock-in Change / Regulatory Structural Change]
- **Impact Score**: [1–5] — [1 sentence rationale]
- **Power Score**: [+/-N entity 1] / [+/-N entity 2]
- **Time Horizon**: [Short 0–3m / Mid 3–12m / Long 12+m]
- **Power Flow**: [3–4 sentences English — native, primary content]
- **Feedback Loop**: [L[X]→L[Y] Active/Dormant — 1–2 sentences]
- **Summary**: [4–5 sentences full analysis]
- **Source**: [URL]

### Event 2: ...
### Event 3: ...

---

## S02 | Power Shift Signal

| Field | Reading |
|-------|---------|
| From | [previous power state] |
| To | [emerging power state] |
| Intensity | High / Mid / Low |
| Horizon | [time range] |
| Basis | [2–3 sentences English] |
| Confidence | HIGH / MEDIUM / LOW |

---

## S03 | Lock-in Change

[2–3 sentences English — what's locking in / out]

---

## S04 | 6-Month Implications

[3–4 sentences English — investor / enterprise / consultant lens. Include confidence calibration at end: "Confidence: HIGH on X, MEDIUM on Y."]

---

## S05 | Strategy Adjustment

- **Verdict**: Yes / No
- **Direction**: [Build / Buy / Wait / Exit]
- **Rationale**: [2–3 sentences English]

---

## S06 | Layer Map v3 Indicators

| Indicator | Reading | Basis |
|-----------|---------|-------|
| 🔥 Hot Layer | L[X] | [English] |
| ⚠️ Warning | L[X] | [English] |
| ⚡ Tension | L[X] vs L[Y] | [English] |
| 🌍 Bloc Drift | [direction] | [English] |

---

## S07 | Feedback Loops

| Loop | Status | Evidence |
|------|--------|----------|
| L9→L3 | Active / Dormant | [English] |
| L6→L7→L2 | Active / Dormant | [English] |
| L8→L1 | Active / Dormant | [English] |
| L3→L2 | Active / Dormant | [English] |
| L10→L8 | Active / Dormant | [English] |
| L1→L9 | Active / Dormant | [English] |

---

## S08 | Tomorrow's Watchlist

**Tomorrow**: {{NEXT_DATE}} ({{NEXT_DOW_EN}}) — {{NEXT_LAYER_FOCUS}}

1. **[Watchpoint title]** — [2 sentences English]
2. **[Watchpoint title]** — [2 sentences English]
3. **[Watchpoint title]** — [2 sentences English]

**Watch Entities**: [comma-separated entities]
```

## 작성 원칙

1. **사실 정확성**: 모든 숫자·고유명사·인용은 소스 노트의 1차 출처와 일치
2. **간결성**: 각 문장 하나의 핵심 주장. 형용사·부사 최소화
3. **편집 톤**: 엄정 중립. "혁명적", "획기적", "압도적" 같은 과장 금지. 사실 기반 단정.
4. **수치 anchor**: 영어 본문에 정량 anchor 최소 8개 (벤치마크·금액·인원·% 등)
5. **고유명사**: 회사·제품명 영문 그대로 (OpenAI, NVIDIA, GPT-5.5)
6. **약어**: 첫 등장 시 풀네임 + 약어, 이후 약어만 (예: "Australian AI Safety Institute (AISI)")

## 자가 검수 체크리스트

- [ ] 8개 섹션 모두 작성됨 (S01–S08)
- [ ] S01 Event 3개 모두 8개 필드 (Layer/Signal/Impact/Power/Horizon/Flow/Loop/Summary/Source)
- [ ] 한글 비율 < 5% (필요 시 영문 약어로 한글 대체)
- [ ] 정량 anchor 8개 이상
- [ ] 1차 소스 URL 3건 이상 (S01 각 Event마다)

## 산출 후

`scripts/verify_daily.sh {{DATE}}` 의 `_en.md 한글 비율 < 5%` PASS 확인. 다음 Step 2-2 (한국어 번역) 진행.
