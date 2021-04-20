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