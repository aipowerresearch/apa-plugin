# Newsletter Conversion Guide v2

> 이 파일은 `newsletter-template.html`과 함께 사용됩니다.
> 플러그인 기본 SKILL.md를 보완하는 로컬 오버라이드 가이드입니다.

## v2 변경사항 (2026-03-20)

기존 v1 대비 3가지 추가:

1. **S05 크로스 레이어 인사이트** — APA의 핵심 차별점인 레이어 간 연결 분석
2. **S07 반대 의견** — 소수/반대 의견 1건으로 분석의 깊이감 확보
3. **이벤트별 원문 링크** — 각 S01 이벤트에 T1 소스 링크 1개씩 첨부

## Section Mapping (v2 Full)

| Report Section | Newsletter Block | 비고 |
|---------------|-----------------|------|
| S01 핵심 사건 3 | Hero card × 3 + 원문 링크 | 각 카드에 `📎 소스명 ↗` 링크 추가 |
| S02 권력 이동 | 테이블 (From→To, 강도, 루프) | S03과 병합 |
| S03 피드백 루프 | S02와 병합 + Hot Loop 요약 1줄 | |
| S04 시나리오 업데이트 | 3-row 확률 테이블 (A/B/C) | 이전%→현재% + 이유 |
| **S05 크로스 레이어** | 보라색 배경 박스 1단락 | **v2 신규** |
| S06 신호 강도 | 4-cell indicator grid | |
| **S07 반대 의견** | 회색 인용 박스 (이탤릭) | **v2 신규** |
| S08 내일 주목 신호 | 회색 배경 텍스트 박스 | |

## Source Link Rules

- S01 각 이벤트의 원문 링크는 source-notes.md의 T1 소스에서 가져옴
- 링크 텍스트 형식: `📎 매체명 ↗` (예: `📎 Reuters ↗`)
- URL이 없거나 불확실하면 해당 줄 생략 (빈 링크 금지)

## S05 작성 규칙

- 리포트 S05에서 핵심 cross-layer 연결 1~2문장 추출
- "오늘의 L{N} 신호가 L{M}에 미치는 영향" 프레임으로 작성
- 최대 3줄

## S07 작성 규칙

- 리포트 S07에서 가장 의미 있는 반대 의견 1건 선택
- 인용 형식으로 표시 (이탤릭)
- 출처 명시 필수

## 예상 분량

v2 기준 스크롤 약 3~4회 (모바일), 데스크탑에서 약 1.5페이지. "짧지만 밀도 높다" 인상 목표.

## 뉴스레터 → 블로그 연결 (v2.1 추가)

### Blog CTA 블록
- S08 아래, Footer 위에 위치
- 해당 일자의 블로그 포스트 URL을 KO/EN 모두 제공
- 변수: `{{BLOG_HEADLINE}}`, `{{BLOG_URL_KO}}`, `{{BLOG_URL_EN}}`
- URL 패턴: `https://aipoweratlas.com/blog/posts/ai-power-atlas-YYYY-MM-DD-lXlY.html` (KO)
- URL 패턴: `https://aipoweratlas.com/blog/posts/ai-power-atlas-YYYY-MM-DD-lXlY-en.html` (EN)

### 파이프라인 순서
1. report 생성 → 2. blog 변환 (URL 확정) → 3. newsletter 변환 (blog URL 삽입)
- 뉴스레터가 블로그 URL을 참조하므로, 블로그가 먼저 완성되어야 함
- full-daily 파이프라인에서 이 순서가 보장되어야 함

## Template Location

`APA/references/newsletter-template.html` (v2.1)

## 기존 SKILL.md와의 관계

플러그인 기본 SKILL.md의 규칙(인라인 CSS, 600px, 테이블 레이아웃, Subject Line 등)은 그대로 유효합니다.
이 가이드는 섹션 매핑과 콘텐츠 범위만 확장합니다.
