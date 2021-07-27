def cal_dividend(seller,amount,member_dict={}):
    dividend = int(amount*0.1)
    # 배당금 10% 1미만
    if dividend < 1 :
        member_dict[seller][1] += amount # 그대로 순이익
    # 배당금 10% 1이상 and 추천인 X
    elif member_dict[seller][0] =='-':
        member_dict[seller][1] += amount - dividend
    # 배당금 10% 1이상 and 추천인 O
    else:
        member_dict[seller][1] += amount - dividend
        cal_dividend(member_dict[seller][0],dividend,member_dict)

def solution(enroll, referral, seller, amount):
    member_dict = {}
    for en,re in zip(enroll,referral):
        member_dict[en]=[re,0]
    amount = list(map(lambda x:x*100,amount))
    for sellery,count in zip(seller,amount):
        cal_dividend(sellery, count,member_dict)
    answer = []
    for member in enroll:
        answer.append(member_dict[member][1])
    return answer

enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]

# seller = ["young", "john", "tod", "emily", "mary"]
# amount = [12, 4, 2, 5, 10]
# result = [360, 958, 108, 0, 450, 18, 180, 1080]

seller = ["sam", "emily", "jaimie", "edward"]
amount = [2, 3, 5, 4]
result = [0, 110, 378, 180, 270, 450, 0, 0]

print(solution(enroll,referral,seller,amount))