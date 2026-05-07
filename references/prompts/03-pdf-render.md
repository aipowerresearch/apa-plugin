# Step 3 — PDF 생성 프롬프트

## 역할
WeasyPrint 기반 PDF 생성기를 호출해 `_en.md` + `_ko.md` 두 분리본을 단일 PDF로 결합한다. EN 섹션 → 페이지 구분 → KO 섹션 순서.

## 입력
- 영어 리포트: `outputs/reports/{{DATE}}_*_daily-report_en.md`
- 한국어 리포트: `outputs/reports/{{DATE}}_*_daily-report_ko.md`
- Noto CJK KR 폰트: `~/.local/share/fonts/noto-cjk/NotoSansCJKkr-{Regular,Bold}.otf`

## 출력
- `outputs/pdf/{{DATE}}_daily-report.pdf` (작업본)
- `web/pdf/{{DATE}}_daily-report.pdf` (배포본 — 위 파일 복사)

## 생성 절차 (Python)

```python
import markdown, weasyprint, shutil

APA_ROOT = "{{APA_ROOT}}"
DATE = "{{DATE}}"

CSS = """
body{font-family:'Noto Sans CJK KR',Georgia,serif;max-width:720px;margin:40px auto;color:#1a1a1a;line-height:1.7;font-size:10.5pt;padding:0 0 40px}
h1{color:#0f172a;border-bottom:3px solid #c9a84c;padding-bottom:8px;margin-top:32px}
h2{color:#2d3748;border-left:4px solid #c9a84c;padding-left:12px;margin-top:28px}
h3{color:#4a5568;margin-top:20px} h4{color:#718096}
table{border-collapse:collapse;width:100%;margin:14px 0;font-size:10pt}
th{background:#2d3748;color:#c9a84c;padding:7px 11px;text-align:left}
td{border:1px solid #e2ddd8;padding:7px 11px;vertical-align:top}
.hdr{background:#0f172a;color:white;padding:24px 32px;margin:-40px -40px 32px}
blockquote{border-left:4px solid #c9a84c;margin:8px 0;padding:8px 16px;background:#f8f6f2;color:#374151}
.lang-break{page-break-before:always}
.lang-hdr{background:#0f172a;color:white;padding:18px 28px;margin:0 -40px 28px;border-top:3px solid #c9a84c}
ul{margin:6px 0 6px 20px} li{margin:3px 0}
"""

def strip_frontmatter(md):
    if md.startswith('---'):
        end = md.find('\n---', 3)
        if end != -1: return md[end+4:].lstrip()
    return md

import glob
en_path = glob.glob(f"{APA_ROOT}/outputs/reports/{DATE}_*_daily-report_en.md")[0]
ko_path = glob.glob(f"{APA_ROOT}/outputs/reports/{DATE}_*_daily-report_ko.md")[0]
with open(en_path, encoding="utf-8") as f: en_md = strip_frontmatter(f.read())
with open(ko_path, encoding="utf-8") as f: ko_md = strip_frontmatter(f.read())

en_html = markdown.markdown(en_md, extensions=['tables','fenced_code'])
ko_html = markdown.markdown(ko_md, extensions=['tables','fenced_code'])

full_html = f"""<!DOCTYPE html><html><head><meta charset="UTF-8"><style>{CSS}</style></head><body>
<div class="hdr">
  <div style="color:#c9a84c;font-size:18px;font-weight:bold;letter-spacing:2px">AI POWER ATLAS</div>
  <div style="color:#94a3b8;font-size:13px;margin-top:5px">Daily Intelligence Report · English Edition · Pro · {DATE}</div>
</div>
{en_html}
<div class="lang-break"></div>
<div class="lang-hdr">
  <div style="color:#c9a84c;font-size:18px;font-weight:bold;letter-spacing:1px">AI POWER ATLAS · 한국어판</div>
  <div style="color:#94a3b8;font-size:13px;margin-top:5px">일간 인텔리전스 리포트 · 한국어 에디션 · Pro · {DATE}</div>
</div>
{ko_html}
</body></html>"""

pdf_out = f"{APA_ROOT}/outputs/pdf/{DATE}_daily-report.pdf"
weasyprint.HTML(string=full_html).write_pdf(pdf_out)
shutil.copy2(pdf_out, f"{APA_ROOT}/web/pdf/{DATE}_daily-report.pdf")
print(f"PDF written: {pdf_out}")
```

## 자가 검수 체크리스트

- [ ] `outputs/pdf/{{DATE}}_daily-report.pdf` 존재
- [ ] `web/pdf/{{DATE}}_daily-report.pdf` 존재 (rsync 대상)
- [ ] 페이지 ≥ 13 (EN 6+ + KO 6+ + S09 추가분)
- [ ] 파일 크기 ≥ 200KB
- [ ] PDF 전반부 (1–6p): 한국어판 헤더 없음 (EN 전용)
- [ ] PDF 후반부: `한국어판` 또는 `한국어 에디션` 헤더 존재

## 산출 후

PDF URL: `https://aipoweratlas.com/pdf/{{DATE}}_daily-report.pdf`
→ Step 4 Pro 뉴스레터의 `{{PDF_LINK}}` 변수에 주입.
