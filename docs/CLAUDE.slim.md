# AI Power Atlas — Workspace Conventions (slim)

이 폴더는 `apa` 플러그인의 데이터·산출물 보관소. 핵심 규칙만 자동 로드용으로 유지하며,
세부 사양은 플러그인 SKILL이 트리거 시 자동 로드한다.

---

## 1. 응답 규칙 (절대)

- **존댓말 사용**. 반말 어미("~이다 / ~한다 / ~해라 / ~야") 금지. 모든 한국어 종결은 "~입니다 / ~합니다 / ~해요" 계열.
- 어조: 엄정 중립. 과도한 긍정 표현 자제.
- 답변: 핵심 위주, 간결, 중복 없음. 사용자가 "더 상세히"를 요청할 때만 확장.

## 2. 작업 폴더 구조 (절대)

```
apa/
├── CLAUDE.md         (이 파일, 슬림)
├── outputs/          (모든 산출물)
├── web/              (웹사이트 동기화 대상)
├── ssh/              (FastComet/Hetzner 등 SSH 키)
├── _archive/         (영구 보존)
└── _quarantine/     (임시 격리, 정기 삭제)
```

산출물 파일명 패턴:
```
YYYY-MM-DD_<DoW>_<type>_<lang>.<ext>
DoW: Mo Tu We Th Fr Sa Su
lang: en | ko | en-ko (PDF 결합본만)
예: 2026-05-01_Fr_daily-report_en.md
    2026-05-01_Fr_daily-report_en-ko.pdf
```

## 3. 파이프라인 호출

| 작업 | 명령 |
|---|---|
| 일간 전체 | `/apa:daily` (오늘) 또는 `/apa:daily 2026-04-30` (소급) |
| 일간 테스트 | `/apa:daily --test-mode` (산출물 격리, 발행 없음) |
| 단계별 | `/apa:scan`, `/apa:report`, `/apa:newsletter`, `/apa:blog`, `/apa:pdf` |
| 주간 | `/apa:weekly` (일요일) |
| 검수 | `/apa:verify YYYY-MM-DD` |
| KB 갱신 | `/apa:kb-update` |
| 업로드 | `/apa:upload` (FastComet 기본; `--target=hetzner-prod` 등 가능) |

## 4. 11단계 파이프라인 보고 형식 (절대)

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━
AI Power Atlas — {YYYY-MM-DD} 완료
━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Step 1: 소스 노트 — ...
... (Step 2~12 모두)
✅ Step 12: 자동 검수 — verify_daily.sh PASS/TOTAL PASS
━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

이후 "요약" 한 단락(3~5문장) + "주요 파일" 4개 항목(computer:// 절대경로).

## 5. 단축 트리거

다음 문구 중 하나가 들어오면 직전 일간 결과를 위 보고 형식으로 재출력:
- "정돈 출력", "정돈해서 출력", "포맷대로 출력", "오늘 결과 정돈", "재출력"

## 6. 절대 금지

- `_v1.md`(병기) 리포트 생성
- 뉴스레터 본문 직전일 회귀 (D-2 키워드 ≥ 4회 등장 시 미교체 의심)
- 플러그인 references/ 외부에 운영 파일 추가 (작업 폴더는 산출물 전용)
- Step 11/12 생략 (업로드·검수 미실행 시 파이프라인 미완료)
