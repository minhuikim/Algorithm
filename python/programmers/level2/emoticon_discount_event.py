# https://school.programmers.co.kr/learn/courses/30/lessons/150368
from itertools import product

def solution(users, emoticons):

    discount = [10, 20, 30, 40]
    discount_rate = list(product(discount, repeat=len(emoticons)))

    join_cost = []
    for rate in discount_rate:
        join = 0
        total_cost = 0
        for ur, uc in users:
            user_cost = 0
            # user가 구입하는 전체 이모티콘 비용
            for r, e in zip(rate, emoticons):
                # 이모티콘 할인율이 기준 이상이면 구매
                if ur <= r:
                    user_cost += int(e * (100 - r) * 0.01)
            # 구매한 이모티콘이 기준 이상이면 멤버쉽 가입
            if uc <= user_cost:
                join += 1
                user_cost = 0
            total_cost += user_cost
            
        join_cost.append([join, total_cost])
        
    return max(join_cost)


users = [[40, 10000], [25, 10000]]
emoticons = [7000, 9000]
# [1, 5400]

users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
emoticons = [1300, 1500, 1600, 4900]
# [4, 13860]

print(solution(users, emoticons))
