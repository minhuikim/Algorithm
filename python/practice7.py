# 표준 입출력
print("Python" + "Java")                            # PythonJava
print("Python", "Java")                             # Python Java
print("Python", "Java", sep=",")                    # Python,Java
print("Python", "Java", "JavaScript", sep=" vs ")   # Python vs Java vs JavaScript

print("Python", "Java", sep=",", end="?")           # Python,Java?무엇이 더 재밌을까요?
print("무엇이 더 재밌을까요?")

print("Python", "Java", sep=",")                    # Python,Java
print("무엇이 더 재밌을까요?")                       # 무엇이 더 재밌을까요?

import sys
print("Python", "Java", file=sys.stdout)            # 표준출력              Python Java
print("Python", "Java", file=sys.stderr)            # 표준에러(로그처리 등)  Python Java

# 시험 성적
scores = {"수학":0, "영어":50, "코딩":100}           # key:value
for subject, score in scores.items():               # subject = key(수학, 영어, 코딩) / score = value(0, 50, 100)
    # print(subject, score)
    '''
        수학       0
        영어       50
        코딩       100
    '''
    print(subject.ljust(8), str(score).rjust(4), sep=":")                  # ljust(8) 왼쪽정렬(8칸 중 값이 없는 공간은 공백으로 채움), rjust(4) 오른쪽 정렬(4칸 중 값이 없는 공간은 공백으로 채움)
    '''
        수학      :   0
        영어      :  50
        코딩      : 100
    '''

# 은행 대기순번표
# 001, 002, 003, ...
for num in range(1, 21):
    print("대기번호 : " + str(num))
    '''
        대기번호 : 1
        대기번호 : 2
        대기번호 : 3
        대기번호 : 4
        대기번호 : 5
        대기번호 : 6
        대기번호 : 7
        대기번호 : 8
        대기번호 : 9
        대기번호 : 10
        대기번호 : 11
        대기번호 : 12
        대기번호 : 13
        대기번호 : 14
        대기번호 : 15
        대기번호 : 16
        대기번호 : 17
        대기번호 : 18
        대기번호 : 19
        대기번호 : 20
    '''

for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))    # zfill(3) 3칸 중 값이 없는 공간은 0으로 채움
    '''
        대기번호 : 001
        대기번호 : 002
        대기번호 : 003
        대기번호 : 004
        대기번호 : 005
        대기번호 : 006
        대기번호 : 007
        대기번호 : 008
        대기번호 : 009
        대기번호 : 010
        대기번호 : 011
        대기번호 : 012
        대기번호 : 013
        대기번호 : 014
        대기번호 : 015
        대기번호 : 016
        대기번호 : 017
        대기번호 : 018
        대기번호 : 019
        대기번호 : 020
    '''

# answer = input("아무 값이나 입력하세요 : ")
# print(type(answer))
# print("입력하신 값은 " + answer + "입니다.")
'''
아무 값이나 입력하세요 : 10
<class 'str'>                   => 사용자의 입력을 통해서 값을 받게 되면 문자열 형태로 저장된다.
입력하신 값은 10입니다.

아무 값이나 입력하세요 : python
<class 'str'>
입력하신 값은 python입니다.
'''

answer = 10
print(type(answer))                     # <class 'int'>

# 다양한 출력포멧
# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))           #        500
print("{0: >10}".format(-500))          #        -500

# 양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500))          #        +500
print("{0: >+10}".format(-500))         #        -500

# 왼쪽 정렬하고, 빈칸을 _로 채움
print("{0:_<+10}".format(500))          # +500______
print("{0:_<10}".format(500))           # 500_______

# 3자리 마다 콤마를 찍어주기
print("{0:,}".format(1000000000000))    # 1,000,000,000,000

# 3자리 마다 콤마를 찍어주기, +-부호도 붙이기
print("{0:+,}".format(1000000000000))   # +1,000,000,000,000
print("{0:+,}".format(-1000000000000))  # -1,000,000,000,000

# 3자리 마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보하기
# 돈이 많으면 행복하니까 빈 자리는 ^로 채워주기
print("{0:^<+30,}".format(1000000000000)) # +1,000,000,000,000^^^^^^^^^^^^

# 소수점 출력
print("{0:f}".format(5/3))              # 1.666667

# 소수점 특정 자리수 까지만 표시 (소수점 3째 자리에서 반올림)
print("{0:.2f}".format(5/3))            # 1.67

# 파일 입출력
# score_file = open("./python/score.txt", "w", encoding="utf8") # 파일을 생성해서 새로 작성
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()
'''
    수학 : 0
    영어 : 50
'''

# score_file = open("./python/score.txt", "a", encoding="utf8")   # 파일 뒤에 이어서 작성
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()
'''
    수학 : 0
    영어 : 50
    과학 : 80
    코딩 : 100
'''

score_file = open("./python/score.txt", "r", encoding="utf8")   # 파일 읽어오기
print(score_file.read())
score_file.close()
'''
    수학 : 0
    영어 : 50
    과학 : 80
    코딩 : 100
'''

score_file = open("./python/score.txt", "r", encoding="utf8")
print(score_file.readline())    # 줄 별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close()
'''
    수학 : 0

    영어 : 50

    과학 : 80

    코딩 : 100
'''

score_file = open("./python/score.txt", "r", encoding="utf8")
print(score_file.readline(), end="")    # 줄 별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()
'''
    수학 : 0
    영어 : 50
    과학 : 80
    코딩 : 100
'''

score_file = open("./python/score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close()
print()
'''
    수학 : 0
    영어 : 50
    과학 : 80
    코딩 : 100
'''

score_file = open("./python/score.txt", "r", encoding="utf8")
lines = score_file.readlines()  # list 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()
print()
'''
    수학 : 0
    영어 : 50
    과학 : 80
    코딩 : 100
'''

# pickle
# 프로그램상에서 사용하는 데이터를 파일에 저장 -> 파일을 불러와서 데이터 재사용 가능
import pickle
# profile_file = open("./python/profile.pickle", "wb")    # wb = binary write , pickle에서는 항상 binary 사용
# profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file)                      # profile에 있는 정보를 file에 저장
# profile_file.close()

profile_file = open("./python/profile.pickle", "rb")
profile = pickle.load(profile_file)                     # file에 있는 정보를 profile에 불러오기
print(profile)                                          # {'이름': '박명수', '나이': 30, '취미': ['축구', '골프', '코딩']}
profile_file.close()

# with
# 파일을 close할 필요 없이 알아서 종료해준다
import pickle
with open("./python/profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))                    # {'이름': '박명수', '나이': 30, '취미': ['축구', '골프', '코딩']}

# with open("./python/study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

with open("./python/study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())                            # 파이썬을 열심히 공부하고 있어요

'''
당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

- X 주차 주간보고 -
부서 : 
이름 : 
업무 요약 :

1주차부터 10주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

조건 : 파일명은 '1주차.txt', '2주차.txt', ... 와 같이 만듭니다.
'''
# for index in range(1, 21):
#     with open("./python/practice7/"+str(index)+"주차.txt", "w", encoding="utf8") as study_file:
#         study_file.write("- {0} 주차 주간보고 -".format(index))
#         study_file.write("\n부서 : ".ljust(5))
#         study_file.write("\n이름 : ".ljust(5))
#         study_file.write("\n업무 요약 : ".ljust(8))

for i in range(1, 11):
    with open("./python/practice7/" + str(i) + "주차.txt", "w", encoding="utf8") as report_file:
        report_file.write("- {0} 주차 주간보고 -".format(i))
        report_file.write("\n부서 : ")
        report_file.write("\n이름 : ")
        report_file.write("\n업무 요약 : ")