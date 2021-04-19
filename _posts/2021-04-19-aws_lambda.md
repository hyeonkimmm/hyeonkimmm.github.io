---
title : "AWS 서버리스"
category :
    - AWS
    - Server less
tag :
    - Server less
toc : true
published : true
---
## 서버리스
- 논리적인 서버가 없다는 뜻
- 물리적인 서버가 있지만 서버를 관리하는 주체가 우리가 아니다.

### 클라우드 컴퓨팅의 역사
- 사용자 증가 -> 본래 업무보다 서버 확장 등 리소스에 더 시간을 투자하게 됨.
- 인프라 관리에 대해 전문적으로 하는 Data Center를 구축 하게 됨
![idc](/image/lecture/IDC.png)
- 이러한 다양한 설계가 필요하다 보니 배보다 배꼽이 더 커지는 부담이 생김

- 가상서버를 고객에게 임대해주면서 cloud computing을 가능하게 함.

### Iaas(infrastructure as a Service)
### PaaS(Platform as a Service)

![idc](/image/lecture/msa.png)
### Faas(Function as a Service)
![faas](/image/lecture/faas.png)
- 함수단위로 서비스함
- 확장성 이점
- 신속하고 효율적

### 서버리스의 개념
> **비즈니스 로직에 집중**하고, **서버운영으로부터 자유**로워지는 **클라우드 컴퓨팅 환경**.
    
### 서버리스의 한계점 및 장단점

- 서버리스의 장점
    - 인프라 관리 감소 , 확장성
    - application traffic이 얼마든 세팅값이 커스터마이징 하는 것만으로 사용할 만큼 사용 가능
    - 빠른 아웃풋
        - 비지니스 로직에만 집중 가능.
        - Faas 같은 경우 코드만 제공하면 원하는 시스템 구축 가능
    - 경제적(비용 절감)
        - 렌트카와 비슷한 느낌(브레이크 후 정차하면 시동이 꺼지는)
        - 사용하지 않는 idle 상태에서 물리적 비용 지불 X
- 서버리스의 단점
    - 낮은 호환성과 높은 종속성
    - 운영체제나 runtime이 고정되어 있음
        - lambda와 같은 경우 java , nodejs , python 정도 지원
        - 크기제한 , 최대 메모리, 최대 처리 가능 시간, 임계치
        - 자원의 형태가 무한한 것은 아님. **제약상태 준수** 필수
    - 한정적
        - running time이 너무 긴 서비스는 어려울 수 있음
        - debug , monitoring system 이 어려움
    - 무상태 status less 한 기능으로 구현 되어야 함

### 서버리스에 적합한 시스템?
![idc](/image/lecture/serverless.png)

## AWS
- 가용영역에 따라 속도 및 지출되는 비용이 달라지므로
- **`가용영역`** 에 대한 필수적인 이해가 필요.
![idc](/image/lecture/aws_infra.png)

1. **Region**
    - aws가 이용되는 지역 - 22개
    - 가용영역의 집합체
    - 대륙간 네트워크 통신 -> Global Networking
2. **Availability Zones**
    - 물리적으로 분리 되어 있음
    - 고대역폭 , 저지연 네트워킹 , 완전 이중화
    - 대기시간이 굉장히 짧음
    - 고가용성
    - 이중화
        - 가용영역이 최소 두개
        - 두 가용영역 중에 하나가 망가져도 돌아갈 수 있게
        - 두번째 가용영역에 복제
    - 각 캐시서버에서 복제를 하여 빠른 속도 가능
