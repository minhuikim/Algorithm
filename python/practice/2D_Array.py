# 값이 0인 2차원 배열 생성
rows = 5
cols = 5
array = [[0 for j in range(cols)] for i in range(rows)]

# print(array)

# [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

#------------------------------------------------------------#

# 10칸의 배열에 띄어쓰기 형식으로 입력되는 값 int형식으로 저장
tmp1 = 5
tmp2 = []
# for p in range(tmp1):
#     tmp2.append(list(map(int, input().split())))

# print(tmp2)

'''
input
1 2 3 4 5 
1 2 3 
1 2 
1 2 3 4 5 6 7
3 2 1

result
[[1, 2, 3, 4, 5], [1, 2, 3], [1, 2], [1, 2, 3, 4, 5, 6, 7], [3, 2, 1]]
'''

#------------------------------------------------------------#

# x, y 각각 입력된 값 저장 및 출력
#   - 지정된 변수만큼 값 입력 가능 - x, y면 1 2 3 입력 불가능
#   - 반복문 밖으로 나가면 마지막 입력된 값만 사용 가능
# for i in range(3):
    # x, y = map(int, input().split())
    # print(x, y)

#-------------------------------------------------------------#

# 최빈값 정렬
# https://codepractice.tistory.com/71

from collections import Counter

n = int(input())
num = []

for i in range(n):
    num.append(int(input()))

dic = Counter(num)      # dict 하위 클래스
                        # 리스트, 튜플 -> 각 데이터 등장 횟수를 사전 형식으로 반환
dic = dic.most_common() # 등장한 횟수를 내림차순으로 정리

print(dic)