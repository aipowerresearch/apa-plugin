# Step 4-2 — Pro 뉴스레터 (NL-02) 작성 프롬프트

## 역할
NL-02 Pro Daily Design C-5 Gold+Slate 표준 템플릿을 복사해 오늘 8섹션 풀 분석으로 본문 교체. Pro 구독자 대상 — 프리 대비 3배 분량 + PDF 링크 + 풀 시나리오 분석.

## 입력
- 영어 리포트 풀텍스트: `{{EN_REPORT_PATH}}`
- 한국어 리포트 풀텍스트 (S09 포함): `{{KO_REPORT_PATH}}`
- PDF 링크: `https://aipoweratlas.com/pdf/{{DATE}}_daily-report.pdf`
- 표준 템플릿 KO: `references/templates/newsletter/STANDARD_newsletter_pro-ko.html`
- 표준 템플릿 EN: `references/templates/newsletter/STANDARD_newsletter_pro-en.html`

## 출력 (반드시 2파일)
- `outputs/newsletters/{{DATE}}_{{DOW_KR}}_newsletter_pro-ko.html`
- `outputs/newsletters/{{DATE}}_{{DOW_KR}}_newsletter_pro-en.html`

## 절대 시그니처

| 항목 | 값 |
|------|----|
| 1행 주석 | `<!-- APA TEMPLATE: NL-02 Pro Daily ({KO|EN}) · Design C-5 Gold+Slate (readable) · v5 -->` |
| PRO 배지 | `>PRO</` HTML span |
| Pro 에디션 라벨 | `Pro 에디션` (KO) / `Pro Edition` (EN) |
| Pro 푸터 | `Pro 구독자로 수신하고 있습니다` (KO) / `Pro subscriber` (EN) |
| PDF 링크 | `/pdf/{{DATE}}_daily-report.pdf` 정확한 당일 날짜 포함 |
| 파일 크기 | ≥ 25KB (표준 ~36KB) |

## 콘텐츠 구조 (절대 준수)

1. **Gold top rule + Header band** (Gold #c9a84c + Slate #2d3748)
   - PRO 배지 + Issue # + 날짜 + 요일 + 집중 레이어
   - Theme band: Italic Georgia 메인 타이틀 + 서브타이틀

2. **S01 Three Key Events** (3 이벤트, 각 5–7문장 풀 분석)
   - 레이어 태그
   - 제목 (블로그 링크)
   - 5–7문장 본문 (영어 리포트 Summary + Power Flow + Feedback Loop 결합)
   - 하단 라벨: 임팩트·권력·horizon·feedback loop

3. **S03 Cross-Layer Cascade** (3개 이벤트가 만드는 자기 강화 연쇄 분석, 200–400자)

4. **S04 Stakeholder Power Shift** (3축 권력 이동 분석)

5. **S05 Scenario Sensitivity** (A 연속 / B 가속 / C 단절 — 퍼센트 + 각 시나리오 1–2문장 내러티브)

6. **S06 WoW Delta** (주간 변화량 — 어떤 신호가 1단계 격상/하락했는지)

7. **S07 6-Month Outlook** (3가지 6개월 구조 전망 + 확신도)

8. **S08 Signal Watch** (내일 3가지 관전 포인트 + 관찰 엔티티)

9. **Tomorrow + PDF box** (내일 집중 레이어 + PDF 다운로드 링크)

10. **Footer** (Gold rule + 푸터 라인)

## 변수 치환

| 변수 | 출처 |
|------|------|
| `2026-04-23` (날짜) | `{{DATE}}` |
| `목요일/Thursday` (요일) | `{{DOW_KR/EN}}` |
| `L7 + L8` (레이어) | `{{LAYER_FOCUS}}` |
| `113` (Issue #) | `{{ISSUE_NUM}}` |
| `pdf/2026-04-23_daily-report.pdf` | `pdf/{{DATE}}_daily-report.pdf` |
| `ai-power-atlas-2026-04-23-l7l8-ko` (블로그 슬러그) | `ai-power-atlas-{{DATE}}-{{LAYER_SLUG}}-ko` |
| 메인 타이틀·서브타이틀·3 이벤트 본문·시나리오·6개월 전망 등 | 오늘 EN/KO 리포트에서 추출 |

## 작성 톤

- **분석 깊이**: Free의 3배. 단순 사실 보도가 아니라 "이 사건이 왜 권력 구조를 바꾸는가" 해석
- **수치 anchor**: 각 이벤트 카드에 정량 anchor 5개 이상
- **편집 주관**: APA 프레임워크(L1–L10, 6 feedback loops, 권력 이동) 사용한 일관된 해석

## 자가 검수 체크리스트

- [ ] 2개 파일 (KO + EN) 모두 생성
- [ ] NL-02 주석 1행에 존재
- [ ] Design C-5 명시
- [ ] PRO 배지 존재 (`>PRO</`)
- [ ] PDF 링크에 당일 날짜 정확히 포함
- [ ] 파일 크기 ≥ 25KB
- [ ] S01–S08 풀 8섹션 본문 모두 작성
- [ ] 3 이벤트 각 5–7문장 분량

## 산출 후

`scripts/verify_daily.sh {{DATE}}` 의 `Pro 시그니처` 체크 PASS 확인. Step 5 (블로그 MD)로 진행.
