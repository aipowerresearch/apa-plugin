---
name: pipeline-runner
description: 일간 전체 파이프라인 13단계 (Step 1~13). 트리거 — "full daily 실행", "13단계 실행", "오늘 파이프라인", "전체 파이프라인", "daily pipeline", "run full daily", "/apa:daily", 또는 사용자가 특정 날짜의 일간 파이프라인을 요청할 때. 날짜를 지정하면 소급 실행도 가능.
---

# Daily Pipeline — 13단계 (절대 규칙)

13단계 전부 필수. 한 단계라도 실패하면 보고 자체 거부 + 수정 후 재실행.

## 인자
- 날짜 (YYYY-MM-DD 또는 자연어; 미지정 시 오늘)
- `--test-mode` (Step 13 업로드 + 뉴스레터 발송 건너뜀, 산출물은 outputs/_test/<date>/로 격리)

## 요일 매핑
| 요일 | 두글자 | 레이어 |
|---|---|---|
| Mon | Mo | L1+L2 |
| Tue | Tu | L3+L4 |
| Wed | We | L5+L6 |
| Thu | Th | L7+L8 |
| Fri | Fr | L9+L10 |
| Sat | Sa | 전체 보완 (Step 9 심층 감사 추가) |
| Sun | Su | Synthesis (주간 PASS 후 발행) |

## Step 0 — 필수 참조 로드 (생략 금지)
- references/scanner/layer-keywords-{en,ko}.md
- references/scanner/source-list-{en,ko}.md
- references/scanner/scanner-supplement.md
- references/framework/key-figures.md
- references/framework/report-spec.md
- references/framework/quality-check.md
- 직전 동일 레이어 source-notes

## 13단계 실행 순서

| Step | 스킬 | 산출물 |
|---|---|---|
| 1 | news-scanner | outputs/sources/{en,ko}/ |
| 2 | report-writer | outputs/reports/{en,ko}/ |
| 3 | pdf-publisher | outputs/pdf/{en,ko,en-ko}/ + web/pdf/{en,ko,en-ko}/ |
| 4 | newsletter-builder | outputs/newsletters/{free,pro}-{en,ko}/ (4종) |
| 5 | blog-converter (MD) | outputs/blog/{en,ko}/ |
| 6 | blog-converter (HTML) | web/blog/posts/ |
| 7 | apv-validator | 리포트 2 + 뉴스레터 4 + 블로그 HTML 2 = 8파일 품질 게이트 |
| 8 | blog-converter (인덱스+nav) | web/blog/index*.html, archive*, intelligence preview, prev/next 갱신 |
| 9 | (소셜 포스트) | outputs/social/YYYY-MM-DD_<DoW>_social.md |
| 10 | archive-manager | outputs/archive-index.md (토요일은 심층 감사 E1~E9 추가) |
| 11 | (웹 인덱스 점검) | 모든 인덱스 페이지 정합성 확인 |
| 12 | verifier | scripts/verify_daily.sh — PASS/TOTAL 보고 (FAIL 시 수정 후 재실행) |
| 13 | uploader | FastComet 또는 설정된 호스트로 rsync (--test-mode 시 건너뜀) |

## Step 7 APV 게이트 (절대 규칙)

Step 6 완료 직후, Step 8(배포) 진입 전에 반드시 `apv-validator` 스킬을 실행한다.

**대상 파일 (8개):**
- `outputs/reports/YYYY-MM-DD_*_daily-report_en.md`
- `outputs/reports/YYYY-MM-DD_*_daily-report_ko.md`
- `outputs/newsletters/free-en-*.html`
- `outputs/newsletters/free-ko-*.html`
- `outputs/newsletters/pro-en-*.html`
- `outputs/newsletters/pro-ko-*.html`
- `web/blog/posts/ai-power-atlas-YYYY-MM-DD-*-en.html`
- `web/blog/posts/ai-power-atlas-YYYY-MM-DD-*-ko.html`

**통과 기준:** 12개 체크포인트 중 10개 이상 PASS. FAIL 항목은 즉시 수정 후 재검사.
**Step 7 FAIL 시:** 해당 파일 재작성 → APV 재실행 → PASS 확인 후 Step 8 진행.

## 완료 보고 형식 (절대 규칙)

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━
AI Power Atlas — {YYYY-MM-DD} 완료
━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Step 1:  소스 노트 — ...
✅ Step 2:  일간 리포트 — _en.md + _ko.md
✅ Step 3:  PDF 리포트 — ...
✅ Step 4:  뉴스레터 — free-ko + free-en + pro-ko + pro-en (4파일)
✅ Step 5:  블로그 MD — ...
✅ Step 6:  블로그 HTML — ...
✅ Step 7:  APV 품질 게이트 — 8파일 검증 PASS
✅ Step 8:  블로그 인덱스 — index.html + index_kr.html + archive × 2 + intelligence
✅ Step 9:  소셜 포스트 — ...
✅ Step 10: 아카이브 인덱스 — archive-index.md 업데이트
✅ Step 11: 웹 인덱스 — intelligence/index.html 갱신
✅ Step 12: 자동 검수 — verify_daily.sh PASS/TOTAL PASS
✅ Step 13: FastComet 업로드 — N개 파일 동기화
━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

이후 "요약" + "주요 파일" 블록 (CLAUDE.md 슬림 버전 참조).
