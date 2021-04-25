---
title : "AWS serverless 실습환경"
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

pip list
    # output
Package    Version
---------- -------
pip        21.0.1
setuptools 56.0.0
wheel      0.36.2

# 기존에 설치되었던 python이 보이지 않고, 가상환경에서 설치한 package만 보임

aws configure # access key 입력
# 정보 입력 이후
# 정보 입력 확인
cat ~/.aws/credentials
# 특정 profile에 따라 configure 다르게 입력 가능
aws configure --profile s3
```
- access key 
![access_key](/image/lecture/02/access_key.png)