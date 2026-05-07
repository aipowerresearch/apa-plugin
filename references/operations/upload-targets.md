# Upload Targets — 호스트 설정

`uploader` 스킬이 참조하는 호스트 정의. 추후 호스트 추가·교체는 이 파일만 수정.

## 활성 호스트

```yaml
- name: fastcomet-prod
  host: 139.162.105.223
  user: intesolk
  port: 22
  remote_path: /home/intesolk/aipoweratlas.com
  ssh_key: ssh/id_rsa
  active: true
  default: true
  notes: 현재 운영. 14개 사이트 호스팅.
```

## 예정 호스트 (예시)

```yaml
- name: hetzner-prod
  host: <ip-tbd>
  user: <username>
  port: 22
  remote_path: /var/www/aipoweratlas
  ssh_key: ssh/hetzner_id_rsa
  active: false
```

## 추가 사이트 (멀티사이트)

```yaml
- name: promptrek
  host: 139.162.105.223
  user: intesolk
  port: 22
  remote_path: /home/intesolk/promptrek.kr
  ssh_key: ssh/id_rsa
  active: true
  default: false
```

## 사용 명령

- `/apa:upload` → default 호스트로 web/ 업로드
- `/apa:upload --target=fastcomet-prod` → 특정 호스트
- `/apa:upload --folder=web/pdf` → 특정 폴더만
- `/apa:upload --target=promptrek --folder=outputs/blog` → 호스트+폴더
