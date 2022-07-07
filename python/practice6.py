# 함수
def open_account():
    print("새로운 계좌가 생성되었습니다.")

open_account()                      # 새로운 계좌가 생성되었습니다.

def deposit(balance, money):        # 입금
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money):       # 출금
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원 입니다.".format(balance))
        return balance

def withdraw_night(balance, money):       # 저녁에 출금
    commission = 100                      # 수수료 100원
    return commission, balance - money - commission


balance = 0                         # 잔액
balance = deposit(balance, 1000)    # 입금이 완료되었습니다. 잔액은 1000원 입니다
# balance = withdraw(balance, 2000)   # 출금이 완료되지 않았습니다. 잔액은 1000원 입니다.
# balance = withdraw(balance, 500)    # 출금이 완료되었습니다. 잔액은 500원 입니다.
commission, balance = withdraw_night(balance, 500) 
print("수수료 {0}원 이며, 잔액은 {1}원 입니다.".format(commission, balance))
    # 수수료 100원 이며, 잔액은 400원 입니다.

# 기본값
def profile(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"\
        .format(name, age, main_lang))

profile("유재석", 20, "파이썬") # 이름 : 유재석   나이 : 20       주 사용 언어 : 파이썬
profile("김태호", 25, "자바")   # 이름 : 김태호   나이 : 25       주 사용 언어 : 자바


# 같은 학교 같은 학년 같은 반 같은 수업
def profile(name, age=17, main_lang="파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"\
        .format(name, age, main_lang))

profile("유재석")   # 이름 : 유재석   나이 : 17       주 사용 언어 : 파이썬
profile("김태호")   # 이름 : 김태호   나이 : 17       주 사용 언어 : 파이썬

# 키워드 값
def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name="유재석", main_lang="파이썬", age=20)  # 유재석 20 파이썬
profile(main_lang="자바", age=25, name="김태호")    # 김태호 25 자바

# 가변인자
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이: {1}\t".format(name, age), end=" ") # 줄바꿈없이 " "으로 끝남
#     print(lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *language):  # * : 가변인자
    print("이름 : {0}\t나이: {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print() # 줄바꿈을 위해 출력

profile("유재석", 20, "Python", "Java", "C", "C++", "C#")   # 이름 : 유재석   나이: 20         Python Java C C++ C#
profile("김태호", 25, "Kotlin", "Swift", "", "", "")        # 이름 : 김태호   나이: 25         Kotlin Swift

# 지역변수와 전역변수
# 1
# gun = 10

# def checkpoint(soldiers): # 경계근무
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# print("전체 총 : {0}".format(gun))
# checkpoint(2)                       # 2명이 경계 근무 나감
# print("남은 총 : {0}".format(gun))
# # 출력 : 에러 (함수 내의 gun이 지역변수인데 초기화가 안돼서 에러출력)

# # 2
# gun = 10

# def checkpoint(soldiers): # 경계근무
#     gun = 20
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# print("전체 총 : {0}".format(gun))
# checkpoint(2)                       # 2명이 경계 근무 나감
# print("남은 총 : {0}".format(gun))
# # 출력 : 함수 내의 gun의 값과 함수 밖의 gun의 값이 다름
#     # 전체 총 : 10
#     # [함수 내] 남은 총 : 18
#     # 남은 총 : 10

# 3
# gun = 10

# def checkpoint(soldiers):   # 경계근무
#     global gun              # 전역 공간에 있는 gun 사용
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# print("전체 총 : {0}".format(gun))
# checkpoint(2)                       # 2명이 경계 근무 나감
# print("남은 총 : {0}".format(gun))
# # 출력 : 함수 내에서 global을 사용해 전역변수인 gun을 불러옴
#     # 전체 총 : 10
#     # [함수 내] 남은 총 : 8
#     # 남은 총 : 8

# 4
gun = 10

def checkpoint(soldiers):           # 경계근무
    global gun                      # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):   # 경계근무
    gun = gun - soldiers             # gun을 파라미터로 받아서 사용
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
# checkpoint(2)                       # 2명이 경계 근무 나감
gun = checkpoint_ret(gun, 2)          # 2명이 경계 근무 나감
print("남은 총 : {0}".format(gun))
# 출력 : 변수를 파라미터로 받아서 사용 후 return
    # 전체 총 : 10
    # [함수 내] 남은 총 : 8
    # 남은 총 : 8

'''
표준 체중을 구하는 프로그램을 작성하시오

* 표준 체중 : 각 개인의 키에 적당한 체중

(성별에 따른 공식)
 남자 : 키(m) x 키(m) x 22
 여자 : 키(m) x 키(m) x 21

조건1 : 표준 체중은 별도의 함수 내에서 계산
        * 함수명 : std_weight
        * 전달값 : 키(height), 성별(gender)
조건2 : 표준 체중은 소수점 둘째자리까지 표시

(출력 예제)
키 175cm 남자의 표준 체중은 67.38kg 입니다.
'''
# 키 m 단위 (실수), 성별 "남자" / "여자"
def std_weight(height, gender):

    height = height / 100

    if gender=="남자":
        return height * height * 22
    else:
        return height * height * 21

height = int(input())
# height = 175    # cm 단위
gender = input()
# gender = "남자"

weight = std_weight(height, gender)
weight = round(weight, 2)

print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))