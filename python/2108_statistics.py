import sys

n = int(input())
num = []

for i in range(n):
    num.append(int(sys.stdin.readline()))

print()

# 산술평균
print(sum(num)//n)

# 중앙값
num.sort()
print(num[n//2])

# 최빈값
print()

# 범위
print(num[n-1]-num[0])



# dic = Counter(num)      # dict 하위 클래스
                        # 리스트, 튜플 -> 각 데이터 등장 횟수를 사전 형식으로 반환
# dic = dic.most_common() # 등장한 횟수를 내림차순으로 정리

# 가장 많이 등장한 횟수만 추출
# many = []
# for num2 in dic:
#     if dic[0][1] == num2[1]:
#         many.append(int(num2[0]))

# if len(many) > 1:
#     many_val = many[len(many)-2]
# else:
#     many_val = many[0]


'''
음의정수... dic으로,,?
max_val = 0
for i in range(4001):
    if many[i] != 0:
        for j in range(4001):
            if many[i] <= many[j]:
                max_val = many[j]

many_arr = []
for i in range(4001):
    if many[i] == max_val:
        many_arr.append(i)

many_arr = sorted(many_arr)
'''