from collections import Counter

n = int(input())
num = []

sum = 0
for i in range(n):
    num.append(int(input()))
    sum = sum + num[i]

num = sorted(num)

dic = Counter(num)      # dict 하위 클래스
                        # 리스트, 튜플 -> 각 데이터 등장 횟수를 사전 형식으로 반환
dic = dic.most_common() # 등장한 횟수를 내림차순으로 정리

# 가장 많이 등장한 횟수만 추출
most = []
for num2 in dic:
    if dic[0][1] == num2[1]:
        most.append(int(num2[0]))

if len(most) > 1:
    max_val = most[len(most)-2]
else:
    max_val = most[0]

# 산술평균
print(sum//n)
# 중앙값
print(num[n//2])
# 최빈값
print(max_val)
# 범위
print(num[n-1]-num[0])