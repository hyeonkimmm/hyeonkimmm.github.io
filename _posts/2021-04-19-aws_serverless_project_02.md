---
title : "AWS 서버리스 프로젝트"
category :
    - AWS
    - Server less
tag :
    - Server less
toc : true
published : true
---
## 실습환경준비
- docker alias 환경 설정
- dkr ='docker' , dkrp='docker-compose'
![alias](/image/lecture/02/alias.png)

```
dkr run -it amazonlinux bash # amazonlinux bash 환경 접속
yum update -y # python3 설치 위한 yum update
yum install python3 -y 

# virtualenv 설치
pip3 install virtualenv

# which install
yum install which

mkdir venv && cd venv
virtualenv -p /usr/bin/python3 py37

source py37/bin/activate # 가상환경 진입

deactivate # 가상환경에서 나오기
```

