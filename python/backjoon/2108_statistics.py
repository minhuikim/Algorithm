import sys
from collections import Counter

n = int(sys.stdin.readline())
num = []

for _ in range(n):
    num.append(int(sys.stdin.readline()))


# 산술평균
print(round(sum(num)/n))

# 중앙값
num.sort()
print(num[n//2])

# 최빈값
mode = Counter(num).most_common(2)

if len(num) > 1:
    if mode[0][1] == mode[1][1]:
        print(mode[1][0])
    else:
        print(mode[0][0])
else:
    print(mode[0][0])

# 범위
print(num[n-1]-num[0])