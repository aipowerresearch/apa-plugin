# Step 4-1 — 무료 뉴스레터 (NL-01) 작성 프롬프트

## 역할
NL-01 Free Daily Design B-2 Slate-Indigo 표준 템플릿을 복사해 오늘 콘텐츠로 본문만 교체. 무료 구독자 대상의 간단 요약 + Pro 업그레이드 CTA 구조.

## 입력
- 영어 리포트: `{{EN_REPORT_PATH}}` (S01 3 이벤트 사용)
- 한국어 리포트: `{{KO_REPORT_PATH}}` (S01 3 이벤트 한국어 + S09 한국 시장)
- 표준 템플릿 KO: `references/templates/newsletter/STANDARD_newsletter_free-ko.html`
- 표준 템플릿 EN: `references/templates/newsletter/STANDARD_newsletter_free-en.html`

## 출력 (반드시 2파일)
- `outputs/newsletters/{{DATE}}_{{DOW_KR}}_newsletter_free-ko.html`
- `outputs/newsletters/{{DATE}}_{{DOW_KR}}_newsletter_free-en.html`

## 절대 시그니처 (검수 통과용)

각 파일이 반드시 갖춰야 할 마커:

| 항목 | 값 |
|------|----|
| 1행 주석 | `<!-- APA TEMPLATE: NL-01 Free Daily ({KO|EN}) · Design B-2 Slate-Indigo · v3 -->` |
| 무료 배지 | `>무료</` (KO) 또는 `>FREE</` (EN) |
| Pro 업그레이드 CTA | `Pro로 업그레이드` (KO) 또는 `Upgrade to Pro` (EN) |
| Free 푸터 | `무료 구독자로 수신하고 있습니다` (KO) 또는 `Free subscriber` (EN) |
| 파일 크기 | 8–20KB 범위 (표준 ~14KB) |

## 콘텐츠 구조 (절대 준수 — STANDARD_newsletter_free-ko.html 그대로)

1. **헤더 (Slate-Indigo 그라데이션)**
   - 무료 배지 + Issue # + 날짜 + 요일 + 집중 레이어
   - 메인 타이틀 (오늘 블로그 포스트 URL 링크)
   - 서브타이틀 (3 이벤트 요약 1줄)

2. **S01 3 이벤트 카드** (각 카드 emerald/blue/dark_em 색상)
   - 레이어 태그 (예: L2 + L1)
   - 제목 (블로그 링크)
   - 2문장 요약
   - 하단 라벨: "임팩트 [N] · 권력 [+/-] · [horizon] · [feedback loop]"

3. **시나리오 확률 막대** (A 연속 / B 가속 / C 단절 — 퍼센트만 공개)

4. **내일 프리뷰** (1줄)

5. **Pro 업그레이드 CTA** (e04060 색상 박스)

6. **푸터** (구독 취소·아카이브 링크)

## 변수 치환 가이드

표준 템플릿을 복사한 뒤 다음 변수 교체:

| 변수 | 출처 |
|------|------|
| `2026-04-23` (날짜) | `{{DATE}}` |
| `목요일` (요일) | `{{DOW_KR}}요일` (또는 EN: `Thursday`) |
| `L7 + L8 · 자본 + 규제` (레이어) | `{{LAYER_FOCUS_FRIENDLY}}` |
| `113` (Issue #) | `{{ISSUE_NUM}}` (계산: 2026-04-25는 #115, 매일 +1) |
| `피지컬 AI 2축…` (메인 타이틀) | 오늘 블로그 KO 헤드라인 |
| `Prometheus $10B…` (서브타이틀) | 3 이벤트 1줄 요약 |
| `ai-power-atlas-2026-04-23-l7l8-ko` (블로그 슬러그) | `ai-power-atlas-{{DATE}}-{{LAYER_SLUG}}-ko` |

## 자가 검수 체크리스트

- [ ] 2개 파일 (KO + EN) 모두 생성
- [ ] NL-01 주석 1행에 존재
- [ ] Design B-2 명시
- [ ] 무료/FREE 배지 존재
- [ ] Pro 업그레이드 CTA 존재
- [ ] 파일 크기 8–20KB

## 산출 후

`scripts/verify_daily.sh {{DATE}}` 의 `Free 시그니처` 체크 PASS 확인.
