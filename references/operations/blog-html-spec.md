# Blog HTML Canonical Template — APA

이 파일은 모든 블로그 포스트(`web/blog/posts/*.html`) 생성 시 반드시 따라야 할 표준 nav/CSS/JS 템플릿이다.

**문제 배경:** 2026-03-28 ~ 2026-04-22 기간에 일부 포스트가 단순화된 nav(메뉴/구독/테마토글 누락)로 생성되어 사이트 일관성이 깨졌다. 2026-04-22 일괄 표준화 후 이 reference로 재발 방지.

---

## 1. 절대 규칙 (체크리스트)

블로그 HTML 생성 시 다음 4개 요소가 모두 포함되어야 한다:

1. ✅ `apa_favicon.png` — `<head>` 내 favicon 링크 2종 + nav-logo 안 22px 이미지
2. ✅ 메뉴 링크 4개 — Blog (active) / 10-Layer Map / Weekly / About
3. ✅ `theme-toggle` 버튼 — 라이트/다크 모드 토글 + localStorage 'apa-theme'
4. ✅ `nav-cta` Subscribe 버튼 — `/#subscribe` 링크 (KO는 "구독", EN은 "Subscribe")

검증 명령:
```bash
for f in web/blog/posts/*.html; do
  for k in theme-toggle nav-cta "10-Layer Map" apa_favicon; do
    grep -q "$k" "$f" || echo "MISSING $k in $f"
  done
done
```
출력이 비어 있어야 통과.

---

## 2. `<head>` 요소 (favicon)

`<meta charset="UTF-8">` 바로 다음 줄에 추가:

```html
  <link rel="icon" type="image/png" href="/images/apa_favicon.png">
  <link rel="apple-touch-icon" href="/images/apa_favicon.png">
```

---

## 3. `<nav>` 블록 (표준)

`{en_url}`, `{ko_url}`, `{en_active}`, `{ko_active}`, `{theme_title}`, `{subscribe}` 치환:

- EN 파일: `en_active=" active"`, `ko_active=""`, `theme_title="Toggle theme"`, `subscribe="Subscribe"`
- KO 파일: `en_active=""`, `ko_active=" active"`, `theme_title="테마 전환"`, `subscribe="구독"`
- URL 형식: `/blog/posts/ai-power-atlas-{YYYY-MM-DD}-{layer}-{en|ko}.html`

```html
<nav>
  <div class="nav-inner">
    <a href="/" class="nav-logo">
      <img src="/images/apa_favicon.png" alt="APA" style="width:22px;height:22px;object-fit:contain;">
      <span style="color:var(--accent);">AI</span> Power Atlas
    </a>
    <div style="display:flex;align-items:center;gap:24px;">
      <div style="display:flex;align-items:center;gap:20px;">
        <a href="/blog/" style="font-size:13px;color:var(--accent);font-weight:600;">Blog</a>
        <a href="/layers/" style="font-size:13px;color:var(--text2);">10-Layer Map</a>
        <a href="/weekly/" style="font-size:13px;color:var(--text2);">Weekly</a>
        <a href="/about/" style="font-size:13px;color:var(--text2);">About</a>
      </div>
      <div class="lang-selector"><a href="{en_url}" class="lang-btn{en_active}">EN</a><div class="lang-divider"></div><a href="{ko_url}" class="lang-btn{ko_active}">KO</a></div>
      <button id="theme-toggle" class="theme-toggle" title="{theme_title}">&#9728;&#65039;</button>
      <a href="/#subscribe" class="nav-cta">{subscribe}</a>
    </div>
  </div>
</nav>
```

---

## 4. `<style>` 추가 블록 (테마 토글용)

`</style>` 바로 위에 삽입:

```css
    :root { color-scheme: dark; }
    body.light-mode {
      --bg: #f8f8fc; --bg2: #f0f0f8; --bg3: #e8e8f4;
      --border: rgba(0,0,0,0.08); --border2: rgba(0,0,0,0.12);
      --text: #0a0a1a; --text2: #404060; --text3: #8080a0;
    }
    .theme-toggle {
      background: none; border: 1px solid var(--border2);
      border-radius: 6px; padding: 4px 8px; cursor: pointer;
      color: var(--text3); font-size: 16px; line-height: 1;
      transition: all 0.2s; margin-left: 8px;
    }
    .theme-toggle:hover { color: var(--text); border-color: var(--text3); }
    body.light-mode nav { background: rgba(248,248,252,0.92); }
```

---

## 5. `</body>` 직전 JS

```html
<script>
(function(){
  var t=document.getElementById('theme-toggle');
  var saved=localStorage.getItem('apa-theme');
  if(saved==='light'){document.body.classList.add('light-mode');t.textContent='\uD83C\uDF19';}
  t.addEventListener('click',function(){
    document.body.classList.toggle('light-mode');
    var isLight=document.body.classList.contains('light-mode');
    t.textContent=isLight?'\uD83C\uDF19':'\u2600\uFE0F';
    localStorage.setItem('apa-theme',isLight?'light':'dark');
  });
})();
</script>
```

---

## 6. 참조 파일

표준 형식을 가장 잘 따르는 reference 포스트:
- `web/blog/posts/ai-power-atlas-2026-04-17-l9l10-en.html` (EN 표준)
- `web/blog/posts/ai-power-atlas-2026-04-17-l9l10-ko.html` (KO 표준)

새 포스트 생성 시 이 두 파일을 복사 후 본문/메타데이터만 교체하는 방식 권장.
