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