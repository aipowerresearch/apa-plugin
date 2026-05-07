# AI Power Atlas — Publishing Schedule (EST 기준)

> 발행 시간 기준: **EST (미국 동부 표준시, UTC-5)**
> EST = 미국 동부 겨울 시간. 여름(3월~11월)은 EDT(UTC-4)로 자동 1시간 앞당겨짐.
> Created: 2026-03-23 | Owner: APA Operations

---

## 1. 미국 시장 최우선 — 발송 시간 선택 근거

**목표 발송 시간: 오전 6:00 AM EST (= 11:00 AM UTC = 오후 8:00 PM KST)**

### 왜 6 AM EST인가?

| 비교 시간대 | 적합성 | 이유 |
|------------|--------|------|
| 4 AM EST | ❌ 부적합 | 도달률 낮음 — 대부분 수신함에서 묻힘 |
| **6 AM EST** | ✅ **최적** | 미국 기술/금융 전문가의 "출근 전 뉴스레터 읽기" 피크 타임 (Morning Brew, The Hustle 등 참조). AI·반도체 관련 고관여 독자층이 가장 활성화되는 시간. |
| 7 AM EST | ✅ 차선 | 경쟁 뉴스레터가 집중되는 시간대. 6 AM이 우위. |
| 9 AM EST | ❌ 비추천 | 업무 시작 후 수신함이 이미 가득 찬 상태 — 오픈율 저하. |

### 한국 구독자에 대한 고지 원칙

> 한국 구독자 수신 시각: **오후 8:00 PM KST (여름/EDT 기준: 오후 7:00 PM KST)**

이는 저녁 식사 후 시간대로 콘텐츠 소비에 적합하다. 다만, APA는 정보 수집 소스의 최우선이 미국 시장임을 명시한다:

> "APA는 세계 AI 산업의 중심인 미국 시장 정보를 최대한 반영한 분석을 매일 저녁 제공합니다. 미국 기준으로 하루가 마감된 뒤 전 세계 독자에게 동시에 발행되는 구조입니다."

---

## 2. 일간 파이프라인 타임라인 (Daily Timeline)

모든 시각은 **EST (UTC-5)** 기준. 괄호 안은 EDT(UTC-4) / KST(UTC+9).

```
┌─────────────────────────────────────────────────────────────────┐
│              AI POWER ATLAS — Daily Publishing Timeline          │
│                         (EST 기준)                               │
└─────────────────────────────────────────────────────────────────┘

  3:00 AM EST  (4:00 AM EDT / 5:00 PM KST)
  ├── 🤖 [자동] 파이프라인 시작
  │   Step 1: 뉴스 스캔 (scan)
  │   Step 2: 8섹션 리포트 생성 (generate)
  │   Step 3: 뉴스레터 KO+EN HTML 생성 (format-newsletter)
  │   Step 4: 블로그 KO+EN .md 생성 (format-blog)
  │   Step 5: 아카이브 인덱스 업데이트 (archive)
  │   Step 6: 소셜 포스트 생성 (social)

  5:00 AM EST  (6:00 AM EDT / 7:00 PM KST)
  ├── ✅ [자동 완료 목표] 모든 산출물 생성 완료
  │   출력 경로: APA/outputs/[reports·newsletters·blog·social]/

  5:30 AM EST  (6:30 AM EDT / 7:30 PM KST)
  ├── 🌐 [마감] 블로그 & 웹사이트 업로드 데드라인
  │   · 플랫폼: FastComet (cPanel 직접 업로드) 또는 Netlify (Git push)
  │   · 업로드 대상: blog_en.md → 영문 블로그 페이지
  │             newsletter_en.html → 웹사이트 아카이브 페이지

  6:00 AM EST  (7:00 AM EDT / 8:00 PM KST)
  └── 📧 [발송] 뉴스레터 발송 (beehiiv 예약 발송)
      · 영어 뉴스레터 → 전체 구독자 (EN 우선)
      · 한국어 뉴스레터 → KO 구독자 세그먼트
```

---

## 3. 주간 종합 리포트 타임라인 (Weekly Timeline)

```
  토요일 10:00 PM EST  (일요일 11:00 PM EDT / 일요일 12:00 PM KST)
  ├── 🤖 [자동] 주간 종합 파이프라인 시작 (weekly-synthesis)

  일요일 12:00 AM EST  (1:00 AM EDT / 2:00 PM KST)
  ├── ✅ 주간 종합 산출물 완료

  일요일  8:00 AM EST  (9:00 AM EDT / 10:00 PM KST)
  └── 📧 주간 종합 뉴스레터 발송 (beehiiv 예약)
```

---

## 4. 예약 작업 설정값 (Scheduled Task Config)

### ai-power-atlas-full-daily

| 항목 | 현재 (변경 전) | 권장 (변경 후) |
|------|--------------|--------------|
| 실행 시각 | 7:00 AM KST | **5:00 PM KST** |
| UTC 기준 | 22:00 UTC (전날) | **08:00 UTC** |
| EST 기준 | 10:00 PM EST (전날) | **3:00 AM EST** |
| Cron (KST) | `0 7 * * 1,2,3,4,5,6` | **`0 17 * * 1,2,3,4,5,6`** |

> **참고**: KST 오후 5시 = UTC 오전 8시 = EST 오전 3시 = EDT 오전 4시 (여름)

### ai-power-atlas-weekly

| 항목 | 현재 | 권장 |
|------|------|------|
| 실행 시각 | 8:00 AM KST 일요일 | **10:00 PM KST 토요일** |
| UTC 기준 | 23:00 UTC 토요일 | **13:00 UTC 토요일** |
| EST 기준 | 6:00 PM EST 토요일 | **8:00 AM EST 토요일** |
| Cron (KST) | `0 8 * * 0` | **`0 22 * * 6`** |

---

## 5. beehiiv 예약 발송 설정

| 뉴스레터 | 발송 시각 | beehiiv 설정값 |
|---------|---------|--------------|
| 일간 EN | 6:00 AM EST 매일 (월~토) | Send Time: 6:00 AM, Timezone: US/Eastern |
| 일간 KO | 6:00 AM EST 매일 (월~토) | Send Time: 6:00 AM, Timezone: US/Eastern |
| 주간 EN | 8:00 AM EST 일요일 | Send Time: 8:00 AM Sunday, Timezone: US/Eastern |
| 주간 KO | 8:00 AM EST 일요일 | Send Time: 8:00 AM Sunday, Timezone: US/Eastern |

> beehiiv은 "US/Eastern" 타임존 설정 시 EDT/EST 자동 전환됨.

---

## 6. 웹사이트 업로드 절차 (FastComet / Netlify)

### FastComet (cPanel)

```
1. 생성된 blog_en.md → HTML 변환 후 /blog/YYYY-MM-DD-slug/ 폴더에 업로드
2. newsletter_en.html → /newsletter/archive/YYYY-MM-DD/ 업로드
3. index 페이지 latest-post 링크 업데이트
데드라인: 5:30 AM EST
```

### Netlify (Git-based)

```
1. APA/outputs/blog/ → Git commit → Push to main
2. Netlify 자동 빌드 트리거 (평균 1~3분 소요)
3. 업로드 완료 확인: netlify.app 도메인 접속 테스트
데드라인: 5:30 AM EST (빌드 시간 포함)
```

---

## 7. 타임존 변환 레퍼런스

| 이벤트 | EST (겨울) | EDT (여름) | UTC | KST |
|--------|-----------|-----------|-----|-----|
| 파이프라인 시작 | 3:00 AM | 4:00 AM | 8:00 AM | 5:00 PM |
| 산출물 완료 목표 | 5:00 AM | 6:00 AM | 10:00 AM | 7:00 PM |
| 웹 업로드 마감 | 5:30 AM | 6:30 AM | 10:30 AM | 7:30 PM |
| 뉴스레터 발송 | 6:00 AM | 7:00 AM | 11:00 AM | 8:00 PM |

> EST/EDT 전환일: 매년 3월 두 번째 일요일(봄 앞으로) / 11월 첫 번째 일요일(가을 뒤로)
> 2026년: 3/8(토) → EDT 시작 / 11/1(일) → EST 복귀

---

*Last updated: 2026-03-23 | AI Power Atlas Operations*
*연관 파일: apa-operations-playbook.md · source-selection-criteria.md*
