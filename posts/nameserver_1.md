# Nameserver

- Written in Jan. 05. 2021
- Authored by Jaycol Kim <jaycol@gmail.com>

## 개요

- 네임서버는 DNS 서버의 유형 중 한 가지, 모든 DNS 레코드를 저장한다.
- 대부분 다수의 네임서버를 두어 안정성을 높임

### Record

- NS
  - 도메인의 네임서버를 바꿔야할 경우 본 레코드를 수정해야 한다.
- A
  - Address Mapping Records 레코드로서, 서브도메인
  - DNS에 저장되는 정보의 타입으로, 도메인 주소와 서버의 IP 주소를 직접 매핑시키는 방법
  - 'domain.com       xxx.xxx.xxx.xxx'
- AAAA
  - IPv6 주소체계와 연결하기 위한 레코드
  - 'domain.com       001:0bd9:0000:0000:0000:0000:2158:64ab'
- CNAME
  - 별칭, Canonical NAME
  - Canonical Name의 약자로 도메인 주소를 또 다른 도메인 주소로 매핑시키는 타입
  - IP 주소가 자주 변경되는 환경에서 유리하나, DNS 정보를 여러번 요청해야하는 단점이 있다.
  - 'domainA.com      domainB.com'
- SOA
  - Start of Authority의 약어로, 도메인의 모든 정보와 권한을 의미하며, SOA 레코드가 없을 경우 다른 레코드를 등록할 수 없다.
- MX
  - Mail eXchanger 레코드
  - 메일서버의 연동 시 메일의 소유를 확인하는 레코드
- TXT
  - 텍스트
  - 화이트도메인 등록과 같이 SPF 레코드 및 도메인 인증관련된 레코드를 추가할 때 사용
- SPF
  - Sender Policy Framework
  - TXT 레코드 안에서 사용되며, 메일 스푸핑을 방지하는데 사용되는 레코드
  - 특정 사업체(네이버, 다음, 구글)의 메일을 보냈을 때 반송이 안되는 경우가 있는데, 이는 대부분 SPF 등록이 안되어있는 경우에 발생
- SRV
  - 서비스 종류 및 포트 번호를 지정함으로서 서비스의 위치를 저장하기 위해 사용

### ISC-dhcp-Server vs dnsmasq

- ISC-dhcp-server는 현재 일반적으로 데몬으로서 사용된다.
- dnsmasq 장점
  - dnsmasq가 dhcp 서버로서 사용되려면, 로컬 호스트네임은 즉시 자동적으로 붙려진다
  - dnsmasq가 설치하기 쉽고, 다루기 쉽낟.
  - ISC-dhcp-server + Bind 조합보다 10배정도 덜 메모리와 CPU 점유율을 나타낸다.
  - ISC 데몬의 몇몇 설정에서 커널 방화벽 규칙을 우회하곤 하는데 dnsmasq는 그렇지 않다.
- dnsmasq 단점
  - Failsafe 시
