---
name: weekly-synthesizer
description: 주간 종합 리포트 + 시나리오 트래커 + Weekly 페이지 3군데 동시 갱신. 트리거 — "주간", "weekly synthesis", "Sunday report", "/apa:weekly".
---

한 주(월~토) daily 리포트 4건 이상을 누적·집계하여 주간 종합 생성 + Weekly 페이지 3군데 동시 업데이트.

## 입력
- `outputs/reports/{en,ko}/2026-WNN_*_daily-report_*.md` (4건+)
- references/framework/shift-tracker.md
- references/operations/publishing-schedule.md
- references/operations/translation-policy.md + translation-policy-ko.md

## Phase 1: 주간 리포트 작성
- `outputs/reports/weekly/{en,ko}/YYYY-WNN_weekly-synthesis_<lang>.md`
- KO 작성 시 translation-policy 절차 동일 적용 (5-Phase: 작성→번역→자체평가→재번역→로그)

## Phase 2: 주간 PDF 3종
- `outputs/pdf/en/YYYY-WNN_weekly-report_en.pdf`
- `outputs/pdf/ko/YYYY-WNN_weekly-report_ko.pdf`
- `outputs/pdf/en-ko/YYYY-WNN_weekly-report_en-ko.pdf`
- `web/pdf/{en,ko,en-ko}/`로도 복사

## Phase 3: Weekly 페이지 3군데 동시 갱신 (절대)

### 영역 1 — Latest Issue 카드 (`web/weekly/index.html`, `index_kr.html`)
- "Latest · YYYY-WNN" 배지 갱신
- 제목 (KO 페이지는 KO 원문 제목)
- PDF 링크 → 새 PDF URL (`/pdf/en-ko/YYYY-WNN_weekly-report_en-ko.pdf` 등)
- 발행일

### 영역 2 — Past Issues archive-grid (같은 두 파일 안)
- 직전 주를 archive-grid로 이동
- 카드 형태로 추가 (제목 + 날짜 + PDF 링크)

### 영역 3 — 블로그 인덱스 주간 카드 (`web/blog/index.html`, `index_kr.html`)
- 주간 카드 추가 (gold border 스타일: `style="border-color:var(--gold);border-width:1px;"`)
- 일간 카드보다 위에 배치
- 위치: 피처드 아래, 그리드 위 (또는 별도 "WEEKLY SYNTHESIS" 섹션)

## Phase 4: 주간 블로그 포스트
- MD: `outputs/blog/{en,ko}/YYYY-WNN_weekly-blog_<lang>.md`
- HTML: `web/blog/posts/ai-power-atlas-YYYY-MM-DD-YYYY-wNN-weekly-<lang>.html`
- 8요소 모두 포함 (theme-toggle, post-nav 등)

## Phase 5: 시나리오 트래커 갱신
references/framework/shift-tracker.md 의 시나리오 가중치 + 피드백 루프 상태 갱신.

## 동작 조건
일요일 자동(`apa-weekly` cron) 또는 수동 호출. 평일 호출 시 누적 부족 경고.

## 자동 검증
- weekly index 2개 + blog index 2개 = 4개 파일에 새 주간 카드 존재
- PDF 3종 모두 ≥ 200KB
- KO weekly 리포트 translation-policy 자체평가 8.0/10 이상
