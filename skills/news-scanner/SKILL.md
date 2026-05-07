---
name: news-scanner
description: AI 뉴스 1차 자료 수집. 트리거 — "뉴스 수집", "오늘 뉴스", "news scan", "scan sources", "/apa:scan", 또는 파이프라인 Step 1 자동 호출.
---

오늘 날짜·요일을 확인하고 해당 요일의 집중 레이어에 맞춰 다국어 1차 자료를 수집한다.

## 입력
- 날짜 (YYYY-MM-DD 또는 자연어; 미지정 시 오늘)
- 언어 (en, ko; 향후 ja/zh/es/de/fr/pt/ar 추가 시 동일 패턴)

## 요일 → 레이어
| 요일 | 레이어 |
|---|---|
| Mo | L1+L2 |
| Tu | L3+L4 |
| We | L5+L6 |
| Th | L7+L8 |
| Fr | L9+L10 |
| Sa | 전체 보완 |
| Su | Synthesis |

## 절차
1. references/scanner/layer-keywords-<lang>.md 로드 → 검색 키워드 확정
2. references/scanner/source-list-<lang>.md 의 Tier 1/2/3 소스에서 수집
3. references/scanner/scanner-supplement.md 5규칙 적용 (Key Figure, MCP/Agent, Prediction, Confidence, Baseline)
4. references/framework/key-figures.md 의 ★★★ 인물 별도 추적
5. 직전 동일 레이어 source-notes 비교 → 신호 변화 기록

## 산출물
`outputs/sources/<lang>/YYYY-MM-DD_<DoW>_source-notes_<lang>.md`

## 완료 조건
- 각 언어별 소스 ≥ 5건 (한국어는 KR-specific 섹션 별도)
- Power Score 계산용 메타데이터 포함
