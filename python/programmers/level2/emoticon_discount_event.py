# https://school.programmers.co.kr/learn/courses/30/lessons/150368
def solution(users, emoticons):
    rate = [10 for _ in range(len(emoticons))]
    discount = [10, 20, 30, 40]
    # 각 이모티콘 별 할인율 10% 20% 30% 40% 일 때 가입자 수, 구매 금액
    '''
    ?? 재귀,,?
    max_join, max_cost
    def emoji_rate(r, e, max_join, max_cost):

        rate = e1 10% + e2 10% + e3 10% + e4 10% ... 

        if total_cost < user_cost:
            # 한 명이 구매하는 이모티콘 비용
            total_cost += (e[i] * (100% - rate))
        else 
            # 예상금액 이상이면 플러스 가입
            join += 1
        
        if max_join <= join:
            max_join = join
            max_cost < cost:
                max_cost = cost

        return emoji_rate(r, e, max_join, max_cost)

    10 10 ... 10 10
    10 10 ... 10 20
    10 10 ... 10 30
    10 10 ... 10 40
    10 10 ... 20 10
    10 10 ... 20 20
    10 10 ... 20 30
    10 10 ... 20 40
    10 10 ... 30 10
    ...... 
    

    '''
    
    max_plus = 0
    max_cost = 0
    i, j = 0, 0
    while j < len(rate)-1:
        plus = 0
        cost = 0
        for buy_rate, join_cost in users:
            for r, e in zip(rate, emoticons):
                if buy_rate <= r:
                    dis_price = int(e * ((100 - r) / 100))
                    cost += dis_price
            if cost >= join_cost:
                plus += 1
                cost = 0
        
        if max_plus <= plus:
            max_plus = plus
            if max_cost < cost:
                max_cost = cost

        # 할인율을 재귀로..?
        if rate[i] < 40:
            rate[i] += 10
        else:
            rate[i] = 10
            if rate[i + j] == 40:
                j += 1
            rate[i + j] += 10

    return [max_plus, max_cost]


users = [[40, 10000], [25, 10000]]
emoticons = [7000, 9000]
# [1, 5400]

# users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
# emoticons = [1300, 1500, 1600, 4900]
# [4, 13860]

print(solution(users, emoticons))

#1300 * 0.6 = 780
#1500 * 0.6 = 900
#1600 * 0.8 = 1280
#4900 * 0.6 = 2940
