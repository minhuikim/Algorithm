## 예외처리
try:
    print("나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:
    print(err)
'''
[예외처리 전]
나누기 전용 계산기입니다.
첫 번째 숫자를 입력하세요 : 6
두 번째 숫자를 입력하세요 : 3
6 / 3 = 2

[예외처리 전]
나누기 전용 계산기입니다.
첫 번째 숫자를 입력하세요 : 6
두 번째 숫자를 입력하세요 : 삼
Traceback (most recent call last):
  File "d:\source\repos\Algorithm\python\practice9.py", line 4, in <module>
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
ValueError: invalid literal for int() with base 10: '삼'

[예외처리 후] except ValueError:
나누기 전용 계산기입니다.
첫 번째 숫자를 입력하세요 : 6
두 번째 숫자를 입력하세요 : 삼
에러! 잘못된 값을 입력하였습니다.

[예외처리 후] except ValueError:
나누기 전용 계산기입니다.
첫 번째 숫자를 입력하세요 : 6
두 번째 숫자를 입력하세요 : 0
Traceback (most recent call last):
  File "d:\source\repos\Algorithm\python\practice9.py", line 6, in <module>
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
ZeroDivisionError: division by zero

[예외처리 후] except ZeroDivisionError as err:
나누기 전용 계산기입니다.
첫 번째 숫자를 입력하세요 : 6
두 번째 숫자를 입력하세요 : 0
division by zero
'''

try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    # nums.append(int(nums[0]/nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print("알 수 없는 에러가 발생하였습니다.")
    print(err)
'''
[예외처리 후 append주석처리하여 에러 발생]
나누기 전용 계산기입니다.
첫 번째 숫자를 입력하세요 : 6
두 번째 숫자를 입력하세요 : 3
알 수 없는 에러가 발생하였습니다.
list index out of range
'''

### 에러 발생시키기
try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise ValueError
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
'''
한 자리 숫자 나누기 전용 계산기입니다.
첫 번째 숫자를 입력하세요 : 10
두 번째 숫자를 입력하세요 : 5
잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.
'''

### 사용자 정의 예외처리
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
    print(err)
'''
한 자리 숫자 나누기 전용 계산기입니다.
첫 번째 숫자를 입력하세요 : 10
두 번째 숫자를 입력하세요 : 5
에러가 발생하였습니다. 한 자리 숫자만 입력하세요.
입력값 : 10, 5
'''

### Finally 무조건 실행
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
    print(err)
finally:
    print("계산기를 이용해 주셔서 감사합니다.")
'''
한 자리 숫자 나누기 전용 계산기입니다.
첫 번째 숫자를 입력하세요 : 5
두 번째 숫자를 입력하세요 : 2
5 / 2 = 2
계산기를 이용해 주셔서 감사합니다.

[예외처리 후에도 finally 구문은 실행]
한 자리 숫자 나누기 전용 계산기입니다.
첫 번째 숫자를 입력하세요 : 10
두 번째 숫자를 입력하세요 : 5
에러가 발생하였습니다. 한 자리 숫자만 입력하세요.
입력값 : 10, 5
계산기를 이용해 주셔서 감사합니다.

[에러가 발생해도 finally 구문은 실행]
한 자리 숫자 나누기 전용 계산기입니다.
첫 번째 숫자를 입력하세요 : 5
두 번째 숫자를 입력하세요 : 0
계산기를 이용해 주셔서 감사합니다.
Traceback (most recent call last):
  File "d:\source\repos\Algorithm\python\practice9.py", line 131, in <module>        
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
ZeroDivisionError: division by zero
'''