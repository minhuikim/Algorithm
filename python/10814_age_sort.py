import sys

n = int(sys.stdin.readline())

x = []

for i in range(n):
    x.append(list(sys.stdin.readline().split()))
    x[i][0] = int(x[i][0])

# index 순서 지키면서 나이순으로 정렬
x.sort(key = lambda x:x[0])

for i in range(n):
    print(x[i][0], x[i][1])