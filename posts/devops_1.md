# DevOps

## DevOps: 문화 + 기술

## 빌드, 배포

- CI

  - 개발 -> 테스트 -> 보안체크 -> 릴리즈

- CD
  - 배포단계 -> 운영배포

## CI/CD란

- "자동화"
  - 개발 프로세스를 개선 및 지동화하는 것

## CI/CD Pipeline

- 새 버전의 소프트웨어를 제공하기 위해 수행해야 할 일련의 단계

### Pipeline tools

- 기존의 전통적인 파이프라인 툴: Jenkins
  - Source Build / Scan / Deploy

## Jenkins는 쿠버네티스 기반에 최적화되어있는가?

- yaml 파일로 관리되지 않음 / CI/CD도 컨테이너 기반의 클라우드 네이티브 기술이 접목이 되어야 하는데 젠킨스는 그렇지 않다.

## Openshift Pipeline

- Openshift Tekton / GitOps를 이용
- Tekton 파이프라인 기반
- Kubernetes Native 선언적 CI/CD

## Tekton

- 컨테이너 기반 클라우드 네이티브 CI/CD
- 쿠버네티스를 위한 빌드
- 주문형 확장
- 안전한 파이프라인 실행
- DevOps 지원
- Yaml 파일, 이미지 업로드 가능

### 구성

#### Step

- Yaml 파일로 구성되어있는 Task 내의 일하는 단위
- 컨테이너에서 명령 또는 스크립트 실행
- 쿠버네티스 컨테이너 사양
  - Env vars
  - Volumes
  - Config Maps
  - Secrets

#### Task

- Step 들을 가지고 있는 List
- 특정한 Task 수행
- Step들은 순차적으로 수행하며, 재사용성을 가지고 있음

#### Pipeline

- Task들의 모음
- 반드시 순차적으로 수행하는 것은 아니며 조건을 걸어 동시성 여부를 정할 수 있음
- Task 실행 로직
  - Conditional
  - Retries

#### Workspace

- namespace 역할

### Tekton Hub

- Task 모음

### Tekton CLI

- 오픈소스
- VSCode, IntelliJ 지원

## GitOps

- Git: SSOT (단일 진실 공급원)
  - 여러 개의 복제본이 있지만 실제로 하나만 바라봄
- 선언적 코드로 구성
- Git 워크플로를 통한 작업

### GitOps 동작방식

- What you want (Git, 원하는 상태) -> CD -> What you have (현재상태)

### GitOps 이점

- 표준 워크플로 (Git Workflow)
- 확장된 보안성
  - 사전에 변경 사항 검토 및 조치 수행
- 가시성과 기록
  - Git 기록을 통해 클러스터 변경사항 캡처 및 수행 가능
- 다중 클러스터 일관성

## DevOps 어플리케이션 배포 모델

- Source Git Repo -> CI -> Image Registry -> Kubernetes
- Config Git Repo -> CD -> (push/pull) -> Kubernetes

## Openshift GitOps

- 선언적 YAML 파일로 관리
- Git 소스를 통해 멀티클러스터링 구축 가능
- 자동화된 ArgoCD 설치 및 업그레이드
- 배포 및 환경에 대한 통찰력

## ArgoCD

- CNF에서 관리
- K8S 배포 툴
- Argo CD 모니터링

### 동기화 운영

- ArgoCD에는 사용된 git repo의 local cache가 존재
- 동기화가 발생하면 git ls-remote 수행
- 원하는 구성이 실행중인 구성과 비교
- 캐시를 백업할 필요는 없음
  - local cache가 없으면 git clone 실행
