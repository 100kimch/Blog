# Firewall

- Written in Nov. 26. 2021
- Authored by Jaycol Kim <jaycol@gmail.com>

## Firewalld

- CentOS 6에서 iptables 사용하여 방화벽 규칙을 적용했으나 CentOS 7 부터는 Firewalld로 방화벽 규칙을 적용하고 제어한다.

### Run Time

- 방화벽 설정 내용을 일시적으로 적용하고자 할 경우 런타임(Run Time)을 사용한다. Firewalld 설정을 다시 불러오거나 시스템을 재시작할 경우 설정 내역이 삭제됨

### Permanent

- 방화벽 설정을 영구적으로 적용할 경우 사용한다. 런타임 설정은 설정 내역 확인이 어려우므로 영구적 적용을 통해 방화벽 정책을 관리하는 것이 가독성이 높다.

### Zone

- Firewalld는 영역(Zone)에 따라 신뢰도를 지정할 수 있다. 접속을 허용하거나 거부해야 할 경우 효율적으로 사용할 수 있다.

### Service

- Firewalld에서 ftp, http, https 등 서비스를 프로토콜 포트로 명확하게 지정하여 사용할 수 있다. CUI에서는 서비스 추가, 수정 방법을 제공하지 않으며, /usr/lib/firewalld/services/`service-name`.xml에 있는 파일을 참조하여 /etc/firewalld/services에 Firewalld 설정 파일을 편집해야 한다.

