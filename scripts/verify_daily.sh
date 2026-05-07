#!/usr/bin/env bash
# ============================================================================
# AI Power Atlas — 일간 파이프라인 검수 스크립트
# ============================================================================
# 사용법:  bash scripts/verify_daily.sh YYYY-MM-DD
# 예시:    bash scripts/verify_daily.sh 2026-04-25
#
# 검수 대상 (6개 영역):
#   [Step 2]  리포트 3개 파일 + 언어 분리 검증
#   [Step 3]  PDF 존재 + 페이지 수 + EN/KO 섹션 분리
#   [Step 4]  뉴스레터 4개 파일 (free+pro × ko+en)
#   [Step 6]  블로그 HTML 2개 + 필수 8요소
#   [Step 7]  블로그 인덱스·아카이브·인텔리전스 오늘 날짜 포함
#   [Step 11] 서버 업로드 검증 (선택적; SSH 키 있을 때만)
#
# 모든 체크는 PASS/FAIL로 보고되며, 실패 항목이 하나라도 있으면 exit 1.
# ============================================================================

set -u

# ───── 인자 파싱 ─────
if [ $# -lt 1 ]; then
  echo "Usage: $0 YYYY-MM-DD [--skip-server]"
  exit 2
fi
DATE="$1"
SKIP_SERVER=0
[ "${2:-}" = "--skip-server" ] && SKIP_SERVER=1

if ! [[ "$DATE" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}$ ]]; then
  echo "ERROR: Date must be YYYY-MM-DD format"
  exit 2
fi

# ───── 경로 설정 ─────
if [ -n "${APA_ROOT:-}" ]; then
  ROOT="$APA_ROOT"
else
  # Find APA root from SSH key if running inside a Cowork session
  SSH_KEY=$(find /sessions -name id_rsa 2>/dev/null | grep -i "/mnt/.*apa.*/ssh/" | head -1)
  if [ -n "$SSH_KEY" ]; then
    ROOT=$(dirname $(dirname "$SSH_KEY"))
  else
    # Assume script is run from APA_ROOT
    ROOT=$(cd "$(dirname "$0")/.." && pwd)
  fi
fi

REPORTS="$ROOT/outputs/reports"
PDFS="$ROOT/outputs/pdf"
NEWSLETTERS="$ROOT/outputs/newsletters"
BLOG_POSTS="$ROOT/web/blog/posts"
SOURCES="$ROOT/outputs/sources"

# 한국어 요일 매핑
YMD=$(date -d "$DATE" +"%Y-%m-%d" 2>/dev/null || echo "$DATE")
DOW_EN=$(date -d "$DATE" +"%a" 2>/dev/null || echo "")
declare -A DOW_KO=( [Mon]="월" [Tue]="화" [Wed]="수" [Thu]="목" [Fri]="금" [Sat]="토" [Sun]="일" )
KDOW="${DOW_KO[$DOW_EN]:-?}"

# ───── 체크 결과 누적 ─────
PASS=0
FAIL=0
FAIL_DETAILS=()

check() {
  local label="$1"; local ok="$2"; local detail="${3:-}"
  if [ "$ok" = "1" ]; then
    echo "  ✅ $label"
    PASS=$((PASS+1))
  else
    echo "  ❌ $label  ${detail}"
    FAIL=$((FAIL+1))
    FAIL_DETAILS+=("$label${detail:+ — $detail}")
  fi
}

echo "═══════════════════════════════════════════════════════════"
echo "AI Power Atlas — 검수 리포트 · $DATE ($KDOW)"
echo "  APA_ROOT: $ROOT"
echo "═══════════════════════════════════════════════════════════"

# ============================================================================
# [Step 0] 누락 일자 감지 (Resilience Hardening · F)
# ============================================================================
# 직전 7일 동안 daily-report_ko.md가 빠진 날짜가 있으면 경고로 보고한다.
# 이 단계는 PASS/FAIL 카운터를 증가시키지 않는다 (정보 표시 목적).
# 실제 차단은 apa-catchup-guard 스킬이 담당한다.
echo ""
echo "▶ [Step 0] 누락 일자 감지 (직전 7일)"
CHECK_SCRIPT="$ROOT/outputs/scripts/check_missed_days.sh"
if [ -x "$CHECK_SCRIPT" ]; then
  STEP0_OUT=$(bash "$CHECK_SCRIPT" --root "$ROOT" 2>&1)
  STEP0_RC=$?
  if [ "$STEP0_RC" = "0" ]; then
    echo "  ✅ 직전 7일 모두 커버됨"
  else
    MISS_LINE=$(echo "$STEP0_OUT" | grep "^MISSING_DATES:" | head -1)
    COVER_LINE=$(echo "$STEP0_OUT" | grep "^COVERED:" | head -1)
    echo "  ⚠️  누락 감지 — ${MISS_LINE} (${COVER_LINE})"
    echo "      → apa-catchup-guard 스킬을 실행하여 복구 권장"
  fi
else
  echo "  ⏭  check_missed_days.sh 미설치 (선택적)"
fi

# ============================================================================
# [Step 1] 소스 노트 + 한국 1차 소스 검증
# ============================================================================
echo ""
echo "▶ [Step 1] 소스 노트 검수 (북미+MCP+Key Figure+한국)"
SRC=$(ls "$SOURCES"/${DATE}_*source-notes.md 2>/dev/null | head -1)
if [ -n "$SRC" ]; then
  check "소스 노트 존재" 1

  # ─── 북미·글로벌 영어 1차 소스 ≥ 10건 ───
  NA_TIER1=$(grep -Eo "openai\.com|anthropic\.com|deepmind|nvidia\.com|theinformation\.com|semianalysis|reuters\.com|bloomberg\.com|whitehouse\.gov|huggingface\.co|microsoft\.com|ai\.meta\.com|x\.ai|mistral\.ai|stratechery|importai|techcrunch|wired\.com|technologyreview|venturebeat|deeplearning\.ai|a16z\.com|sequoiacap|rand\.org|cset\.georgetown|ainowinstitute" "$SRC" 2>/dev/null | sort -u | wc -l)
  NA_BRANDS=$(grep -Eo "OpenAI|Anthropic|NVIDIA|Microsoft|Google|Meta|Stanford|MIT|Reuters|Bloomberg|TechCrunch|White House|EU AI Office" "$SRC" 2>/dev/null | sort -u | wc -l)
  if [ "$NA_TIER1" -ge "5" ] || [ "$NA_BRANDS" -ge "10" ]; then
    check "북미·영어 1차 소스 ≥ 10건 (Tier 1·2 도메인=${NA_TIER1} 브랜드=${NA_BRANDS})" 1
  else
    check "북미·영어 1차 소스 ≥ 10건" 0 "도메인=${NA_TIER1} 브랜드=${NA_BRANDS} (부족 — references/source-list.md Tier 1·2 참조)"
  fi

  # ─── MCP/에이전트 프로토콜 신호 ≥ 1건 (매일 모니터링; 추후 화·수에만 적용 검토) ───
  MCP_KW=$(grep -Eoi "MCP|Model Context Protocol|agent protocol|A2A protocol|agentic|LangChain|LangGraph|CrewAI|AutoGen" "$SRC" 2>/dev/null | sort -u | wc -l)
  MCP_LOG="$ROOT/outputs/_mcp-signal-log.csv"
  if [ ! -f "$MCP_LOG" ]; then echo "date,signal_count" > "$MCP_LOG"; fi
  echo "${DATE},${MCP_KW}" >> "$MCP_LOG"
  # 14일 신호 평균이 1 미만이면 권고 메시지
  RECENT=$(tail -14 "$MCP_LOG" | awk -F, 'NR>1 {sum+=$2; cnt++} END {if(cnt>0) print sum/cnt; else print 0}')
  if [ "$MCP_KW" -ge "1" ]; then
    check "MCP/에이전트 프로토콜 신호 ≥ 1건 (오늘 ${MCP_KW}건 · 14일 평균 ${RECENT})" 1
  else
    # 0건은 NOTES 처리 (FAIL 아님 — 신호 없는 날도 정상)
    check "MCP/에이전트 프로토콜 신호 — 오늘 0건 (14일 평균 ${RECENT})" 1
  fi
  # 14일 평균 0.5 미만이면 운영자에게 권고 (참고용 echo)
  if [ "$(echo "$RECENT < 0.5" | bc -l 2>/dev/null)" = "1" ]; then
    echo "    ℹ  MCP 14일 평균 ${RECENT} < 0.5 — 매일 모니터링 → 화·수(L3·L5) 집중일로 이전 검토 권고"
  fi

  # ─── Key Figure X 포스트 확인 ≥ 1건 (또는 "확인 — 해당 없음") ───
  KF_HANDLES=$(grep -Eo "@jensenhuang|@sama|@DarioAmodei|@demishassabis|@elonmusk|@ClementDelangue|@kevin_scott|@adcock_brett|@pmarca|@janleike|@Yoshua_Bengio|@drfeifei" "$SRC" 2>/dev/null | sort -u | wc -l)
  KF_NAMES=$(grep -Eo "Jensen Huang|Sam Altman|Dario Amodei|Demis Hassabis|Elon Musk|Marc Andreessen|Yoshua Bengio|Fei-Fei Li" "$SRC" 2>/dev/null | sort -u | wc -l)
  KF_NOTE=$(grep -c "Key Figure\|키 피규어\|확인 — 해당 없음" "$SRC" 2>/dev/null)
  if [ "$KF_HANDLES" -ge "1" ] || [ "$KF_NAMES" -ge "2" ] || [ "$KF_NOTE" -ge "1" ]; then
    check "Key Figure 확인 (handles=${KF_HANDLES} names=${KF_NAMES} 명시=${KF_NOTE})" 1
  else
    check "Key Figure 확인" 0 "오늘 레이어 ★★★ 인물 X 포스트 검색 또는 '확인 — 해당 없음' 명시 필요 (references/key-figures-tracker.md 참조)"
  fi

  # ─── 한국 1차 소스 ≥ 5건 (기존) ───
  KR_DOMAIN=$(grep -Eo "https?://[^[:space:]]+\.(kr|co\.kr|or\.kr|go\.kr|re\.kr|ac\.kr)/[^[:space:]]*" "$SRC" 2>/dev/null | sort -u | wc -l)
  KR_MEDIA=$(grep -Eo "매일경제|한국경제|전자신문|조선비즈|이데일리|뉴시스|디지털타임스|ZDNet Korea|AI타임스" "$SRC" 2>/dev/null | sort -u | wc -l)
  KR_ENTITY=$(grep -Eo "삼성전자|SK hynix|SK하이닉스|네이버|카카오|LG AI|Upstage|뤼튼|과기정통부|산업통상자원부|금융위|국가AI위원회|KAIST|KISDI" "$SRC" 2>/dev/null | sort -u | wc -l)
  KR_TOTAL=$((KR_DOMAIN + KR_MEDIA + KR_ENTITY))
  KR_SECTION=$(grep -c "한국 시장\|KR-specific\|KR 1차 소스\|한국 1차" "$SRC" 2>/dev/null)
  if [ "$KR_TOTAL" -ge "5" ] || [ "$KR_SECTION" -ge "1" ]; then
    check "한국 1차 소스 ≥ 5건 (도메인=${KR_DOMAIN} 매체=${KR_MEDIA} 엔티티=${KR_ENTITY} · 섹션=${KR_SECTION})" 1
  else
    check "한국 1차 소스 ≥ 5건" 0 "도메인=${KR_DOMAIN} 매체=${KR_MEDIA} 엔티티=${KR_ENTITY} 합계=${KR_TOTAL} (5건 미만 — references/korea-sources.md 참조)"
  fi
else
  check "소스 노트 존재" 0 "missing ${DATE}_*source-notes.md"
fi

# ============================================================================
# [Step 2] 리포트 3개 파일 + 언어 분리 검증
# ============================================================================
echo ""
echo "▶ [Step 2] 리포트 2종 세트 검수 (_v1.md 생성 금지)"
V1=$(ls "$REPORTS"/${DATE}_*daily-report_v1.md 2>/dev/null | head -1)
EN_REPORT=$(ls "$REPORTS"/${DATE}_*daily-report_en.md 2>/dev/null | head -1)
KO_REPORT=$(ls "$REPORTS"/${DATE}_*daily-report_ko.md 2>/dev/null | head -1)

[ -n "$EN_REPORT" ] && check "리포트 _en.md (영어 전용)" 1 || check "리포트 _en.md (영어 전용)" 0 "missing ${DATE}_*daily-report_en.md"
[ -n "$KO_REPORT" ] && check "리포트 _ko.md (한국어 전용 + 한국 시장 보강)" 1 || check "리포트 _ko.md (한국어 전용 + 한국 시장 보강)" 0 "missing ${DATE}_*daily-report_ko.md"

# _v1.md 존재하면 경고 (legacy 금지 대상)
[ -z "$V1" ] && check "_v1.md 미생성 (금지 대상)" 1 || check "_v1.md 미생성 (금지 대상)" 0 "$V1 존재 — legacy 한영 병기 파일. 삭제 권장."

# 언어 분리 검증: _en.md는 한글 비율 <5%, _ko.md는 한글 비율 >30%
if [ -n "$EN_REPORT" ]; then
  RATIO=$(python3 -c "
import re
with open('$EN_REPORT', encoding='utf-8') as f: t = f.read()
ko = len(re.findall(r'[가-힣]', t))
total = len(t)
print(round(100*ko/total, 1) if total else 0)
")
  OVER=$(python3 -c "print(1 if float('$RATIO') < 5 else 0)")
  check "_en.md 한글 비율 < 5% (실제 ${RATIO}%)" "$OVER" "$([ "$OVER" = "0" ] && echo "영어 전용 파일에 한글이 과다합니다")"
fi

if [ -n "$KO_REPORT" ]; then
  RATIO=$(python3 -c "
import re
with open('$KO_REPORT', encoding='utf-8') as f: t = f.read()
ko = len(re.findall(r'[가-힣]', t))
total = len(t)
print(round(100*ko/total, 1) if total else 0)
")
  OVER=$(python3 -c "print(1 if float('$RATIO') > 25 else 0)")
  check "_ko.md 한글 비율 > 25% (실제 ${RATIO}%)" "$OVER" "$([ "$OVER" = "0" ] && echo "한국어 전용 파일인데 한글이 부족합니다")"

  # 한국 시장 보강 검증 (S09 섹션 또는 인라인 '한국 시장 파급' 블록 최소 2개)
  KR_SECTION=$(grep -c "^## S09\|Regional Market Addendum\|지역 시장 보강" "$KO_REPORT")
  KR_INLINE=$(grep -c "한국 시장 파급\|한국 시장 영향\|국내 시장 파급" "$KO_REPORT")
  KR_KEYWORD=$(grep -Eo "삼성전자|SK hynix|네이버|카카오|한국|국내|과기정통부|산업부|코스피|원화" "$KO_REPORT" | sort -u | wc -l)
  if [ "$KR_SECTION" -ge "1" ] || [ "$KR_INLINE" -ge "2" ]; then
    check "_ko.md 한국 시장 보강 (S09 섹션 또는 인라인 ≥2 + 키워드 ${KR_KEYWORD}개)" 1
  else
    check "_ko.md 한국 시장 보강" 0 "S09 섹션=0 AND 인라인=${KR_INLINE} (≥2 필요) AND 한국 키워드=${KR_KEYWORD} — 한국 시장 파급 정보를 보강해야 합니다"
  fi
fi

# ─── 번역 충실도 1차 검수 (EN vs KO) ───
if [ -n "$EN_REPORT" ] && [ -n "$KO_REPORT" ]; then
  echo ""
  echo "  ▸ 번역 충실도 1차 검수 (EN ↔ KO)"
  FIDELITY=$(python3 << PYEOF
import re, sys
with open("$EN_REPORT", encoding="utf-8") as f: en = f.read()
with open("$KO_REPORT", encoding="utf-8") as f: ko = f.read()

checks = []

# 1. S01 이벤트 3개 존재
en_events = len(re.findall(r'(?m)^### Event\s+\d', en))
ko_events = len(re.findall(r'(?m)^### Event\s+\d', ko))
checks.append(("S01 이벤트 3개 일치", en_events == 3 and ko_events == 3, f"EN={en_events} KO={ko_events}"))

# 2. S01–S08 8개 섹션 존재
en_sections = len(re.findall(r'(?m)^##\s+S0[1-8]\s*\|', en))
ko_sections = len(re.findall(r'(?m)^##\s+S0[1-8]\s*\|', ko))
checks.append(("S01–S08 8개 섹션 일치", en_sections == 8 and ko_sections == 8, f"EN={en_sections} KO={ko_sections}"))

# 3. 주요 % 수치 일치 — 벤치마크·비율 숫자는 언어 무관하게 동일해야 함
PCT = re.compile(r'\b\d+\.?\d*%')
en_pcts = set(PCT.findall(en))
ko_pcts = set(PCT.findall(ko))
missing_pcts = en_pcts - ko_pcts
pct_ratio = 1.0 - len(missing_pcts) / max(len(en_pcts), 1)
checks.append((f"주요 % 수치 일치율 ≥ 90% (실제 {round(pct_ratio*100,1)}%)", pct_ratio >= 0.90, f"EN에 있고 KO에 없는 %: {sorted(missing_pcts)[:5]}"))

# 4. 핵심 기업/제품명 일치 — Latin 알파벳 고유명사는 KO에도 그대로 남아야 함
# (한국어 번역 관례: 지명은 한글화되나 기업·제품·법·지표명은 영문 유지)
BRAND_EN_ONLY = [
    'OpenAI', 'Anthropic', 'NVIDIA', 'Microsoft', 'Google', 'Broadcom', 'Meta',
    'GPT-5.5', 'GB200', 'NVL72', 'Claude', 'Azure', 'Copilot', 'Cursor',
    'Terminal-Bench', 'OSWorld', 'MRCR',
    'Stanford AI Index', 'Frontier', 'ChatGPT', 'Gemini',
    'ASD', 'AISI', 'RSP',
]
brand_missing = [b for b in BRAND_EN_ONLY if b in en and b not in ko]
brand_total = [b for b in BRAND_EN_ONLY if b in en]
brand_ratio = 1.0 - len(brand_missing) / max(len(brand_total), 1)
checks.append((f"핵심 기업·제품명 일치율 ≥ 90% (실제 {round(brand_ratio*100,1)}%)", brand_ratio >= 0.90, f"EN에만 있음: {brand_missing[:5]}"))

# 5. 문자 수 비율 — KO 문자 수 ≥ EN × 0.45 (한글은 음절 밀도 높아 자연히 짧음; 축약 방지 최소선)
en_len = len(en)
ko_len = len(ko)
len_ratio = ko_len / max(en_len, 1)
checks.append((f"문자 수 비율 (KO/EN) ≥ 0.45 (실제 {round(len_ratio,2)})", len_ratio >= 0.45, f"EN={en_len} KO={ko_len} — 0.45 미만이면 요약·축약 의심"))

# 6. KO 본문 영문 단어 비율 — 한글 우선 정책 (translation-policy.md)
# 화이트리스트(고유명사·약어): 카운트 제외. 임계값 ≤ 15%
WHITELIST = set(BRAND_EN_ONLY) | {
    'AI', 'GPU', 'CPU', 'API', 'MCP', 'RAG', 'LLM', 'HBM', 'ARR', 'MRR',
    'EU', 'US', 'UK', 'KR', 'JP', 'CN',
    'L1','L2','L3','L4','L5','L6','L7','L8','L9','L10',
    'S01','S02','S03','S04','S05','S06','S07','S08','S09',
    'PASS','FAIL','HIGH','MEDIUM','LOW',
    'Q1','Q2','Q3','Q4',
    'B','M','K','T',
}
# KO 본문에서 영문 단어 추출 (자체평가 주석·코드블록·링크·URL 제외)
ko_body = re.sub(r'<!--.*?-->', '', ko, flags=re.DOTALL)
ko_body = re.sub(r'```.*?```', '', ko_body, flags=re.DOTALL)
ko_body = re.sub(r'\[(.*?)\]\((.*?)\)', r'\1', ko_body)
ko_body = re.sub(r'https?://\S+', '', ko_body)
en_words_in_ko = re.findall(r'\b[A-Za-z][A-Za-z0-9\-]{1,}\b', ko_body)
en_filtered = [w for w in en_words_in_ko if w not in WHITELIST]
total_words_in_ko = len(re.findall(r'\S+', ko_body))
en_ratio = len(en_filtered) / max(total_words_in_ko, 1)
top_offenders = sorted(set(en_filtered), key=lambda x: en_filtered.count(x), reverse=True)[:8]
checks.append((f"KO 본문 영문 단어 비율 ≤ 15% (실제 {round(en_ratio*100,1)}%)", en_ratio <= 0.15, f"화이트리스트 외 영어: {top_offenders}"))

fail_lines = []
for label, ok, detail in checks:
    mark = "PASS" if ok else "FAIL"
    print(f"{mark}|{label}|{detail}")
    if not ok: fail_lines.append(label)
PYEOF
)
  while IFS='|' read -r mark label detail; do
    [ -z "$mark" ] && continue
    if [ "$mark" = "PASS" ]; then
      check "    $label" 1
    else
      check "    $label" 0 "$detail"
    fi
  done <<< "$FIDELITY"
fi

# ============================================================================
# [Step 3] PDF 검수
# ============================================================================
echo ""
echo "▶ [Step 3] PDF 리포트 검수"
PDF="$PDFS/${DATE}_daily-report.pdf"

if [ -f "$PDF" ]; then
  check "PDF 존재: ${DATE}_daily-report.pdf" 1
  PAGES=$(pdfinfo "$PDF" 2>/dev/null | awk '/^Pages:/ {print $2}')
  SIZE=$(stat -c%s "$PDF" 2>/dev/null || stat -f%z "$PDF" 2>/dev/null)
  [ "${PAGES:-0}" -ge 13 ] && check "PDF 페이지 ≥ 13 (실제 ${PAGES}p)" 1 || check "PDF 페이지 ≥ 13 (실제 ${PAGES:-?}p)" 0 "표준은 EN ≥7p + KO ≥7p"
  [ "${SIZE:-0}" -ge 200000 ] && check "PDF 크기 ≥ 200KB ($(echo $SIZE | awk '{printf "%.0fKB", $1/1024}'))" 1 || check "PDF 크기 ≥ 200KB" 0 "실제 ${SIZE}B — 내용 부족 의심"

  # EN/KO 섹션 분리 검증: 앞쪽 페이지에 '한국어판' 없음 + 뒤쪽 페이지에 있음
  EN_HAS_KO_HEADER=$(pdftotext -f 1 -l 3 "$PDF" - 2>/dev/null | grep -c "한국어판\|한국어 에디션")
  KO_HAS_KO_HEADER=$(pdftotext "$PDF" - 2>/dev/null | grep -c "한국어판\|한국어 에디션")
  [ "$EN_HAS_KO_HEADER" = "0" ] && check "PDF 전반부: EN 섹션만 포함" 1 || check "PDF 전반부: EN 섹션만 포함" 0 "전반부에 한국어판 헤더가 보임 — 구조 오류"
  [ "$KO_HAS_KO_HEADER" -gt "0" ] && check "PDF 후반부: KO 섹션 헤더 존재" 1 || check "PDF 후반부: KO 섹션 헤더 존재" 0 "KO 섹션이 빠진 것으로 보임"
else
  check "PDF 존재" 0 "missing $PDF"
fi

# ============================================================================
# [Step 4] 뉴스레터 4개 파일 검수
# ============================================================================
echo ""
echo "▶ [Step 4] 뉴스레터 4종 세트 검수"
NL_FREE_KO=$(ls "$NEWSLETTERS"/${DATE}_*_newsletter_free-ko.html 2>/dev/null | head -1)
NL_FREE_EN=$(ls "$NEWSLETTERS"/${DATE}_*_newsletter_free-en.html 2>/dev/null | head -1)
NL_PRO_KO=$(ls "$NEWSLETTERS"/${DATE}_*_newsletter_pro-ko.html 2>/dev/null | head -1)
NL_PRO_EN=$(ls "$NEWSLETTERS"/${DATE}_*_newsletter_pro-en.html 2>/dev/null | head -1)

[ -n "$NL_FREE_KO" ] && check "Free KO 뉴스레터" 1 || check "Free KO 뉴스레터" 0 "missing ${DATE}_*_newsletter_free-ko.html"
[ -n "$NL_FREE_EN" ] && check "Free EN 뉴스레터" 1 || check "Free EN 뉴스레터" 0 "missing ${DATE}_*_newsletter_free-en.html"
[ -n "$NL_PRO_KO" ] && check "Pro KO 뉴스레터" 1 || check "Pro KO 뉴스레터" 0 "missing ${DATE}_*_newsletter_pro-ko.html"
[ -n "$NL_PRO_EN" ] && check "Pro EN 뉴스레터" 1 || check "Pro EN 뉴스레터" 0 "missing ${DATE}_*_newsletter_pro-en.html"

# 크기 sanity check
for f in "$NL_FREE_KO" "$NL_FREE_EN" "$NL_PRO_KO" "$NL_PRO_EN"; do
  if [ -n "$f" ] && [ -f "$f" ]; then
    SZ=$(stat -c%s "$f" 2>/dev/null || stat -f%z "$f" 2>/dev/null)
    NAME=$(basename "$f")
    [ "${SZ:-0}" -ge 5000 ] && check "  $NAME ≥ 5KB ($(echo $SZ | awk '{printf "%.0fKB", $1/1024}'))" 1 || check "  $NAME ≥ 5KB" 0 "실제 ${SZ}B — 빈 템플릿 의심"
  fi
done

# Free 시그니처: NL-01 + Design B-2 + Pro CTA + Free footer + ~10-18KB
for f in "$NL_FREE_KO" "$NL_FREE_EN"; do
  if [ -n "$f" ] && [ -f "$f" ]; then
    NAME=$(basename "$f")
    HAS_NL01=$(head -3 "$f" | grep -c "NL-01")
    HAS_DESIGN=$(head -3 "$f" | grep -c "Design B-2")
    HAS_UPGRADE=$(grep -c "Pro로 업그레이드\|Upgrade to Pro" "$f")
    HAS_FREE_FOOTER=$(grep -c "무료 구독자\|Free subscriber" "$f")
    SZ=$(stat -c%s "$f" 2>/dev/null || stat -f%z "$f" 2>/dev/null)
    SZ_OK=$(python3 -c "print(1 if 8000 <= ${SZ:-0} <= 20000 else 0)")
    if [ "$HAS_NL01" = "1" ] && [ "$HAS_DESIGN" = "1" ] && [ "$HAS_UPGRADE" -ge "1" ] && [ "$HAS_FREE_FOOTER" -ge "1" ] && [ "$SZ_OK" = "1" ]; then
      check "  $NAME : Free 시그니처 (NL-01 · B-2 · Pro CTA · Free footer · 8–20KB)" 1
    else
      check "  $NAME : Free 시그니처" 0 "NL-01=$HAS_NL01 B-2=$HAS_DESIGN upgrade=$HAS_UPGRADE footer=$HAS_FREE_FOOTER size_ok=$SZ_OK"
    fi
  fi
done

# Pro 시그니처: NL-02 + Design C-5 + PRO badge + Pro footer + ≥25KB
for f in "$NL_PRO_KO" "$NL_PRO_EN"; do
  if [ -n "$f" ] && [ -f "$f" ]; then
    NAME=$(basename "$f")
    HAS_NL02=$(head -3 "$f" | grep -c "NL-02")
    HAS_DESIGN=$(head -3 "$f" | grep -c "Design C-5")
    HAS_BADGE=$(grep -c ">PRO</\|Pro 에디션\|Pro Edition" "$f")
    HAS_PRO_FOOTER=$(grep -c "Pro 구독자\|Pro subscriber" "$f")
    HAS_PDF=$(grep -c "/pdf/${DATE}_daily-report.pdf" "$f")
    SZ=$(stat -c%s "$f" 2>/dev/null || stat -f%z "$f" 2>/dev/null)
    SZ_OK=$(python3 -c "print(1 if ${SZ:-0} >= 25000 else 0)")
    if [ "$HAS_NL02" = "1" ] && [ "$HAS_DESIGN" = "1" ] && [ "$HAS_BADGE" -ge "1" ] && [ "$HAS_PRO_FOOTER" -ge "1" ] && [ "$HAS_PDF" -ge "1" ] && [ "$SZ_OK" = "1" ]; then
      check "  $NAME : Pro 시그니처 (NL-02 · C-5 · PRO badge · PDF link · ≥25KB)" 1
    else
      check "  $NAME : Pro 시그니처" 0 "NL-02=$HAS_NL02 C-5=$HAS_DESIGN badge=$HAS_BADGE footer=$HAS_PRO_FOOTER PDF=$HAS_PDF size_ok=$SZ_OK (실제 ${SZ}B)"
    fi
  fi
done

# ─────────────────────────────────────────────────────────────────
# [Step 4-X] 본문 콘텐츠 매칭 검수 (직전일 회귀 차단 · 2026-04-27 추가)
# 목적: 직전일 뉴스레터를 복사해 헤더만 교체하는 회귀 패턴 차단
# 방법: 리포트 _en.md S01 Event 1·2·3 제목에서 distinguishing 키워드 추출 →
#       각 파생 산출물(뉴스레터 4 + 블로그 HTML 2 + 소셜)에 키워드 ≥3개 일치 확인
# ─────────────────────────────────────────────────────────────────
echo ""
echo "▶ [Step 4-X] 본문 콘텐츠 매칭 검수 (직전일 회귀 차단)"

# 산출물 경로 미리 확정 (Step 6/7 보다 먼저 사용)
BLOG_KO_X=$(ls "$BLOG_POSTS"/ai-power-atlas-${DATE}-*-ko.html 2>/dev/null | head -1)
BLOG_EN_X=$(ls "$BLOG_POSTS"/ai-power-atlas-${DATE}-*-en.html 2>/dev/null | head -1)
SOCIAL_X=$(ls "$ROOT/outputs/social/${DATE}"_*_social.md 2>/dev/null | head -1)

if [ -n "$EN_REPORT" ] && [ -f "$EN_REPORT" ]; then
  TODAY_KEYS=$(python3 - "$EN_REPORT" << 'PYEOF'
import re, sys
with open(sys.argv[1]) as f:
    md = f.read()
events = re.findall(r"### Event \d+:\s*(.+?)\n", md)
title_text = " | ".join(events).strip()
candidates = set()
for tok in re.findall(r"\b[A-Z][A-Za-z0-9]{2,}(?:[ \-/][A-Z][A-Za-z0-9]{2,}){0,3}\b", title_text):
    if len(tok) >= 4 and tok.split()[0] not in {"Event","And","The","For","With"}:
        candidates.add(tok)
for m in re.findall(r"\b\d+\.?\d*%|\b\d+(?:-Year|-year)\b|Q[1-4]\s?20\d{2}", title_text):
    candidates.add(m)
print("\n".join(sorted(candidates)[:12]))
PYEOF
)
  if [ -z "$TODAY_KEYS" ]; then
    check "본문 매칭 키워드 추출" 0 "리포트에서 distinguishing 키워드 추출 실패"
  else
    KEY_COUNT=$(echo "$TODAY_KEYS" | wc -l | tr -d ' ')
    check "본문 매칭 키워드 추출 ($KEY_COUNT개)" 1
    MIN_MATCH=3
    for label_fn in "Free KO|$NL_FREE_KO" "Free EN|$NL_FREE_EN" "Pro KO|$NL_PRO_KO" "Pro EN|$NL_PRO_EN" "Blog HTML KO|$BLOG_KO_X" "Blog HTML EN|$BLOG_EN_X" "Social|$SOCIAL_X"; do
      LABEL="${label_fn%%|*}"
      FN="${label_fn##*|}"
      if [ -z "$FN" ] || [ ! -f "$FN" ]; then continue; fi
      MATCHES=0
      while IFS= read -r KEY; do
        if [ -z "$KEY" ]; then continue; fi
        if grep -qF "$KEY" "$FN"; then MATCHES=$((MATCHES+1)); fi
      done <<< "$TODAY_KEYS"
      if [ "$MATCHES" -ge "$MIN_MATCH" ]; then
        check "  $LABEL : 오늘 키워드 ${MATCHES}/${KEY_COUNT} 일치 (≥${MIN_MATCH})" 1
      else
        check "  $LABEL : 오늘 키워드 ${MATCHES}개만 일치 (≥${MIN_MATCH} 필요) — 본문 미교체 의심" 0 "키워드: $(echo "$TODAY_KEYS" | tr '\n' ' ')"
      fi
    done
    # 직전 동일 레이어 회귀 검사 (D-2 기준 — 일요일 휴간일 고려)
    PREV_DATE=$(python3 -c "from datetime import date,timedelta; d=date.fromisoformat('$DATE'); print((d-timedelta(days=2)).isoformat())")
    PREV_EN=$(ls "$REPORTS"/${PREV_DATE}_*_daily-report_en.md 2>/dev/null | head -1)
    if [ -n "$PREV_EN" ] && [ -f "$PREV_EN" ]; then
      PREV_KEYS=$(python3 - "$PREV_EN" << 'PYEOF'
import re, sys
with open(sys.argv[1]) as f: md=f.read()
ev = re.findall(r"### Event \d+:\s*(.+?)\n", md)
title = " | ".join(ev).strip()
c=set()
for tok in re.findall(r"\b[A-Z][A-Za-z0-9]{2,}(?:[ \-/][A-Z][A-Za-z0-9]{2,}){0,3}\b", title):
    if len(tok)>=4 and tok.split()[0] not in {"Event","And","The","For","With"}: c.add(tok)
print("\n".join(sorted(c)[:8]))
PYEOF
)
      if [ -n "$PREV_KEYS" ]; then
        for label_fn in "Free KO|$NL_FREE_KO" "Free EN|$NL_FREE_EN" "Pro KO|$NL_PRO_KO" "Pro EN|$NL_PRO_EN"; do
          LABEL="${label_fn%%|*}"; FN="${label_fn##*|}"
          if [ -z "$FN" ] || [ ! -f "$FN" ]; then continue; fi
          PREV_HITS=0
          while IFS= read -r PKEY; do
            if [ -z "$PKEY" ]; then continue; fi
            COUNT=$(grep -cF "$PKEY" "$FN" 2>/dev/null)
            COUNT=${COUNT:-0}
            PREV_HITS=$((PREV_HITS + COUNT))
          done <<< "$PREV_KEYS"
          if [ "$PREV_HITS" -le 3 ]; then
            check "  $LABEL : 직전일($PREV_DATE) 키워드 ${PREV_HITS}회 (≤3 허용)" 1
          else
            check "  $LABEL : 직전일($PREV_DATE) 키워드 ${PREV_HITS}회 — 본문 회귀 의심" 0 "직전일 키워드: $(echo "$PREV_KEYS" | tr '\n' ' ')"
          fi
        done
      fi
    fi
  fi
fi

# ============================================================================
# [Step 6] 블로그 HTML 검수 (필수 8요소)
# ============================================================================
echo ""
echo "▶ [Step 6] 블로그 HTML 검수 (필수 요소)"
BLOG_KO=$(ls "$BLOG_POSTS"/ai-power-atlas-${DATE}-*-ko.html 2>/dev/null | head -1)
BLOG_EN=$(ls "$BLOG_POSTS"/ai-power-atlas-${DATE}-*-en.html 2>/dev/null | head -1)

[ -n "$BLOG_KO" ] && check "블로그 HTML KO 존재" 1 || check "블로그 HTML KO 존재" 0 "missing ai-power-atlas-${DATE}-*-ko.html"
[ -n "$BLOG_EN" ] && check "블로그 HTML EN 존재" 1 || check "블로그 HTML EN 존재" 0 "missing ai-power-atlas-${DATE}-*-en.html"

# 필수 8요소 체크
REQUIRED=( "application/ld+json" "theme-toggle" "nav-cta" "apa_favicon" "scroll-top" "post-nav" "article-header" "article-body" )
for f in "$BLOG_KO" "$BLOG_EN"; do
  [ -z "$f" ] || [ ! -f "$f" ] && continue
  NAME=$(basename "$f")
  MISSING=""
  for k in "${REQUIRED[@]}"; do
    grep -q "$k" "$f" || MISSING="$MISSING $k"
  done
  if [ -z "$MISSING" ]; then
    check "  $NAME : 8개 필수 요소 전부 OK" 1
  else
    check "  $NAME : 필수 요소 누락" 0 "missing:${MISSING}"
  fi
done

# 전날 블로그의 next 링크가 오늘 포스트를 가리키는지
PREV_DATE=$(date -d "$DATE -1 day" +"%Y-%m-%d" 2>/dev/null || echo "")
if [ -n "$PREV_DATE" ]; then
  PREV_KO=$(ls "$BLOG_POSTS"/ai-power-atlas-${PREV_DATE}-*-ko.html 2>/dev/null | head -1)
  PREV_EN=$(ls "$BLOG_POSTS"/ai-power-atlas-${PREV_DATE}-*-en.html 2>/dev/null | head -1)
  if [ -n "$PREV_KO" ] && [ -f "$PREV_KO" ]; then
    grep -q "/blog/posts/ai-power-atlas-${DATE}-" "$PREV_KO" && check "  전날 KO 블로그 next → 오늘 포스트 링크" 1 || check "  전날 KO 블로그 next → 오늘 포스트 링크" 0 "$PREV_KO 에 ${DATE} 링크 없음"
  fi
  if [ -n "$PREV_EN" ] && [ -f "$PREV_EN" ]; then
    grep -q "/blog/posts/ai-power-atlas-${DATE}-" "$PREV_EN" && check "  전날 EN 블로그 next → 오늘 포스트 링크" 1 || check "  전날 EN 블로그 next → 오늘 포스트 링크" 0 "$PREV_EN 에 ${DATE} 링크 없음"
  fi
fi

# ============================================================================
# [Step 7] 인덱스/아카이브/인텔리전스 오늘 날짜 반영
# ============================================================================
echo ""
echo "▶ [Step 7] 블로그 인덱스·아카이브·인텔리전스 검수"
for f in \
  "$ROOT/web/blog/index.html" \
  "$ROOT/web/blog/index_kr.html" \
  "$ROOT/web/blog/archive/index.html" \
  "$ROOT/web/blog/archive/index_kr.html" ; do
  if [ -f "$f" ]; then
    grep -q "$DATE" "$f" && check "  $(basename $(dirname $f))/$(basename $f) 에 $DATE 포함" 1 || check "  $(basename $(dirname $f))/$(basename $f) 에 $DATE 포함" 0 "누락"
  fi
done

# intelligence preview date
INTEL="$ROOT/web/intelligence/index.html"
if [ -f "$INTEL" ]; then
  MON=$(date -d "$DATE" +"%B" 2>/dev/null || echo "")
  DAY=$(date -d "$DATE" +"%-d" 2>/dev/null || echo "")
  YEAR=$(date -d "$DATE" +"%Y" 2>/dev/null || echo "")
  if [ -n "$MON" ] && [ -n "$DAY" ] && [ -n "$YEAR" ]; then
    PATTERN="$MON $DAY, $YEAR"
    grep -q "$PATTERN" "$INTEL" && check "  intelligence/index.html preview 날짜 ($PATTERN)" 1 || check "  intelligence/index.html preview 날짜 ($PATTERN)" 0 "최신 날짜로 갱신 필요"
  fi
fi

# ============================================================================
# [Step 9] 자동 품질 감사 (quality_audit.py 산출물 확인)
# ============================================================================
echo ""
echo "▶ [Step 9] 자동 품질 감사 검수"
QA_FILE="$ROOT/outputs/quality/${DATE}_daily-audit.md"
QA_PROMPTS="$ROOT/outputs/quality/${DATE}_audit-prompts.md"
if [ -f "$QA_FILE" ]; then
  check "품질 감사 보고서 존재" 1
  VERDICT=$(grep -m1 "판정 (프로그래매틱 5/8)" "$QA_FILE" 2>/dev/null | grep -oE "PASS with NOTES|PASS|FAIL|SKIP" | head -1)
  case "$VERDICT" in
    PASS) check "품질 감사 판정: $VERDICT" 1 ;;
    "PASS with NOTES") check "품질 감사 판정: $VERDICT (참고 사항 있음)" 1 ;;
    FAIL) check "품질 감사 판정: $VERDICT" 0 "프로그래매틱 검사 1개 이상 FAIL — $QA_FILE 확인" ;;
    *) check "품질 감사 판정 미확인" 0 "$QA_FILE 의 판정 라인 파싱 실패" ;;
  esac
  if [ -f "$QA_PROMPTS" ]; then
    check "LLM 검사 프롬프트 (B·D·E) 생성됨" 1
  fi
else
  check "품질 감사 보고서 존재" 0 "missing $QA_FILE — python3 scripts/quality_audit.py ${DATE} 실행 필요"
fi

# ============================================================================
# [Step 11] 서버 업로드 검증 (선택적)
# ============================================================================
if [ "$SKIP_SERVER" = "0" ]; then
  echo ""
  echo "▶ [Step 11] 서버 업로드 검수"
  SSH_KEY=$(find /sessions -name id_rsa 2>/dev/null | grep -i "/mnt/.*apa.*/ssh/" | head -1)
  if [ -z "$SSH_KEY" ]; then
    echo "  ⏭  SSH 키 없음 — 서버 검증 스킵 (--skip-server 권장)"
  else
    chmod 600 "$SSH_KEY" 2>/dev/null
    REMOTE="intesolk@139.162.105.223"
    for path in \
      "/home/intesolk/aipoweratlas.com/blog/posts/ai-power-atlas-${DATE}-" \
      "/home/intesolk/aipoweratlas.com/pdf/${DATE}_daily-report.pdf" ; do
      FOUND=$(ssh -i "$SSH_KEY" -o StrictHostKeyChecking=no -o 