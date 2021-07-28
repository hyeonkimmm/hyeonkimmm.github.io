from collections import defaultdict
from itertools import combinations
def solution(orders, course):
    order_dict ={}
    answer = []
    for c in course:
        order_dict[c]= defaultdict(int)

    for order in orders:
        for combine in course:
            for combination_order in list(combinations(sorted(order),combine)):
                order_dict[combine][''.join(combination_order)]+=1 

    for combine in course:
        try:
            top_order = max(order_dict[combine].values())
        except :
            continue
        if top_order >=2:
            for key,value in order_dict[combine].items():
                if value == top_order:
                    answer.append(key)
    return sorted(answer)
'''
최소 2가지 이상의 메뉴로 단품메뉴 구성
최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합
for 문 중첩 두번에
course에 맞게 조합해주는 dict 선언해서 하나씩 늘리면 될듯
'''
orders= ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course= [2,3,4]
print(solution(orders,course))

orders= ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course= [2,3,5]
print(solution(orders,course))

orders= ["XYZ", "XWY", "WXA"]
course= [2,3,4]
print(solution(orders,course))

