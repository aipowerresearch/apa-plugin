---
name: uploader
description: 범용 SSH/SFTP/rsync 업로드 (FastComet/Hetzner/AWS 등). 트리거 — "업로드", "upload", "deploy", "/apa:upload", 파이프라인 Step 11 자동 호출.
---

호스트 중립 업로드 스킬. 호스트 설정은 `references/operations/upload-targets.md`에서 관리.

## 동작
1. `references/operations/upload-targets.md`에서 활성 호스트 정보 로드
2. SSH 키 위치 자동 탐색 (작업 폴더의 `ssh/id_rsa`)
3. SSH 키 권한 600 보정
4. rsync로 `web/` 또는 지정 폴더 업로드 (`--chmod=D755,F644`)
5. 서버 권한 일괄 보정
6. 전송된 파일 수 보고

## 호스트 추가 방법
`references/operations/upload-targets.md`에 새 항목 추가:
```yaml
- name: hetzner-prod
  host: <ip>
  user: <username>
  port: 22
  remote_path: /var/www/aipoweratlas
  ssh_key: ssh/hetzner_id_rsa
  active: true
```

## 사용 예
- `/apa:upload` — 기본 활성 호스트로 web/ 업로드
- `/apa:upload --target=hetzner-prod` — 특정 호스트
- `/apa:upload --folder=web/pdf` — 특정 폴더만
