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
print(sqrt(16))     # 4.0   sqrt : 제곱근

from random import * # 랜덤 함수 import
print(random())      # 0.06075268502477238   0.0~1.0 미만의 임의의 값 생성
print(random() * 10) # 1.627092019612486     0.0~10.0 미만의 임의의 값 생성
print(int(random() * 10)) # 1                0~10 미만의 임의의 값 생성
print(int(random() * 10)) # 3                0~10 미만의 임의의 값 생성
print(int(random() * 10)) # 0                0~10 미만의 임의의 값 생성
print(int(random() * 10) + 1) # 3            1~10 이하의 임의의 값 생성
print(int(random() * 10) + 1) # 9            1~10 이하의 임의의 값 생성
print(int(random() * 10) + 1) # 4            1~10 이하의 임의의 값 생성
print(int(random() * 10) + 1) # 5            1~10 이하의 임의의 값 생성
print(int(random() * 10) + 1) # 2            1~10 이하의 임의의 값 생성
print(int(random() * 10) + 1) # 6            1~10 이하의 임의의 값 생성

# 로또 값 출력 1
print(int(random() * 45) + 1) # 2              1~45 이하의 임의의 값 생성
print(int(random() * 45) + 1) # 42             1~45 이하의 임의의 값 생성
print(int(random() * 45) + 1) # 18             1~45 이하의 임의의 값 생성
print(int(random() * 45) + 1) # 6              1~45 이하의 임의의 값 생성
print(int(random() * 45) + 1) # 41             1~45 이하의 임의의 값 생성
print(int(random() * 45) + 1) # 5              1~45 이하의 임의의 값 생성

# 로또 값 출력 2
print(randrange(1, 46)) # 30    1~46 미만의 임의의 값 생성
print(randrange(1, 46)) # 19    1~46 미만의 임의의 값 생성
print(randrange(1, 46)) # 15    1~46 미만의 임의의 값 생성
print(randrange(1, 46)) # 36    1~46 미만의 임의의 값 생성
print(randrange(1, 46)) # 15    1~46 미만의 임의의 값 생성
print(randrange(1, 46)) # 43    1~46 미만의 임의의 값 생성

# 로또 값 출력 3
print(randint(1, 45))   # 26    1~45 이하의 임의의 값 생성
print(randint(1, 45))   # 3     1~45 이하의 임의의 값 생성
print(randint(1, 45))   # 27    1~45 이하의 임의의 값 생성
print(randint(1, 45))   # 33    1~45 이하의 임의의 값 생성
print(randint(1, 45))   # 13    1~45 이하의 임의의 값 생성
print(randint(1, 45))   # 39    1~45 이하의 임의의 값 생성

# 퀴즈
''' 
당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.

조건 1 : 랜덤으로 날짜를 뽑아야 함
조건 2 : 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
조건 3 : 매월 1~3일은스터디 준비를 해야 하므로 제외

(출력문 예제) 
오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다.
'''
from random import * # 랜덤 함수 import
date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월",date,"일로 선정되었습니다.")
print("오프라인 스터디 모임 날짜는 매월 "+str(date)+"일로 선정되었습니다.")