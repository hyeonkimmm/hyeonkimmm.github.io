---
title : "AWS serverless architecture"
category :
    - AWS
    - Server less
tag :
    - Server less
toc : true
published : true
---
## 전체 아키텍쳐
---
![hosting](/image/lecture/hosting.png)
---
![hosting](/image/lecture/dynamoDB.png)
---
![hosting](/image/lecture/business_logic.png)
---
![hosting](/image/lecture/alarm.png)
---
![hosting](/image/lecture/whole_logic.png)

## 실습환경 준비
[WSL To Windows Operation System](https://www.44bits.io/ko/post/wsl2-install-and-basic-usage)
     - Windowds 에서 Ubuntu Linux 설치에 관해 아주 자세히 나와 있음.

### docker 
- 위의 링크로 설치를 완료 한 후
- docker로 nginx web server 설정
- 고정 ip , 127.0.0.1 로 접속 가능

![docker](/image/lecture/docker_ps.png)
- docker 정보 확인


![ngix](/image/lecture/ngix.png)
- ip addr show eth0에서 확인한 172.17.21.105 ip로 접속

![ngix](/image/lecture/ngix_ip.png)
- 127.0.0.1 로 접속

https://github.com/microsoft/WSL/issues/4150