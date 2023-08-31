def solution(price, money, count):
    # amount = sum(price * i for i in range(1, count+1))
    # return 0 if amount < money else amount - money
    return max(0, sum(price * i for i in range(1, count+1)) - money)

price = 3
money = 20
count = 4
print(solution(price, money, count))