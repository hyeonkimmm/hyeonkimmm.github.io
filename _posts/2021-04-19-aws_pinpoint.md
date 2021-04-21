---
title : "AWS Pinpoint tutorials"
category :
    - AWS
    - Pinpoint
tag :
    - Pinpoint
toc : true
published : true
---
## [Pinpoint Tutorials](https://docs.aws.amazon.com/ko_kr/pinpoint/latest/userguide/gettingstarted.html)
- AWS 사용 설명서를 보고 정리함
- Pinpoint 를 알려주고 설명하기 위함.
- 목적: 특정 사람들에게 보내는 광고 , 타겟팅 하는 광고
- [개발자 가이드](https://docs.aws.amazon.com/ko_kr/pinpoint/latest/developerguide/tutorials.html)

- AmazonPinpoint 메시지 보내기 시작 하기 위한 절차
- 고객 연락처 정보 추가 -> 특정 고객을 대상으로 하는 세그먼트 만들기
- 메시지 생성 및 캠페인 예약
- 캠페인 보내는 이후 캠페인의 수행 성과 확인 가능

---
### Pinpoint 콘솔
- Importing customer data from a file.
- Creating a segment that targets specific users based on their attributes.
- Creating an email campaign and scheduling it to be sent at a specific time.
- Viewing email delivery and response data by using the analytics dashboards that are built into Amazon Pinpoint.
파일에서 고객 데이터 가져오기
속성에 따라 특정 사용자를 대상으로 하는 세그먼트 생성
이메일 캠페인 생성 및 특정 시간에 전송되도록 예약
Amazon Pinpoint에 내장된 분석 대시보드를 사용하여 이메일 배달 및 반응 데이터 보기

---
### Step1 : Create and configure a project
![create_account](/image\AWS\pinpoint\create_project.png)
``` Json
# 아래와 같이 JSON 파일로 권한을 줘야 작동하는 것 처럼 보인다.
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ViewProject",
            "Effect": "Allow",
            "Action": "mobiletargeting:GetApps",
            "Resource": "arn:aws:mobiletargeting:region:accountId:*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "mobiletargeting:Get*",
                "mobiletargeting:List*"
            ],
            "Resource": [
                "arn:aws:mobiletargeting:region:accountId:apps/projectId",
                "arn:aws:mobiletargeting:region:accountId:apps/projectId/*",
                "arn:aws:mobiletargeting:region:accountId:reports"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "ses:Get*",
                "kinesis:ListStreams",
                "firehose:ListDeliveryStreams",
                "iam:ListRoles",
                "ses:List*",
                "sns:ListTopics",
                "ses:Describe*",
                "s3:List*"
            ],
            "Resource": "*"
        }
    ]
}
```
- 권한 받은 이후 create project page
![create_account](/image\AWS\pinpoint\create_project_2.png)

## Project list

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9d840fb2-11ae-41c7-8eb0-f8ec9b7bc414/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9d840fb2-11ae-41c7-8eb0-f8ec9b7bc414/Untitled.png)

## Segments list

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/107182cc-8e6c-4b44-a90c-942f0f3169a8/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/107182cc-8e6c-4b44-a90c-942f0f3169a8/Untitled.png)

### tc_hkim_segment

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c7062d5a-6178-4b03-9985-3b55348f3af4/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c7062d5a-6178-4b03-9985-3b55348f3af4/Untitled.png)

### s3_bucket_segment_file

- s3 bucket에서 불러와서 segment 등록 되는지 확인
- s3 bucket에서 segment 설정하려면 IAM role을 생성해서 추가 부여해줘야 함.

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1e10e46f-d303-451f-98be-ed3efd03ea77/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1e10e46f-d303-451f-98be-ed3efd03ea77/Untitled.png)

- csv s3 bucket에 업로드

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/52ae0e82-d2c1-49a3-bb6f-f14c3b6d2656/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/52ae0e82-d2c1-49a3-bb6f-f14c3b6d2656/Untitled.png)

- 자동 업데이트 되는지 확인하고자 campaign을 실행 하였으나 황솔희 사원님의 회사 메일로 전송되지 않음.

### s3 bucket v0.02

- 새로 업데이트 하고 다시 실행했으나 똑같이 황솔희 사원님의 메일로 전송되지 않음.,

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/edad7436-1af4-42f8-8624-11676f49f777/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/edad7436-1af4-42f8-8624-11676f49f777/Untitled.png)

### Pinpoint_sample_import

- 로컬에서 수정한 csv 파일(황솔희 사원님 email 추가)을 직접 올려서 새로운 segment 생성

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6055665c-24fe-453c-9c04-a6f64fb4f6bf/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6055665c-24fe-453c-9c04-a6f64fb4f6bf/Untitled.png)

### tc-KOR segment

- Criteria 때문에 메일로 보내지지 않는지 확인하고자 생성
- Company 이름과 country로 Criteria 조건을 걸었음

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0e4c7236-7423-441b-b5b1-a689da672d7e/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0e4c7236-7423-441b-b5b1-a689da672d7e/Untitled.png)

## Campaign list

- 총 실행했던 campaign list
- 다양하게 시도했으나 내 이메일에만 전송되는 issue가 있었음.

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5d25551e-15c5-45fc-ba11-eabe7739f993/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5d25551e-15c5-45fc-ba11-eabe7739f993/Untitled.png)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/21a0ab58-0dab-482c-87c9-1a7b0f778ff8/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/21a0ab58-0dab-482c-87c9-1a7b0f778ff8/Untitled.png)

- [ ]  tc_campaign 클릭시 상단의 오류 체크

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f1ef8c07-7147-4bf3-b4c9-f36c04b6aab3/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f1ef8c07-7147-4bf3-b4c9-f36c04b6aab3/Untitled.png)

### s3 bucket campaign

- s3 bucket의 csv 파일을 불러와서 알람이 가는지 testing하는 campaign
- 메일이 제대로 온 것 확인

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/93592c87-4d9d-4700-b2ef-9cc70d3bf1ad/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/93592c87-4d9d-4700-b2ef-9cc70d3bf1ad/Untitled.png)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d60a2b7a-49ea-438a-95bb-fc5374d78451/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d60a2b7a-49ea-438a-95bb-fc5374d78451/Untitled.png)

- 나에게 온 메일

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/fe428513-80a4-43fc-95d8-17997f721bb7/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/fe428513-80a4-43fc-95d8-17997f721bb7/Untitled.png)

### tc-campagin-v0.02

- 나머지 campagin은 모두 동일하게 진행됨
- 로컬에서 업데이트 후 Criteria 를 새롭게 조합한 segment를 생성하고 테스팅함
- 우측 campaign deliveries
    - Endpoints targeted
        - 2명 (아마 황솔희 사원님과 내가 그런 것 같음)
    - Endpoints processed
        - 1명 (메일이 나에게만 온 것 같음)
- campaign deliveries 의 내용을 보고 추측 하자면 , 아마 criteria는 제대로 맞게 들어간 것 같고, processed 가 나만 적용된 이유를 확인해 보아야 할 것 같음.
- [ ]  endpoints에 대해 정확하게 조사하기

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/fd0278d1-b493-4aa5-a6ee-2d7042dbcb38/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/fd0278d1-b493-4aa5-a6ee-2d7042dbcb38/Untitled.png)

## Push notifications

- 특정 segments한테 ad하는 또 하나의 방법인 notifications 방식을 시도해 보았음
- APNs, Baidu Cloud Push, ADM 등이 있었다.
- **그나마** 가장 친숙한 Firebase로 시작하기로 했다.
- Firebase Cloud Messaging(FCM) 이라는 도구가 있길래 추가해보았다.

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/22fef44f-9e48-4821-ab1e-879b4adc97f4/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/22fef44f-9e48-4821-ab1e-879b4adc97f4/Untitled.png)

### Firebase push notification

- push notification이라는 프로젝트 생성
- 프로젝트 설정의 클라우드 메시징 탭에서 서버키를 받아 등록

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5ecf71f9-e345-499b-9eab-f6bac84d996c/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5ecf71f9-e345-499b-9eab-f6bac84d996c/Untitled.png)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/16a66fb5-6b27-4a04-b972-f48e65921890/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/16a66fb5-6b27-4a04-b972-f48e65921890/Untitled.png)

- 등록 이후 Test messaging을 시도했으나, Device tokens을 불러올 수가 없었음
- 처음엔 서버키를 넣고 해보았는데, 이는 아닌 것으로 확인.
- firebase 공식 document 확인 하면 app을 등록하고 token을 불러오는 함수를 작성해야 token을 불러 올 수 있음
- 아래와 같음.
    - [ ]  이를 계속 진행해야 하는지 이사님께 질문

```java
FirebaseMessaging.getInstance().getToken()
    .addOnCompleteListener(new OnCompleteListener<String>() {
        @Override
        public void onComplete(@NonNull Task<String> task) {
          if (!task.isSuccessful()) {
            Log.w(TAG, "Fetching FCM registration token failed", task.getException());
            return;
          }

          // Get new FCM registration token
          String token = task.getResult();

          // Log and toast
          String msg = getString(R.string.msg_token_fmt, token);
          Log.d(TAG, msg);
          Toast.makeText(MainActivity.this, msg, Toast.LENGTH_SHORT).show();
        }
    });

```

[백그라운드 앱에 테스트 메시지 보내기 | Firebase](https://firebase.google.com/docs/cloud-messaging/android/first-message?hl=ko)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/fc5abf98-f073-4f05-8973-38d91c747cad/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/fc5abf98-f073-4f05-8973-38d91c747cad/Untitled.png)

- 추가로 알게 된 사실
- push notification message actions에서 다양한 방법으로 시도 가능
- 아직 하나도 시도해보지는 못함.

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0d4988b3-7b62-4cbe-8cf2-84aa97ce09d9/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0d4988b3-7b62-4cbe-8cf2-84aa97ce09d9/Untitled.png)