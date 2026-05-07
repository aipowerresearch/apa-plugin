# APA Plugin — Operations Guide

## 수정 절차

1. 이 대화창(플러그인 유지보수 전용)에서 수정 지시
2. Claude가 GitHub API로 직접 push
3. 새 Claude 세션 시작 시 최신 플러그인 자동 로드

## 버전 관리 (semver)

| 변경 유형 | 버전 올림 | 예시 |
|-----------|-----------|------|
| 새 스킬·커맨드 추가 | minor | 2.1.0 → 2.2.0 |
| 버그 수정·프롬프트 조정 | patch | 2.1.0 → 2.1.1 |
| 구조 변경·비호환 | major | 2.1.0 → 3.0.0 |

버전은 `.claude-plugin/plugin.json`의 `version` 필드를 직접 수정.

## 브랜치 전략

- `main` — 안정 운영 버전 (직접 push)
- 대규모 변경 시: feature 브랜치 → PR → main merge

## 보안 규칙

- PAT, SSH 키, 서버 자격증명은 절대 commit 금지
- `.gitignore`에 `ssh/`, `.env`, `*.pem`, `id_rsa` 포함
- 운영 토큰은 GitHub Settings → Developer Settings에서 관리

## v2.2.0 로드맵

`outputs/_logs/v2.2-roadmap-memo.md` 참조.

## 저장소 정보

- GitHub: https://github.com/aipowerresearch/apa-plugin
- 작성자: AI Power Research · https://aipoweratlas.com
- 라이선스: Proprietary (Private repository)
