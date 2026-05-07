# Step 6 — 블로그 HTML 변환 프롬프트

## 역할
04-24 표준 블로그 HTML을 복사해 본문/메타데이터만 교체. 8개 필수 요소 (JSON-LD schema · theme-toggle · nav-cta · apa_favicon · scroll-top · post-nav · article-header · article-body) 누락 금지.

## 입력
- 블로그 마크다운: `outputs/blog/{{DATE}}_{{LAYER_SLUG}}_blog_{ko,en}.md`
- 표준 템플릿: `references/templates/blog-html/STANDARD_blog_{ko,en}.html` (2026-04-24 기준)
- 전날 블로그 HTML: `web/blog/posts/ai-power-atlas-{{PREV_DATE}}-*-{ko,en}.html` (next 링크 패치 대상)

## 출력 (2파일)
- `web/blog/posts/ai-power-atlas-{{DATE}}-{{LAYER_SLUG}}-ko.html`
- `web/blog/posts/ai-power-atlas-{{DATE}}-{{LAYER_SLUG}}-en.html`

## 절대 시그니처 (검수 통과용)

각 파일이 반드시 갖춰야 할 요소 (verify_daily.sh 8요소 체크):

1. **JSON-LD schema**: `<script type="application/ld+json">` NewsArticle 메타데이터
2. **theme-toggle**: 라이트/다크 모드 버튼 + localStorage `apa-theme`
3. **nav-cta**: Subscribe 링크 (`구독` KO / `Subscribe` EN)
4. **apa_favicon**: `<head>` 2줄 + nav-logo `<img>` 22px
5. **#scroll-top**: 우측 하단 스크롤 버튼 + JS 토글
6. **post-nav**: prev (전날) + next (오늘)
7. **article-header**: h1 + author-block + article-meta + article-desc
8. **article-body**: 4–6 h2 섹션 + blockquote + hr + 6개월 함의 단락

## 변수 치환

표준 템플릿(예: `STANDARD_blog_ko.html`) 복사 후 다음 6개 영역 교체:

| 영역 | 출처 |
|------|------|
| JSON-LD `headline` | 오늘 블로그 KO/EN 제목 |
| JSON-LD `description` | 오늘 frontmatter summary |
| JSON-LD `url` `datePublished` `dateModified` | 오늘 URL + 날짜 |
| JSON-LD `articleSection` | 예: "AI Power Atlas Daily Intelligence" |
| `<title>` 태그 | 오늘 블로그 제목 |
| `<meta name="description">` `<meta property="og:title">` `<meta property="og:description">` | 오늘 frontmatter |
| 모든 `2026-04-24-l9l10-{ko,en}` URL/슬러그 | `{{DATE}}-{{LAYER_SLUG}}-{ko,en}` |
| `lang-selector` 짝 파일 링크 | KO ↔ EN 짝 파일 |
| `<h1>` 메인 타이틀 | 블로그 KO/EN 제목 |
| `article-meta`의 `article-date`·`article-tag` | 오늘 날짜·집중 레이어 |
| `article-desc` | 오늘 summary |
| `article-body` 본문 | 블로그 마크다운을 HTML로 변환 (4–6 h2, blockquote, hr, 6개월 함의) |
| `post-nav` prev | 전날 포스트 URL + 제목 |
| `post-nav` next | 빈 상태 (`<div class="post-nav-item next" style="visibility:hidden"></div>`) |

## 전날 포스트 next 링크 패치 (절대)

오늘 블로그 HTML 생성 후, 전날 KO + EN 블로그 HTML의 next 링크를 오늘 포스트로 업데이트:

```
<div class="post-nav-item next" style="visibility:hidden"></div>
```
→
```
<a href="/blog/posts/ai-power-atlas-{{DATE}}-{{LAYER_SLUG}}-ko.html" class="post-nav-item next"><span class="post-nav-label">다음 글 →</span><span class="post-nav-title">{{TODAY_TITLE_KO}}</span></a>
```

EN 파일도 동일 패턴 ("Next →" + EN 제목).

## 자가 검수 체크리스트

`scripts/verify_daily.sh {{DATE}} --skip-server` 의 `[Step 6] 블로그 HTML 검수` 블록이 다음을 모두 PASS:

- [ ] 블로그 HTML KO 존재
- [ ] 블로그 HTML EN 존재
- [ ] 8개 필수 요소 (KO 파일)
- [ ] 8개 필수 요소 (EN 파일)
- [ ] 전날 KO 블로그 next → 오늘 포스트 링크 OK
- [ ] 전날 EN 블로그 next → 오늘 포스트 링크 OK

## 산출 후

Step 7 (블로그 인덱스·아카이브·인텔리전스 갱신)으로 진행.
