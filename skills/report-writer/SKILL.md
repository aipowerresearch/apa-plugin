---
name: report-writer
description: 8섹션 일간 리포트 생성 (EN 원문 → KO 충실 번역 + 한국 시장 보강 + 품질 검수). 트리거 — "리포트 생성", "일간 리포트", "generate report", "/apa:report", 파이프라인 Step 2 자동 호출.
---

오늘 source-notes를 입력으로 받아 8섹션 일간 리포트를 EN/KO 두 파일로 작성한다.

## 절대 규칙 (Option B)
- **EN 먼저 완전 작성** → KO는 영어 원문의 충실 번역 (요약·축약 금지)
- KO에는 추가로 한국 시장 보강 정보 (S09 또는 S01 인라인 블록)
- `_v1.md`(병기) 파일 **생성 금지** — `_en.md` + `_ko.md` 2개만
- 메인 타깃: 북미·영어권 Pro 구독자

## 입력
- `outputs/sources/en/YYYY-MM-DD_<DoW>_source-notes_en.md`
- `outputs/sources/ko/YYYY-MM-DD_<DoW>_source-notes_ko.md`
- references/framework/report-spec.md (Impact/Power Score, Confidence)
- references/framework/quality-check.md
- references/framework/key-figures.md
- **references/operations/translation-policy.md** (한국어 번역 정책 — 필수 준수)
- **references/knowledge-base/feedback_context.md** (KB 피드백 컨텍스트 — §3-0 규칙 적용)

## 8섹션 구조
S01 핵심 이벤트 3개 (Layer/Signal/Impact/Power Flow/Feedback Loop/Summary/Source) ·
S02 권력 이동 신호 · S03 락인 변화 · S04 6개월 시사점 ·
S05 전략 조정 · S06 Map v3 지표 · S07 피드백 루프 · S08 내일 주목 신호

## 산출물
- `outputs/reports/en/YYYY-MM-DD_<DoW>_daily-report_en.md`
- `outputs/reports/ko/YYYY-MM-DD_<DoW>_daily-report_ko.md`

---

---

## §3-0 피드백 컨텍스트 주입 (Phase 1 시작 전 필수)

Phase 1(EN 원문 작성) 시작 **전**, `references/knowledge-base/feedback_context.md`를 읽고
아래 4개 항목을 리포트 작성에 반영한다. 파일이 없으면 이 단계를 건너뛴다.

| 항목 | 적용 방식 |
|------|-----------|
| **Hot Layers** | S01 이벤트 선정 가중치로 활용 (스케줄 기반 레이어 충돌 시 스케줄 우선) |
| **Recurring Entities** | S01 Power Flow에서 해당 엔티티 언급 시 이전 맥락 한 줄 명시 |
| **Open S08 Signals** | 오늘 S01 이벤트와 연결되는 미결 신호에 `*(S08 signal from YYYY-MM-DD realized)*` 주석 추가 |
| **Power Shift Direction** | S02 작성 시 최근 방향 연속성 또는 단절 여부를 명시 |

> 우선순위: 이 §3-0 규칙은 입력 목록 순서보다 **우선** 적용된다.

## 작성 절차 (절대 순서)

### Phase 1: EN 원문 작성
8섹션을 영어로 완결되게 작성. 메인 타깃 독자(북미 Pro 구독자) 기준 자연스러운 native 영어.

### Phase 2: KO 1차 번역
references/operations/translation-policy.md 준수:
- 한글 번역 가능 용어는 모두 한글로 (예: "구현", "프레임워크", "인프라", "생태계")
- 고유명사·약어·기술 용어 중 한글 번역 불명확한 것만 영어 허용
- 직역체 금지 ("이는 ~을 의미합니다", "그것은 ~합니다" 등)
- 격식체 종결 어미 일관 (~입니다/~합니다)
- 한국 시장 보강(S09 또는 S01 인라인) 추가

### Phase 3: 자체 품질 평가 (필수, 생략 금지)
번역 직후 섹션별로 10점 척도로 자체 평가:

| 항목 | 배점 |
|---|---|
| 충실성 (Fidelity) | 3 |
| 자연스러움 (Fluency) | 3 |
| 용어 적절성 (Term Appropriateness) | 2 |
| 문법·맞춤법 (Grammar) | 1 |
| 톤 일관성 (Tone Consistency) | 1 |

**기준선: 8.0/10**

평가 결과를 다음 형식으로 KO 파일 말미에 기록 (HTML 주석으로 숨김):

```markdown
<!--
## 번역 품질 자체 평가 — YYYY-MM-DD

| 섹션 | 충실 | 자연 | 용어 | 문법 | 톤 | 합계 | 판정 |
|------|------|------|------|------|----|------|------|
| S01 Event 1 | 3 | 3 | 2 | 1 | 1 | 10.0 | PASS |
| S01 Event 2 | 3 | 2 | 1 | 1 | 1 | 8.0 | PASS |
| S02 | 3 | 2 | 2 | 1 | 1 | 9.0 | PASS |
| S03 | 3 | 1 | 1 | 1 | 1 | 7.0 | FAIL → 재번역 |
| ... |

전체 평균: X.X / 10
-->
```

### Phase 4: 재번역 (FAIL 섹션)
8점 미만 섹션 식별 → 감점 사유 식별 → 재번역.
재평가 후 8점 이상 확인. 모든 섹션 PASS까지 반복.

### Phase 5: 로그 (6점 미만 발생 시)
6점 미만 섹션이 1개라도 있었으면 `outputs/_logs/translation-log.md`에 append:
```
## YYYY-MM-DD — translation issues
- S03 첫 평가 5.5/10 (사유: 직역체 + 영어 용어 6개 미번역)
- 재번역 후 8.5/10 PASS
- 패턴: "implications" → "시사점" 일관 적용 필요
```

---

## 자동 검수 (verify_daily.sh)
파이프라인 Step 12에서 다음 검사:
1. 이벤트 개수 일치 (S01 Event 1·2·3)
2. 주요 % 수치 일치율 ≥ 90%
3. 핵심 기업·제품명 일치율 ≥ 90%
4. KO/EN 문자 수 비율 ≥ 0.45 (한글 음절 밀도 보정)
5. **KO 본문 영문 단어 비율 ≤ 15% (화이트리스트 제외)** ← 신규 추가
