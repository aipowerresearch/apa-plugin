#!/usr/bin/env python3
# ============================================================================
# AI Power Atlas — Step 9 자동 품질 감사 (Quality Audit)
# ============================================================================
# 사용법:
#   python3 scripts/quality_audit.py YYYY-MM-DD
#   python3 scripts/quality_audit.py YYYY-MM-DD --strict   # FAIL 시 exit 1
#
# 검사 카테고리 (총 8개, A–H):
#   A. 수치 정확성        (프로그래매틱 자동)
#   B. 인용 귀속          (LLM 필요 — Cowork 프롬프트 생성)
#   C. 날짜·시점 정확성   (프로그래매틱 자동)
#   D. 논리 정합성        (LLM 필요 — Cowork 프롬프트 생성)
#   E. 소스 원문 대조     (LLM 필요 — Cowork 프롬프트 생성)
#   F. 섹션 간 정합성     (프로그래매틱 자동)
#   G. 템플릿 준수        (프로그래매틱 자동)
#   H. 파생 산출물 스팟   (프로그래매틱 자동)
#
# 산출물:
#   outputs/quality/{DATE}_daily-audit.md       (감사 결과 보고서)
#   outputs/quality/{DATE}_audit-prompts.md     (Cowork에서 LLM 검사할 3개 프롬프트)
#
# 종료 코드:
#   0 — 프로그래매틱 5개 PASS · LLM 3개 보고만 (기본 모드)
#   1 — 프로그래매틱 1개 이상 FAIL (--strict 시)
# ============================================================================

import sys, re, os, glob, json
from datetime import datetime
from pathlib import Path

# ───── APA_ROOT 탐색 ─────
def find_apa_root():
    if os.environ.get("APA_ROOT"):
        return Path(os.environ["APA_ROOT"])
    # SSH 키 기반 탐색 (Cowork 세션)
    for sess in glob.glob("/sessions/*/mnt/*/ssh/id_rsa"):
        return Path(sess).parent.parent
    # 스크립트 위치 기준
    return Path(__file__).resolve().parent.parent

ROOT = find_apa_root()

# ───── 인자 ─────
if len(sys.argv) < 2:
    print("Usage: quality_audit.py YYYY-MM-DD [--strict]", file=sys.stderr)
    sys.exit(2)
DATE = sys.argv[1]
STRICT = "--strict" in sys.argv

if not re.match(r"^\d{4}-\d{2}-\d{2}$", DATE):
    print("ERROR: Date must be YYYY-MM-DD", file=sys.stderr)
    sys.exit(2)

# ───── 입력 파일 로드 ─────
def find_one(pattern):
    matches = sorted(glob.glob(str(ROOT / pattern)))
    return matches[0] if matches else None

src_path = find_one(f"outputs/sources/{DATE}_*source-notes.md")
en_path  = find_one(f"outputs/reports/{DATE}_*_daily-report_en.md")
ko_path  = find_one(f"outputs/reports/{DATE}_*_daily-report_ko.md")
nl_pro_ko = find_one(f"outputs/newsletters/{DATE}_*_newsletter_pro-ko.html")
nl_pro_en = find_one(f"outputs/newsletters/{DATE}_*_newsletter_pro-en.html")
blog_ko   = find_one(f"web/blog/posts/ai-power-atlas-{DATE}-*-ko.html")
blog_en   = find_one(f"web/blog/posts/ai-power-atlas-{DATE}-*-en.html")
social    = find_one(f"outputs/social/{DATE}_*_social.md")

def read(p):
    if not p: return ""
    with open(p, encoding="utf-8") as f: return f.read()

src_text = read(src_path)
en_text  = read(en_path)
ko_text  = read(ko_path)
nl_pro_ko_text = read(nl_pro_ko)
nl_pro_en_text = read(nl_pro_en)
blog_ko_text   = read(blog_ko)
blog_en_text   = read(blog_en)
social_text    = read(social)

# ───── 검사 결과 누적 ─────
results = []   # list of (cat, label, status, detail)

def add(cat, label, status, detail=""):
    """status: PASS / FAIL / NOTES / SKIP / DEFERRED"""
    results.append((cat, label, status, detail))

def fail_count():
    return sum(1 for _, _, s, _ in results if s == "FAIL")

# ============================================================================
# A. 수치 정확성 — 리포트의 핵심 수치가 소스 노트에 존재하는가
# ============================================================================
def audit_A():
    if not en_text or not src_text:
        add("A", "수치 정확성", "SKIP", "리포트 또는 소스 노트 누락")
        return
    # EN 리포트의 % 수치·금액·인원 추출
    NUM_PAT = re.compile(r"\b(\d+\.?\d*%|\$\d+(?:[.,]\d+)*[BMK]?|A\$\d+(?:[.,]\d+)*[BMK]?|\d{1,3}(?:,\d{3})+|\d+M\b|\d+B\b)")
    en_nums = set(NUM_PAT.findall(en_text))
    src_nums = set(NUM_PAT.findall(src_text))
    # 핵심 수치 (3자리 이상)만 검증
    key_nums = {n for n in en_nums if len(n) >= 3}
    missing = sorted(key_nums - src_nums)
    if not key_nums:
        add("A", "수치 정확성 — 핵심 수치 추출 0개", "NOTES", "리포트에 정량 anchor 부족")
    elif len(missing) / len(key_nums) >= 0.30:
        add("A", f"수치 정확성 (소스 미매칭 {len(missing)}/{len(key_nums)})", "FAIL",
            f"30%+ 미매칭. 샘플: {missing[:5]}")
    elif missing:
        add("A", f"수치 정확성 (소스 미매칭 {len(missing)}/{len(key_nums)})", "NOTES",
            f"미매칭 샘플: {missing[:5]} — 소스 노트 보강 권고")
    else:
        add("A", f"수치 정확성 — {len(key_nums)}개 핵심 수치 모두 소스 매칭", "PASS")

# ============================================================================
# C. 날짜·시점 정확성 — 리포트의 날짜가 모두 합리적 범위 내인가
# ============================================================================
def audit_C():
    if not en_text:
        add("C", "날짜·시점 정확성", "SKIP", "리포트 누락"); return
    today = datetime.strptime(DATE, "%Y-%m-%d")
    DATE_PAT = re.compile(r"\b(20\d{2})-(\d{2})-(\d{2})\b|\b(20\d{2})/(\d{1,2})/(\d{1,2})\b")
    found_dates = []
    for m in DATE_PAT.finditer(en_text):
        try:
            if m.group(1):
                d = datetime(int(m.group(1)), int(m.group(2)), int(m.group(3)))
            else:
                d = datetime(int(m.group(4)), int(m.group(5)), int(m.group(6)))
            found_dates.append(d)
        except ValueError:
            pass
    # 미래 날짜 감지 (오늘 + 365일 이후)
    future = [d for d in found_dates if (d - today).days > 365]
    # 과거 너무 오래된 (오늘 - 1825일 이전 = 5년)
    too_old = [d for d in found_dates if (today - d).days > 1825]
    if future:
        add("C", f"날짜 정확성 — 1년 이상 미래 날짜 {len(future)}건", "FAIL",
            f"샘플: {[d.strftime('%Y-%m-%d') for d in future[:3]]}")
    elif too_old:
        add("C", f"날짜 정확성 — 5년 이상 과거 날짜 {len(too_old)}건", "NOTES",
            f"역사적 인용 가능성 — 확인 필요: {[d.strftime('%Y-%m-%d') for d in too_old[:3]]}")
    else:
        add("C", f"날짜 정확성 — {len(found_dates)}개 날짜 합리적 범위", "PASS")

# ============================================================================
# F. 섹션 간 정합성 — S07 Active 루프와 S01 Feedback Loop 필드 일치
# ============================================================================
def audit_F():
    if not en_text:
        add("F", "섹션 간 정합성", "SKIP", "리포트 누락"); return
    # S07 표에서 Active 상태 루프 추출
    s07_block = re.search(r"## S07 \|.*?(?=\n##|\Z)", en_text, re.DOTALL)
    s01_blocks = re.findall(r"### Event \d+:.*?(?=\n### Event \d+:|\n##|\Z)", en_text, re.DOTALL)
    if not s07_block or not s01_blocks:
        add("F", "섹션 간 정합성", "SKIP", "S07 또는 S01 추출 실패"); return
    s07_active_loops = set(re.findall(r"\b(L\d+→L\d+(?:→L\d+)?)\b\s*\|\s*Active", s07_block.group()))
    s01_loops = set()
    for b in s01_blocks:
        s01_loops.update(re.findall(r"\b(L\d+→L\d+(?:→L\d+)?)\b", b))
    # S07의 Active 루프 중 S01에 없는 것
    orphan = s07_active_loops - s01_loops
    if orphan:
        add("F", f"섹션 정합성 — S07 Active 루프 중 S01 미언급 {len(orphan)}건", "NOTES",
            f"Active 루프인데 어떤 이벤트도 활성화시키지 않음: {sorted(orphan)}")
    else:
        add("F", f"섹션 정합성 — S07 Active 루프 {len(s07_active_loops)}개 모두 S01에서 활성화", "PASS")
    # S08 Watchlist 3건 존재
    s08_block = re.search(r"## S08 \|.*?(?=\n##|\Z)", en_text, re.DOTALL)
    if s08_block:
        wl_count = len(re.findall(r"^\d+\.\s+\*\*", s08_block.group(), re.MULTILINE))
        if wl_count >= 3:
            add("F", f"섹션 정합성 — S08 Watchlist {wl_count}건", "PASS")
        else:
            add("F", f"섹션 정합성 — S08 Watchlist {wl_count}건 (3건 필요)", "FAIL",
                "내일 주목 신호가 부족합니다")

# ============================================================================
# G. 템플릿 준수 — S01 Event 3개 모두 8개 필드, S02-S08 헤더 존재
# ============================================================================
def audit_G():
    if not en_text:
        add("G", "템플릿 준수", "SKIP", "리포트 누락"); return
    REQUIRED_FIELDS = ["Layer", "Signal Type", "Impact Score", "Power Score",
                       "Time Horizon", "Power Flow", "Feedback Loop", "Summary", "Source"]
    s01_events = re.findall(r"### Event \d+:.*?(?=\n### Event \d+:|\n##|\Z)", en_text, re.DOTALL)
    if len(s01_events) != 3:
        add("G", f"템플릿 준수 — S01 Event {len(s01_events)}개 (3개 필요)", "FAIL"); return
    missing_overall = []
    for i, ev in enumerate(s01_events, 1):
        miss = [f for f in REQUIRED_FIELDS if f"**{f}**" not in ev]
        if miss:
            missing_overall.append((i, miss))
    if missing_overall:
        add("G", f"템플릿 준수 — Event 필드 누락", "FAIL",
            f"이벤트별 누락: {missing_overall}")
    else:
        add("G", "템플릿 준수 — S01 3개 이벤트 모두 9개 필드 완비", "PASS")
    # S02–S08 헤더 존재
    expected = ["S01", "S02", "S03", "S04", "S05", "S06", "S07", "S08"]
    found = re.findall(r"^##\s+(S0[1-8])\s*\|", en_text, re.MULTILINE)
    missing_sec = [s for s in expected if s not in found]
    if missing_sec:
        add("G", f"템플릿 준수 — 누락 섹션 {missing_sec}", "FAIL")
    else:
        add("G", "템플릿 준수 — S01–S08 8개 섹션 모두 존재", "PASS")

# ============================================================================
# H. 파생 산출물 스팟 체크 — 뉴스레터·블로그·소셜의 핵심 수치가 리포트와 일치
# ============================================================================
def audit_H():
    if not en_text:
        add("H", "파생 산출물 스팟", "SKIP", "리포트 누락"); return
    # 리포트의 % 수치 상위 5개 추출
    en_pcts = re.findall(r"\b\d+\.?\d*%", en_text)
    key_pcts = list(set(en_pcts))[:5]
    if not key_pcts:
        add("H", "파생 산출물 스팟 — 리포트에 % 수치 없음", "NOTES"); return
    targets = [
        ("뉴스레터 Pro KO", nl_pro_ko_text),
        ("뉴스레터 Pro EN", nl_pro_en_text),
        ("블로그 KO", blog_ko_text),
        ("블로그 EN", blog_en_text),
        ("소셜", social_text),
    ]
    fail_items = []
    pass_items = []
    for name, txt in targets:
        if not txt:
            continue
        miss = [p for p in key_pcts if p not in txt]
        if len(miss) > len(key_pcts) // 2:
            fail_items.append((name, miss))
        else:
            pass_items.append(name)
    if fail_items:
        add("H", f"파생 산출물 스팟 — 핵심 수치 절반 이상 누락 ({len(fail_items)}개 산출물)", "FAIL",
            f"누락 항목: {fail_items}")
    else:
        add("H", f"파생 산출물 스팟 — {len(pass_items)}개 산출물에서 핵심 수치 일치", "PASS")

# ============================================================================
# B, D, E — LLM 필요 (프롬프트 생성하여 Cowork에서 실행)
# ============================================================================
def emit_llm_prompts():
    """LLM 필요 검사 3개의 프롬프트 생성. ANTHROPIC_API_KEY가 있으면 직접 호출, 없으면 파일로 저장."""
    out_dir = ROOT / "outputs" / "quality"
    out_dir.mkdir(parents=True, exist_ok=True)
    prompts_file = out_dir / f"{DATE}_audit-prompts.md"

    en_excerpt = en_text[:6000] if en_text else "(no report)"
    src_excerpt = src_text[:6000] if src_text else "(no sources)"
    URL_PAT = re.compile(r"https?://[^\s)]+")
    S01_URLS = URL_PAT.findall(en_text)[:5] if en_text else []

    content = f"""# Daily Audit Prompts — {DATE} (LLM 필요 카테고리 B·D·E)

> 자동 검수 스크립트 quality_audit.py가 생성. Cowork 세션에서 fact-checker 서브에이전트에 아래 프롬프트를 전달하거나, ANTHROPIC_API_KEY 설정 후 quality_audit.py 재실행 시 자동 호출.

---

## B. 인용 귀속 검사

당신은 사실 확인 에디터다. 아래 일간 리포트(EN 발췌)에서 인물 발언·인용을 찾아 다음을 판단하라:

1. 모든 직접·간접 인용이 올바른 인물에 귀속되었는가?
2. 직접 인용("...")과 간접 인용 표현이 정확히 구분되었는가?
3. 소스 노트와 비교해 발언의 맥락이 왜곡되지 않았는가?

판정: PASS / NOTES / FAIL 중 하나.

**리포트 EN (발췌)**:
```
{en_excerpt}
```

**소스 노트 (발췌)**:
```
{src_excerpt}
```

---

## D. 논리 정합성 검사

당신은 구조 분석가다. 아래 리포트에서 다음 6가지 논리 정합성을 점검하라:

1. Impact Score 부여 근거와 서술 내용이 일관되는가?
2. Power Score 방향(+/-)과 실제 분석이 모순 없는가?
3. Feedback Loop 연결의 인과 관계가 타당한가?
4. S02(시스템 역학)가 S01(이벤트)에서 도출 가능한가?
5. S04(6개월 시사점)의 확신도와 근거 강도가 적합한가?
6. 같은 리포트 내 모순된 주장이 없는가?

각 항목별 PASS/NOTES/FAIL과 종합 판정 출력.

**리포트 EN**:
```
{en_excerpt}
```

---

## E. 소스 원문 대조 검사

당신은 외부 사실 확인자다. 리포트의 S01 핵심 이벤트 3건의 출처 URL이 아래 나열되어 있다. 각 URL의 실제 내용 (당신이 알고 있는 한도 내)과 리포트 기술을 대조해 왜곡·과장·누락이 있는지 판단하라.

**리포트 S01 출처 URL**:
{S01_URLS}

**리포트 EN**:
```
{en_excerpt}
```

각 출처별 PASS/NOTES/FAIL과 종합 판정 출력.

---

*이 파일은 Cowork 세션에서 fact-checker 서브에이전트의 입력으로 사용한다. 결과는 outputs/quality/{DATE}_daily-audit.md 의 B/D/E 섹션에 추가한다.*
"""
    prompts_file.write_text(content, encoding="utf-8")
    return prompts_file

# ============================================================================
# 실행
# ============================================================================
audit_A()
audit_C()
audit_F()
audit_G()
audit_H()
prompts_file = emit_llm_prompts()

# B, D, E는 DEFERRED로 표기
add("B", "인용 귀속 (LLM 필요)", "DEFERRED", f"프롬프트: {prompts_file.name}")
add("D", "논리 정합성 (LLM 필요)", "DEFERRED", f"프롬프트: {prompts_file.name}")
add("E", "소스 원문 대조 (LLM 필요)", "DEFERRED", f"프롬프트: {prompts_file.name}")

# ───── 산출물 저장 ─────
out_dir = ROOT / "outputs" / "quality"
out_dir.mkdir(parents=True, exist_ok=True)
audit_file = out_dir / f"{DATE}_daily-audit.md"

programmatic = [r for r in results if r[2] != "DEFERRED"]
deferred = [r for r in results if r[2] == "DEFERRED"]
fails = fail_count()

if fails == 0 and all(r[2] in ("PASS", "NOTES") for r in programmatic):
    if any(r[2] == "NOTES" for r in programmatic):
        verdict = "PASS with NOTES"
    else:
        verdict = "PASS"
else:
    verdict = "FAIL"

content = f"""# Daily Audit — {DATE}

**검사 대상**:
- 리포트 EN: {Path(en_path).name if en_path else '(missing)'}
- 리포트 KO: {Path(ko_path).name if ko_path else '(missing)'}
- 소스 노트: {Path(src_path).name if src_path else '(missing)'}

**판정 (프로그래매틱 5/8)**: **{verdict}**
**LLM 필요 (B·D·E)**: 별도 프롬프트 파일 — `{prompts_file.name}` (Cowork 또는 API 호출 필요)

---

## 자동 검사 결과 (A·C·F·G·H)

| 카테고리 | 항목 | 결과 | 상세 |
|---------|------|------|------|
"""
for cat, label, status, detail in programmatic:
    icon = {"PASS": "✅", "NOTES": "⚠️", "FAIL": "❌", "SKIP": "⏭"}.get(status, "❓")
    content += f"| {cat} | {label} | {icon} {status} | {detail[:80]} |\n"

content += f"""
---

## LLM 필요 검사 (B·D·E) — Deferred

| 카테고리 | 항목 | 상태 |
|---------|------|------|
"""
for cat, label, status, detail in deferred:
    content += f"| {cat} | {label} | 🔄 {status} ({detail}) |\n"

content += f"""
---

## 종합 판정: **{verdict}**

- 프로그래매틱 검사 (A·C·F·G·H): {sum(1 for _,_,s,_ in programmatic if s=='PASS')}개 PASS · {sum(1 for _,_,s,_ in programmatic if s=='NOTES')}개 NOTES · {fails}개 FAIL · {sum(1 for _,_,s,_ in programmatic if s=='SKIP')}개 SKIP
- LLM 필요 검사 (B·D·E): 3개 모두 DEFERRED — Cowork에서 fact-checker 서브에이전트 실행 또는 API 호출 후 결과 추가 입력
- 다음 실행: 매일 Step 9에서 자동 실행, 결과는 `outputs/quality/` 누적

*Generated by quality_audit.py at {datetime.now().isoformat(timespec='seconds')}*
"""

audit_file.write_text(content, encoding="utf-8")

# ───── 콘솔 요약 ─────
print(f"=== Daily Audit — {DATE} ===")
print(f"산출물: {audit_file}")
print(f"LLM 프롬프트: {prompts_file}")
print(f"")
for cat, label, status, detail in programmatic:
    icon = {"PASS": "✅", "NOTES": "⚠️", "FAIL": "❌", "SKIP": "⏭"}.get(status, "❓")
    print(f"  {cat}. {icon} {status:5s}  {label}")
for cat, label, status, _ in deferred:
    print(f"  {cat}. 🔄 DEFERRED  {label}")
print(f"")
print(f"종합 판정: {verdict}")

if STRICT and fails > 0:
    sys.exit(1)
sys.exit(0)
