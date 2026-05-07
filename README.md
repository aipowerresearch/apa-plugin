# AI Power Atlas Plugin

**Version**: 2.2.0  
**Author**: AI Power Research  
**Homepage**: https://aipoweratlas.com

## Overview

AI Power Atlas(APA) 플러그인 — 10-Layer 권력 흐름 프레임워크 기반 일간/주간/심층분석 인텔리전스 자동 생성·발행 시스템.

## Features

- 13-step 일간 파이프라인 (수집 → 리포트 → PDF → 뉴스레터 → 블로그 → APV 품질 게이트 → 업로드)
- APV (Atlas Publication Validator): 12-point 인간 문체 품질 게이트
- 8섹션 리포트 (EN/KO 병행, 번역 충실도 검수)
- 뉴스레터 4종 (free/pro × EN/KO)
- 지식 베이스 일간/주간 갱신

## Installation

Cowork 또는 Claude Code에서 다음 명령 실행:

```
/plugin marketplace add aipowerresearch/apa-plugin
```

## Skills

| 스킬 | 설명 |
|------|------|
| `pipeline-runner` | 13단계 일간 파이프라인 전체 실행 |
| `report-writer` | 8섹션 일간 리포트 (EN+KO) |
| `apv-validator` | 12-point 인간 문체 품질 검증 |
| `newsletter-builder` | 뉴스레터 4종 생성 |
| `pdf-publisher` | PDF 3종 생성 |
| `blog-converter` | 블로그 MD+HTML + 인덱스 갱신 |
| `analysis-publisher` | Deep research analysis (3000+자) |
| `weekly-synthesizer` | 주간 종합 리포트 + 시나리오 트래커 |

## Changelog

### v2.2.0 (2026-05-08)
- `apv-validator` 스킬 신규 추가
- `pipeline-runner` 11단계 → 13단계 (Step 7 APV 게이트, Step 12 검수)
- `analysis-publisher` Phase 4.5 APV 게이트 추가
- `commands/daily.md` 13단계 기준 업데이트

### v2.1.0
- 초기 릴리스
