# 연산자
print(1+1) # 2
print(3-2) # 1
print(5*2) # 10
print(6/3) # 2.0

print(2**3) # 2^3 = 8
print(5%3) # 나머지구하기 2
print(10%3) # 1
print(5//3) # 몫 1
print(10//3) # 3

print(10>3) # True
print(4 >= 7) # False
print(10 < 3) # False
print(5 <= 5) # True

print(3==3) # True
print(4==2) # False
print(3+4==7) # True

print (1!=3) # True
print(not (1!=3)) #False

print((3>0) and (3<5)) # True
print((3>0) & (3<5)) # True

print((3>0) or (3>5)) # True
print((3>0) | (3>5)) # True

print(5 > 4 > 3) # True
print(5 > 4 > 7) # False

# 간단한 수식
print(2 + 3 * 4) # 14
print((2 + 3) * 4) # 20
number = 2 + 3 * 4 # 14
print(number)
number = number + 2 # 16
print(number)
number += 2 # 18
print(number)
number *= 2 # 36
print(number)
number /= 2 # 18.0
print(number)
number -= 2 # 16.0
print(number)

number %= 5 # 2 -> 0.0 / 5 -> 1.0
print(number)

# 숫자 처리 함수
print(abs(-5))      # 5     abs : 절대값
print(pow(4, 2))    # 4^2 = 4*4 = 16
print(max(5, 12))   # 12    max : 최대값
print(min(5, 12))   # 5     min : 최소값
print(round(3.14))  # 3     round : 반올림
print(round(4.99))  # 5

from math import *  #math 라이브러리 import
print(floor(4.99))  # 4     floor : 내림
print(ceil(3.14))   # 4     ceil : 올림
print(sqrt(16))     # 4     sqrt