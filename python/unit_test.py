my_list = [(1, 5), (2, 8), (3, 3), (4, 7), (4, 8)]

print(max(my_list))


print("0번 값 기준으로 가장 큰 값:", max_value_0th)

exit()

from itertools import product

# 할인율과 상품 가격 리스트
discount_rates = [10, 20, 30, 40]
product_prices = [1000, 2000, 4000]

# 가능한 모든 할인 조합 생성
combinations = list(product(discount_rates, repeat=len(product_prices)))

print(combinations)

# 각 조합에 대한 총 가격 계산 및 출력
for combo in combinations:
    total_price = sum(price * (100 - rate) / 100 for price, rate in zip(product_prices, combo))
    


exit()

print(int(1300 * 0.6)) # = 780
print(int(1500 * 0.6)) # = 900
print(int(1600 * 0.8)) # = 1280
print(int(4900 * 0.6)) # = 2940


exit()
price = 10000
discount = 500
discount_rate = 5

# 할인금액 = 정가 * 할인율
#         = 정가 * (할인율 / 100)
print(int(price * (5 / 100)))
print(int(price * 0.05))

# 구매금액 = 정가 * 100% - 할인율
#         = 정가 * ((100 - 할인율) / 100)
print(int(price * ((100 - 5) / 100)))
print(int(price * 0.95))

# 할인율 = 할인액 / 정가 * 100
print(discount / price * 100)