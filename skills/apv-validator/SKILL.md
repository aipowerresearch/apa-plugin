---
name: apv-validator
description: >
  AI Power Atlas 발행물 전용 Atlas Publication Validator (APV) — 12-point 인간 문체 검증기.
  리포트(_en.md / _ko.md), 블로그 HTML, 뉴스레터 HTML 등 APA 파이프라인 산출물이 AI가
  자동 생성한 텍스트가 아닌 숙련된 인텔리전스 애널리스트가 직접 작성한 분석으로 읽히도록 보증한다.
  파이프라인 Step 2(리포트), Step 4(뉴스레터), Step 5–6(블로그) 완료 직후 또는 단독으로 실행 가능.
  반드시 사용해야 하는 경우: "APV 실행", "run APV", "발행물 검수", "publication voice check",
  "리포트 문체 검증", "블로그 검수", "뉴스레터 검수", "AI 냄새 검수", "인간 문체 체크",
  "human voice check", "publication validator", "산출물 품질 검사", 또는 APA 파이프라인
  산출물이 생성된 뒤 품질 검증이 필요할 때. 파이프라인 완료 후 verify_daily.sh와 별도로 실행하며,
  verify_daily.sh가 구조·마커를 검증한다면 APV는 문체·어조·인간적 품질을 검증한다.
  APA 프로젝트에서 리포트·블로그·뉴스레터가 생성되었을 때 자동으로 이 스킬을 트리거해야 한다.
---

# Atlas Publication Validator (APV)

APA 발행물 전용 12-point 인간 문체 검증기.
LVV(Lecture Voice Validator)의 구조를 차용하되, 체크포인트를 인텔리전스 분석 발행물에 맞게 재설계.

**목적**: AI Power Atlas의 리포트·블로그·뉴스레터가 "AI가 찍어낸 뉴스 요약"이 아닌 "시니어 애널리스트가 직접 쓴 인텔리전스 브리핑"으로 읽히도록 보증한다. Pro 구독자($15–30/월)가 비용을 지불하는 것은 자동 요약이 아니라 인간적 판단과 통찰이다.

**적용 대상**: 리포트 MD (`_en.md`, `_ko.md`), 블로그 HTML (`-en.html`, `-ko.html`), 뉴스레터 HTML (free/pro × en/ko)

---

## Setup

1. 대상 파일 확정 — 사용자가 지정하지 않으면 오늘 날짜의 리포트·블로그·뉴스레터를 자동 탐색
2. 파일 유형 판별: `report` / `blog` / `newsletter` — 유형별로 일부 기준치가 다름 (아래 표 참조)
3. HTML 파일인 경우 태그를 제거하고 본문 텍스트만 추출하여 검사 대상 확정
4. 검사 대상 텍스트의 단어 수를 카운트

### 유형별 기준치 차이

| 기준 | Report | Blog | Newsletter (Free) | Newsletter (Pro) |
|------|--------|------|-------------------|-----------------|
| AI 관용구 한도 | ≤ 3 | ≤ 2 | ≤ 2 | ≤ 3 |
| 분석적 관점 삽입 최소 | 5개 | 3개 | 1개 | 4개 |
| 구체 데이터 밀도 | 1,000w당 ≥ 8개 | 1,000w당 ≥ 5개 | 1,000w당 ≥ 4개 | 1,000w당 ≥ 6개 |
| 빈 수사 비율 한도 | ≤ 0.2 | ≤ 0.25 | ≤ 0.3 | ≤ 0.2 |

---

## The 12-Point Checklist

각 포인트를 순서대로 진행. 위반 발견 시 즉시 인라인 수정 후 다음 포인트로 이동.

### Point 1 — AI 관용구 탐지 (AI Cliche Scan)

**검사**: AI가 습관적으로 생성하는 관용구·필러를 전수 검색.
금지 목록:
- 도입부 클리셰: *in today's rapidly evolving, in an era of, as we navigate, the landscape of, in this comprehensive*
- 빈 강조: *it's worth noting, importantly, significantly, notably, crucially, pivotally, fundamentally, essentially, it cannot be overstated, make no mistake*
- AI 서술 버릇: *delve into, unpack, landscape (비유적), ecosystem (기술 외), robust, comprehensive, holistic, synergy, paradigm shift, transformative, groundbreaking, game-changing, cutting-edge, leverage (동사), facilitate, utilize*
- 전환 클리셰: *that being said, having said that, with that in mind, moving forward, on a broader note, looking ahead*
- 결론 클리셰: *in conclusion, to sum up, all in all, at the end of the day, the bottom line is*

**통과 기준**: 유형별 한도 이내 (Report ≤ 3, Blog/Newsletter-Free ≤ 2, Newsletter-Pro ≤ 3).
**FAIL 시**: 해당 표현을 구체적이고 직접적인 문장으로 교체. 같은 의미를 전달하되 더 짧고 구체적인 단어를 사용.

### Point 2 — 분석적 관점 삽입 (Analytical Perspective Injection)

**검사**: 단순 사실 나열(what happened)을 넘어 분석적 관점(why it matters, what it implies)을 제공하는 구간을 카운트.
인정되는 형태:
- 인과 관계 분석: "X가 발생한 이유는 Y이며, 이는 Z를 의미한다"
- 비교 맥락 제공: "이전 사례 A와 비교하면..."
- 반직관적 해석: "표면적으로는 X이지만, 실제로는 Y"
- 미래 시사점 추론: 구체적 타임라인과 조건이 붙은 예측
- 이해관계자 영향 분석: "이 변화가 [구체 행위자]에게 미치는 영향은..."

인정되지 않는 형태:
- 사실만 나열: "A사가 B를 발표했다. C사도 D를 발표했다."
- 모호한 시사점: "이것은 업계에 큰 영향을 미칠 것이다" (구체성 없음)

**통과 기준**: 유형별 최소치 이상 (Report ≥ 5, Blog ≥ 3, NL-Free ≥ 1, NL-Pro ≥ 4).
**FAIL 시**: 사실 나열 구간에 "so what" 분석을 추가. 구체적 행위자, 수치, 타임라인을 포함.

### Point 3 — 구체 데이터 밀도 (Concrete Data Density)

**검사**: 본문에서 구체적 데이터 포인트를 카운트.
인정되는 데이터: 금액($40B), 백분율(72%), 날짜(2026-05-01), 회사명+행동(SK Hynix가 HBM4 공급 확정), 인물명+직함, CVE/논문 번호, 정확한 제품명, 구체적 수량.
인정되지 않는 데이터: "많은 기업들", "상당한 성장", "최근", "가까운 미래에", 수치 없는 형용사적 표현.

**통과 기준**: 유형별 밀도 이상 (Report ≥ 8/1,000w, Blog ≥ 5/1,000w, NL-Free ≥ 4/1,000w, NL-Pro ≥ 6/1,000w).
**FAIL 시**: 모호한 표현을 구체적 수치·이름·날짜로 교체. 원본 소스에서 데이터를 추출하여 삽입.

### Point 4 — 문장 리듬 변화 (Sentence Rhythm Variance)

**검사**: 연속 5문장의 단어 수를 측정하여 리듬 단조로움을 탐지.
진짜 애널리스트 문체는: 짧은 단정(8–12단어) + 중간 분석(20–30단어) + 긴 맥락 제공(35–50단어)이 혼재.
AI 문체는: 모든 문장이 20–30단어 범위에 모여 있음. 펀치 있는 짧은 문장이 없고, 깊이 있는 긴 분석도 없음.

**통과 기준**: 연속 5문장이 모두 같은 길이 범위(±5단어)에 있는 구간 = 0.
**FAIL 시**: 핵심 판단 문장을 짧게 끊거나(10단어 이하), 맥락 설명을 하나의 길고 정교한 문장으로 결합. 특히 S01 Summary, S03, S04에서 리듬 변화 필수.

### Point 5 — 삼박자 리스트 과잉 (Three-Beat List Overuse)

**검사**: 세 항목을 나열하는 패턴을 카운트. "X, Y, and Z" 또는 "첫째 X, 둘째 Y, 셋째 Z" 형태.
AI는 거의 모든 나열을 세 항목으로 맞추는 습관이 있다. 진짜 분석가는 두 항목으로 끊거나, 넷 이상을 나열하거나, 비대칭 구조를 사용한다.

**통과 기준**: 섹션당(S01, S02, ... 또는 블로그 h2 단위) 삼박자 리스트 ≤ 1개.
**FAIL 시**: 과잉 리스트를 두 항목으로 축약하거나, 비대칭 나열(중요 항목에 2문장, 나머지 한 줄)로 재구성.

### Point 6 — 헤징 과잉 (Excessive Hedging)

**검사**: 불필요한 한정어를 카운트.
금지 대상: *could potentially, may possibly, might arguably, it seems likely that, appears to suggest, in some ways, to a certain extent, relatively speaking, one could argue, it is possible that, there is reason to believe*
인텔리전스 분석에서 불확실성은 **확신도 등급**(HIGH/MEDIUM/LOW)으로 표현하는 것이 정석. 문장 내 빈 헤징은 권위를 약화시킴.

**통과 기준**: 1,000 spoken words당 ≤ 2회. 확신도 등급으로 이미 불확실성을 표시한 섹션에서 추가 헤징 = 0.
**FAIL 시**: 확신이 있으면 단정적으로 진술. 불확실하면 확신도 등급을 명시하고 빈 헤징 삭제.

### Point 7 — 도입부·전환 단조로움 (Opening & Transition Monotony)

**검사**: 각 섹션(S01–S08 또는 블로그 h2) 도입부의 첫 문장 패턴을 수집. 3개 이상의 섹션이 동일한 구조("On [date], [company] announced...")로 시작하면 위반.
또한 섹션 간 전환 패턴이 반복되는지 확인("Meanwhile", "In parallel", "Separately" 등의 동일 전환어 3회 이상).

**통과 기준**: 동일 도입 패턴 3연속 = 0. 동일 전환어 3회 이상 = 0.
**FAIL 시**: 도입부를 다양화 — 수치로 시작, 질문으로 시작, 결론부터 시작(inverted pyramid), 대조로 시작 등. 전환어를 삭제하거나 구조적 연결(이전 섹션 콜백)로 대체.

### Point 8 — 빈 수사 대 실질 분석 (Empty Rhetoric vs. Substance)

**검사**: 두 종류의 진술을 분류.
- **실질 분석**: 구체적 수치 근거, 인과 논리, 비교 데이터, 행위자+행동+결과 구조
- **빈 수사**: "이것은 매우 중요하다", "업계에 큰 파장을 일으킬 것이다", "전례 없는 변화", "역사적 전환점" — 구체성 없이 중요성만 반복

**통과 기준**: 빈 수사 / 실질 분석 비율 ≤ 유형별 한도 (Report ≤ 0.2, Blog ≤ 0.25, NL-Free ≤ 0.3, NL-Pro ≤ 0.2).
**FAIL 시**: 빈 수사를 구체적 근거로 교체하거나 삭제. "전례 없는"은 "2003년 이후 최초" 같은 구체적 비교로.

### Point 9 — 중복 진술 (Redundancy Check)

**검사**: 동일한 분석·주장을 약간 다른 표현으로 반복하는 경우를 탐지.
특히 APA에서 자주 발생하는 패턴:
- S01 Summary에서 한 말을 S03 Lock-in Change에서 동의어로 반복
- S04 6-Month Implications에서 S01 Power Flow의 문장을 거의 그대로 재활용
- 블로그에서 리포트 문장을 표현만 바꿔 복사

인정되는 반복: 의도적 요약 섹션(S08 Watchlist), 다른 관점에서의 재분석.
인정되지 않는 반복: 동일 관점·동일 맥락에서 동의어 치환만으로 같은 말 반복.

**통과 기준**: 비의도적 중복 ≤ 2개 / 파일.
**FAIL 시**: 중복 중 한쪽을 삭제하거나, 새로운 각도(다른 이해관계자, 다른 시간 지평)에서 재분석.

### Point 10 — 수동태·비인칭 과잉 (Passive Voice & Impersonal Overuse)

**검사**: 수동태 문장("it was announced", "has been observed", "is expected to")과 비인칭 주어("It is clear that", "There is a growing consensus") 비율을 측정.
진짜 인텔리전스 분석은 행위자를 명시한다: "NVIDIA unveiled" (능동), "The Pentagon designated" (능동). AI는 행위자를 숨기고 수동태로 작성하는 경향이 강하다.

**통과 기준**: 수동태 비율 ≤ 15% (전체 문장 대비). 비인칭 주어("It is", "There is/are" 도입) ≤ 5%.
**FAIL 시**: 행위자를 주어로 복원하여 능동태로 전환. "It was announced that X will Y" → "X announced Y."

### Point 11 — 한국어 번역 자연성 (KO Translation Naturalness) — _ko 파일만

**검사**: 한국어 파일이 영어 직역투가 아닌 자연스러운 한국어 분석문으로 읽히는지 확인.
위반 패턴:
- 영어 어순 직역: "이것은 X를 의미하는 Y이다" (→ "Y, 즉 X를 뜻한다")
- 과도한 피동: "~되어진다", "~되어질 것이다"
- 명사 나열 번역: "인공지능 인프라 보안 프레임워크 규제 변화" (명사 5연속)
- 영어식 관계절 직역: "~하는 것으로 알려진 X는 ~한 Y를 ~하는 Z이다" (한 문장에 관계절 3중첩)
- 존댓말 일관성: APA 한국어판은 "~입니다/~합니다" 체. "~이다/~한다" 혼용 금지.

**통과 기준**: 직역투 위반 ≤ 3개 / 파일. 존댓말 이탈 = 0.
**FAIL 시**: 한국어 자연어 어순으로 재구성. 피동 → 능동, 명사 나열 → 조사 삽입, 관계절 → 분리 문장.

### Point 12 — 편집 서명 (Editorial Signature)

**검사**: 발행물에 AI가 절대 자발적으로 생성하지 않는 "인간 편집자의 흔적"이 있는지 확인.
기대하는 서명들 (파일당 최소 2개):
- **단언적 판단**: "이 거래는 과대평가다", "이 정책은 실패할 것이다" 등 확신도가 뒷받침된 직접적 판단
- **비대칭 비중 배분**: 3개 이벤트 중 가장 중요한 것에 40% 이상의 분량, 나머지에 짧은 비중
- **독자 직접 호명**: "Pro 구독자라면 주목할 포인트는...", "여기서 한국 투자자가 볼 것은..."
- **반직관적 해석**: 통념과 다른 분석을 근거와 함께 제시
- **콜백/연결**: 과거 리포트 내용을 인용하거나 시리즈 연속성 표시 ("4월 17일자에서 예고한 대로...")

**통과 기준**: 파일당 편집 서명 ≥ 2개.
**FAIL 시**: 가장 적합한 위치에 편집 서명을 추가. 특히 S04(6-Month Implications)와 블로그 결론부에 단언적 판단을 삽입.

---

## 실행 절차

1. 대상 파일 목록 확정 (리포트 _en.md + _ko.md, 블로그 -en.html + -ko.html, 뉴스레터 4종 중 해당 파일)
2. 각 파일에 대해 12개 포인트를 순서대로 검사
3. 각 포인트에서 위반 발견 → 즉시 인라인 수정 → 수정 내용을 로그에 기록
4. 12개 포인트 완료 후 수정된 파일을 저장
5. 결과 로그 출력

**대량 실행 모드**: 파이프라인에서 리포트 2파일 + 뉴스레터 4파일 + 블로그 2파일 = 총 8파일을 검수할 때, 전체를 한 번에 실행하되 파일별 결과를 개별 출력.

---

## Output

```
## APV Results — {filename}
Type: {report | blog | newsletter-free | newsletter-pro}

| # | Point | Result | Details |
|---|-------|--------|---------|
| 1 | AI 관용구 | PASS/FAIL | X instances (limit: Y) |
| 2 | 분석적 관점 | PASS/FAIL | X injections (min: Y) |
| 3 | 구체 데이터 밀도 | PASS/FAIL | X/1000w (min: Y) |
| 4 | 문장 리듬 변화 | PASS/FAIL | X monotone zones |
| 5 | 삼박자 리스트 | PASS/FAIL | X overuse (limit: Y/section) |
| 6 | 헤징 과잉 | PASS/FAIL | X/1000w (limit: 2) |
| 7 | 도입·전환 단조 | PASS/FAIL | X repeated patterns |
| 8 | 빈 수사 비율 | PASS/FAIL | ratio X (limit: Y) |
| 9 | 중복 진술 | PASS/FAIL | X redundancies (limit: 2) |
| 10 | 수동태·비인칭 | PASS/FAIL | passive X%, impersonal Y% |
| 11 | KO 번역 자연성 | PASS/FAIL/N-A | X violations (limit: 3) |
| 12 | 편집 서명 | PASS/FAIL | X signatures (min: 2) |

총점: X/12 PASS
수정 적용: YES/NO
```

FAIL이 하나라도 있으면 수정 후 재실행. 12/12 PASS 확인 후 파이프라인 다음 단계로 진행.

---

## 파이프라인 통합 가이드

APV는 APA 일간 파이프라인의 **품질 게이트**로 사용할 수 있다:

- **Step 2 완료 후**: 리포트 `_en.md` + `_ko.md` → APV 실행 → PASS 후 Step 3(PDF)
- **Step 4 완료 후**: 뉴스레터 4파일 → APV 실행 → PASS 후 Step 5(블로그 MD)
- **Step 6 완료 후**: 블로그 HTML 2파일 → APV 실행 → PASS 후 Step 7 이후

또는 파이프라인 전체 완료 후 일괄 검수:
- Step 12(verify_daily.sh) 이후 APV를 추가 품질 검수로 실행

**verify_daily.sh와의 관계**: verify_daily.sh는 구조·마커·파일 존재·크기 등 **형식적 검증**을 담당한다. APV는 **내용적·문체적 검증**을 담당한다. 둘은 보완 관계이며, 둘 다 통과해야 최종 품질 인증.

---

*APV v1.0 — May 2026. AI Power Atlas Publication QA.*
