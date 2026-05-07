# AI Power Atlas — Plugin v2.1.0

10-Layer 권력 흐름 프레임워크 기반 일간/주간/심층분석 인텔리전스 자동 생성·발행 플러그인.
다국어 EN/KO 동시 지원 (향후 JA/ZH/ES/DE/FR/PT/AR 확장 가능). 번역 품질 검수 내장 (10점 척도, 8.0/10 기준선).

## 설치

### Windows
```powershell
.\install.ps1 -RegisterTasks
```

### macOS / Linux
```bash
./install.sh
```

기본 작업 폴더: `~/Downloads/apa/`

## 핵심 명령

| 명령 | 설명 | 주기 |
|---|---|---|
| `/apa:daily` | 일간 전체 파이프라인 11단계 | 매일 07:00 |
| `/apa:daily --test-mode` | 발행 없이 검증만 | 수동 |
| `/apa:weekly` | 주간 종합 (3군데 동시 갱신) | 일요일 07:00 |
| `/apa:analysis` | Deep research 분석 (3000+ 단어, SEO/AEO/GEO) | **수요일 08:00** |
| `/apa:verify` | 자동 검수 단독 실행 | 수동 |
| `/apa:upload` | 범용 SSH/SFTP/rsync 업로드 | 수동 |
| `/apa:kb-update` | 지식 베이스 일간 갱신 | 매일 08:30 |

## 자동 갱신 페이지

**매일** (`/apa:daily`)
- 메인 (`/`, `/index_kr.html`) — SAMPLE INTELLIGENCE 카드
- 인텔리전스 (`/intelligence/`) — Report Structure 8섹션
- 블로그 인덱스 (`/blog/`) — 피처드 1 + 그리드 8 (총 9, 중복 차단) + Deep Analysis 8개
- 블로그 아카이브 (`/blog/archive/`) — 월별 그루핑, 한글 제목 정합성

**일요일** (`/apa:weekly`)
- Weekly (`/weekly/`) — Latest 카드 + Past Issues + PDF 링크
- 블로그 인덱스 — 주간 카드 (gold border)

**수요일** (`/apa:analysis`)
- Analysis (`/analysis/`) — 3000+ 단어 deep research, en+ko 짝
- 블로그 Deep Analysis 카드 갱신

## 번역 품질 안전망 3중

1. **policy** — `references/operations/translation-policy.md` (공통) + `translation-policy-{lang}.md` (언어별)
2. **self-evaluation** — report-writer 스킬 5-Phase 절차, 섹션별 10점 척도
3. **automated check** — verify_daily.sh 영문 단어 비율 ≤ 15% (화이트리스트 제외)

## 다국어 확장

새 언어 추가 시 두 파일만 추가:
- `references/scanner/source-list-<lang>.md`
- `references/scanner/layer-keywords-<lang>.md`
- `references/operations/translation-policy-<lang>.md`

## 라이선스 / 작성자
AI Power Research · https://aipoweratlas.com
