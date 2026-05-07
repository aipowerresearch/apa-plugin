# Web Update Targets — 매일 갱신 페이지

> blog-converter 스킬이 daily 파이프라인 Step 7에서 갱신해야 할 웹 페이지 목록.

## 매일 갱신 (daily 파이프라인 Step 7)

| 페이지 | EN 파일 | KO 파일 | 갱신 영역 |
|---|---|---|---|
| 메인 | `web/index.html` | `web/index_kr.html` | SAMPLE INTELLIGENCE 카드 (오늘 Event 1) + 날짜 |
| 인텔리전스 | `web/intelligence/index.html` | `web/intelligence/index_kr.html` | 날짜 헤더 + Report Structure 8섹션 카드 |
| 블로그 인덱스 | `web/blog/index.html` | `web/blog/index_kr.html` | 피처드 1 + 그리드 8 (총 9, 중복 차단) + Deep Analysis 8 |
| 블로그 아카이브 | `web/blog/archive/index.html` | `web/blog/archive/index_kr.html` | 월별 그루핑, 최신 맨 위, KO 제목 정합성 |

## 주간 갱신 (weekly-synthesizer)

| 페이지 | EN 파일 | KO 파일 | 갱신 영역 |
|---|---|---|---|
| Weekly | `web/weekly/index.html` | `web/weekly/index_kr.html` | Latest 카드 + Past Issues archive-grid + PDF 링크 |
| 블로그 인덱스 | (위와 동일) | | 주간 카드 추가 (gold border) |

## 10일 1회 → 주간 갱신 (analysis-publisher, 매주 수요일)

| 페이지 | EN 파일 | KO 파일 | 갱신 영역 |
|---|---|---|---|
| Analysis 인덱스 | `web/analysis/index.html` | `web/analysis/index_kr.html` | 새 카드 맨 위 추가, "Coming Soon" 1개 제거 |
| 블로그 Deep Analysis | (블로그 인덱스 안) | | Deep Analysis 8개 영역 갱신 |

## 변경 없음 (정적 페이지)

- `web/about/`, `web/layers/`, `web/legal/` — 콘텐츠 변경 시 수동
- ~~`web/courses/`~~ — **사이트에 포함 안 함** (사용자 결정)
- `web/pricing` 영역 (메인 페이지 내 통합) — 정책 변경 시 수동

## 자동 검증 (verify_daily.sh)
모든 daily 갱신 페이지에 오늘 날짜 (`YYYY-MM-DD` 또는 한글 표기) 존재 여부 확인.
