# Step 8 — 소셜 포스트 작성 프롬프트

## 역할
오늘 리포트의 핵심 이벤트를 Twitter/X (영어 5개 + 한국어 3개) + LinkedIn (영어/한국어 1개씩) 포맷으로 변환.

## 입력
- 영어 리포트: `{{EN_REPORT_PATH}}`
- 한국어 리포트: `{{KO_REPORT_PATH}}`

## 출력
파일: `outputs/social/{{DATE}}_{{DOW_KR}}_social.md`

## 표준 구조

```markdown
---
date: {{DATE}}
day: {{DOW_KR}} ({{DOW_EN}})
focus: {{LAYER_FOCUS}}
report: {{REPORT_FILENAME}}
---

# AI Power Atlas — Social Posts · {{DATE}} ({{DOW_KR}})

## Twitter / X — English (5)

### 1. Lead
[리드 포스트 — 오늘 가장 큰 사건의 핵심 1–2 문장 + 정량 anchor + URL aipoweratlas.com]

### 2. Event 2
[Event 2 핵심 정량 anchor + 1줄 함의 + 2–3 핵심 숫자]

### 3. Event 3
[Event 3 핵심 정량 anchor + 1줄 함의]

### 4. Contrarian
[일반적 해석에 반박하는 구조적 관점 — APA의 차별화 포인트]

### 5. System Signal
[3 이벤트가 만드는 시스템 신호 종합 + 6개월 시사점 1줄 + URL]

## Twitter / X — Korean (3)

### 1. Lead
[리드 포스트 한국어 — 핵심 정량 anchor + 1줄 함의 + URL]

### 2. Event 2 또는 3
[가장 중요한 보조 사건 한국어 요약]

### 3. System
[시스템 신호 한국어 — 두 스택/락인/감원 등 구조적 변화 1줄]

## LinkedIn — English (~150 words)

[150단어 본문 — 3 이벤트 종합 분석 + 6개월 함의 + 확신도 + URL aipoweratlas.com]

## LinkedIn — Korean (~200자)

[200자 본문 — 3 이벤트 종합 분석 + 6개월 함의 + 확신도 + URL aipoweratlas.com / intesol.kr]
```

## 작성 원칙

1. **이모지 없음**: 분석적 톤 유지, 가벼운 감정 표현 금지
2. **수치 anchor 우선**: 모든 포스트에 정량 수치 1개 이상 (벤치마크·금액·인원·%)
3. **차별화**: 일반 보도와 다른 APA의 구조적 해석 (락인·풀스택·feedback loop 등)
4. **링크**: 모든 메인 포스트 끝에 `aipoweratlas.com` 또는 `intesol.kr` 추가
5. **글자 수 제약**:
   - X 영문: 280자 이하 (본문 200자 + URL/여백)
   - X 한국어: 280자 이하 (한글 1자 ≈ X에서 2자)
   - LinkedIn 영문: ~150 words
   - LinkedIn 한국어: ~200자

## 자가 검수 체크리스트

- [ ] Twitter/X EN 5개
- [ ] Twitter/X KO 3개
- [ ] LinkedIn EN 1개 (150 words)
- [ ] LinkedIn KO 1개 (200자)
- [ ] 이모지 없음
- [ ] 모든 메인 포스트에 URL 포함

## 산출 후

Step 9 (아카이브 인덱스 업데이트)로 진행.
