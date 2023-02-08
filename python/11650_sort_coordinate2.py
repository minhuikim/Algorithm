import sys

n = int(sys.stdin.readline())
xy = []

for _ in range(n):
    xy.append(list(map(int, sys.stdin.readline().split())))

# 정렬 -> y좌표 정렬 후 x좌표 정렬
xy.sort(key = lambda cdnt : (cdnt[1], cdnt[0]))

for i in range(n):
    print(xy[i][0], xy[i][1])
