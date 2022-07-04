### 리스트 [] : 순서를 가지는 객체의 집합

# 지하철 칸별로 10명, 20명, 30명이 있는 경우
# subway1 = 10
# subway2 = 20
# subway3 = 30
subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호씨가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

# 하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하")       # append 더하다
print(subway)               # ['유재석', '조세호', '박명수', '하하']

# 정형돈씨를 유재석 / 조세호 사이에 태워봄
subway.insert(1, "정형돈")  # insert 원하는 위치에 입력함
print(subway)               # ['유재석', '정형돈', '조세호', '박명수', '하하']

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())         # pop 뒤에서부터 하나씩 빼냄
                            # 하하
print(subway)               # ['유재석', '정형돈', '조세호', '박명수']
# print(subway.pop())         # 박명수
# print(subway)               # ['유재석', '정형돈', '조세호']
# print(subway.pop())         # 조세호
# print(subway)               # ['유재석', '정형돈']

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)                   # ['유재석', '정형돈', '조세호', '박명수', '유재석']
print(subway.count("유재석"))   # 같은 값이 몇개 있는지 확인
                                # 2

# 정렬
num_list = [5, 4, 3, 2, 1]
num_list.sort()             # 오름차순 정렬
print(num_list)             # [1, 2, 3, 4, 5]

# 뒤집어서 정렬
num_list.reverse()          # 내림차순 정렬
print(num_list)             # [5, 4, 3, 2, 1]

# 모두 지우기
num_list.clear()            # 비움
print(num_list)             # []

# 다양한 자료형 함께 사용
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장
num_list = [5, 4, 3, 2, 1]
num_list.extend(mix_list)   # num_list에 mix_list 합침
print(num_list)             # [5, 4, 3, 2, 1, '조세호', 20, True]

# 사전 (키에 대한 중복이 허용되지 않음)
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])           # 유재석
print(cabinet[100])         # 김태호
print(cabinet.get(3))       # 유재석
#print(cabinet[5])          # 오류 발생
print(cabinet.get(5))       # None
print(cabinet.get(5, "사용 가능"))       # 값이 없으면 문장 출력

print(3 in cabinet)         # in 사전 자료형 안에 값이 있는지 확인
                            # True
print(5 in cabinet)         # False

cabinet = {"A-3":"유재석", "B-100":"김태호"}    # 숫자 말고 문장도 사용 가능
print(cabinet["A-3"])           # 유재석
print(cabinet["B-100"])         # 김태호

# 새 손님
print(cabinet)                  # {'A-3': '유재석', 'B-100': '김태호'}
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)                  # {'A-3': '김종국', 'B-100': '김태호', 'C-20': '조세호'}

# 간 손님
del cabinet["A-3"]              # del 값 삭제
print(cabinet)                  # {'B-100': '김태호', 'C-20': '조세호'}

# key 들만 출력
print(cabinet.keys())           # dict_keys(['B-100', 'C-20'])

# value 들만 출력
print(cabinet.values())         # dict_values(['김태호', '조세호'])

# key, value 쌍으로 출력
print(cabinet.items())          # dict_items([('B-100', '김태호'), ('C-20', '조세호')])

# 목욕탕 폐점
cabinet.clear()
print(cabinet)                  # {}

### 튜플 (더하거나 뺄 수 없는 고정값)
menu = ("돈까스", "치즈까스")
print(menu[0])          # 돈까스
print(menu[1])          # 치즈까스
#menu.add("생선까스")     # 오류 출력

name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby) # 김종국 20 코딩

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby) # 김종국 20 코딩

### 세트 (set, 집합)
# 중복 안됨, 순서 없음
my_set = {1, 2, 3, 3, 3}
print(my_set)           # 중복 제거하여 출력
                        # {1, 2, 3}
java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])  # 리스트를 먼저 만들고 set으로 감싸줌

# 교집합 (java와 python을 모두 할 수 있는 개발자)
print(java & python)                # {'유재석'}
print(java.intersection(python))    # {'유재석'}

# 합집합 (java 할 수 있거나 python 할 수 있는 개발자)
print(java | python)                # {'양세형', '박명수', '김태호', '유재석'}
print(java.union(python))           # {'양세형', '박명수', '김태호', '유재석'}

# 차집합 (java는 할 수 있지만 python은 할 줄 모르는 개발자)
print(java - python)                # {'김태호', '양세형'}
print(java.difference(python))      # {'김태호', '양세형'}

# python을 할 줄 아는 사람이 늘어남
python.add("김태호")                # add 입력
print(python)                       # {'박명수', '김태호', '유재석'}

# java를 잊었어요
java.remove("김태호")               # remove 삭제
print(java)                         # {'양세형', '유재석'}

### 자료구조의 변경
# 커피숍
menu = {"커피", "우유", "주스"}
print(menu, type(menu))         # {'주스', '커피', '우유'} <class 'set'>

menu = list(menu)
print(menu, type(menu))         # ['주스', '커피', '우유'] <class 'list'>

menu = tuple(menu)
print(menu, type(menu))         # ('주스', '커피', '우유') <class 'tuple'>

menu = set(menu)
print(menu, type(menu))         # {'주스', '우유', '커피'} <class 'set'>


'''
당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
추첨 프로그램을 작성하시요.

조건 1 : 편의상 댓글은 20명이 작성하였고, 아이디는 1~20이라고 가정
조건 2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
조건 3 : random 모듈의 shuffle과 sample을 활용

(출력 예제)
-- 당첨자 발표 --
치킨 당첨자 : 1
커피 당첨자 : [2, 3, 4]
-- 축하합니다 --
'''
# 활용 예제
from random import *
lst = [1, 2, 3, 4, 5]
print(lst)              # [1, 2, 3, 4, 5]
shuffle(lst)            # list내의 값을 무작위로 정렬
print(lst)              # [4, 2, 1, 5, 3]
print(sample(lst, 1))   # list내의 값을 원하는 개수만큼 무작위로 출력
                        # [2]

# 풀이
users = range(1, 21)     # 1부터 20까지 숫자를 생성
print(type(users))       # <class 'range'>
users = list(users)
print(type(users))       # <class 'list'>
print(users)             # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
winners = sample(users, 4)  # 4명 중에서 1명은 치킨, 3명은 커피

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다 --")
