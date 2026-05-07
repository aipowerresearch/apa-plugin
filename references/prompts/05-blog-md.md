# Step 5 — 블로그 마크다운 작성 프롬프트

## 역할
오늘 리포트의 핵심 3 이벤트와 6개월 시사점을 블로그 포스트 형식으로 재구성. SEO frontmatter + 도입부 + 4–6 h2 섹션 + 6개월 함의 결론 + CTA.

## 입력
- 영어 리포트: `{{EN_REPORT_PATH}}`
- 한국어 리포트: `{{KO_REPORT_PATH}}`

## 출력 (2파일)
- `outputs/blog/{{DATE}}_{{LAYER_SLUG}}_blog_ko.md`
- `outputs/blog/{{DATE}}_{{LAYER_SLUG}}_blog_en.md`

## 표준 구조

### Frontmatter (YAML)

```yaml
---
title: "[메인 타이틀] — AI Power Atlas {{DATE}} ({{LAYER_FOCUS_FRIENDLY}})"
date: {{DATE}}
layers: [{{LAYER_LIST}}]   # 예: [L1, L2, L5, L7, L8, L10]
tags: [{{TAGS}}]            # 핵심 기업·제품·인물·사건 태그
summary: "[3–4문장 요약 — SEO meta description으로 사용]"
---
```

### 본문 구조 (KO 예시)

```markdown
# [한글 메인 타이틀]

**{{DATE}} ({{DOW_KR}}) | {{LAYER_FOCUS_KR}}**

[도입 단락 — 오늘 3 이벤트가 무엇이고 왜 의미 있는지 1단락 5–6문장]

## S01 핵심 사건

### 1. [Event 1 한글 제목]

[Event 1 본문 — 영어 리포트 Summary + Power Flow 결합. 4–6문장. 정량 수치 5개 이상 포함]
**Impact 5 · +N {entity} / -N {entity} · {feedback loop}**

### 2. [Event 2 한글 제목]
...

### 3. [Event 3 한글 제목]
...

## 락인 변화

[S03 한국어 본문 — 영어 리포트 Lock-in Change 섹션 충실 번역, 4–6문장]

## 6개월 시사점

[S04 한국어 본문 — 영어 리포트 6-Month Implications 섹션 충실 번역, 4–6문장. 끝에 확신도 포함]

## 내일의 관전 포인트

- **[Watchpoint 1 제목]** — [1문장]
- **[Watchpoint 2 제목]** — [1문장]
- **[Watchpoint 3 제목]** — [1문장]

---

**구독하세요** — AI Power Atlas는 매일 레이어별로 AI가 권력 구조를 어떻게 재편하는지 추적합니다: aipoweratlas.com

*이 포스트는 AI Power Atlas L1–L10 프레임워크의 일부입니다. 오늘의 집중: {{LAYER_FOCUS_FRIENDLY}}.*
```

EN 버전은 동일 구조로 영어 본문 작성 (영어 리포트의 Summary/Power Flow/S03/S04를 그대로 사용).

## 작성 원칙

1. **재구성, 단순 복붙 아님**: 리포트 8섹션 → 블로그 4–6 h2로 재구성. 구조적 정보 손실 없이 가독성 우선.
2. **SEO 친화적 제목**: 주요 키워드 (기업명·제품명·핵심 수치) 포함
3. **frontmatter summary**: 150–200자 — Google snippet으로 표시
4. **링크**: 본문 안에 1차 출처 인라인 링크 1–2개 (블로그가 가치 있는 hub로 보이도록)

## 자가 검수 체크리스트

- [ ] frontmatter YAML 유효 (`---`로 감싸기)
- [ ] title·date·layers·tags·summary 5개 키 모두 존재
- [ ] h2 섹션 4–6개
- [ ] KO/EN 두 파일 모두 생성
- [ ] EN 본문 한글 비율 < 5%, KO 본문 한글 비율 > 25%

## 산출 후

Step 6 (블로그 HTML 변환)으로 진행. 본 마크다운이 HTML 변환의 input.
