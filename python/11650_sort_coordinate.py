import sys

n = int(sys.stdin.readline())
xy = []

for _ in range(n):
    xy.append(list(map(int, sys.stdin.readline().split())))

# 정렬 -> x좌표 정렬 후 y좌표 정렬
xy.sort(key = lambda cdnt : (cdnt[0], cdnt[1]))

for i in range(n):
    print(xy[i][0], xy[i][1])

''' 
시간제한

def sort_num(a, b):
    tmp = a
    a = b
    b = tmp
    return a, b

for i in range(n):
    for j in range(n):
        if xy[i][0] < xy[j][0]:
            xy[i], xy[j] = sort_num(xy[i], xy[j])

        if xy[i][0]==xy[j][0] and xy[i][1] < xy[j][1]:
            xy[i], xy[j] = sort_num(xy[i], xy[j])
'''