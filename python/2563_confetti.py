piece = int(input())

xy = [[0 for j in range(100)] for i in range(100)]
area = 0

for p in range(piece):
    x, y = map(int, input().split())
    
    # x축 3 -> 3~13까지 +1
    # y축 7 -> 7~17까지 +1
    for i in range(x, x+10):
        for j in range(y, y+10):
            xy[i][j] = 1

for i in range(100):
    for j in range(100):
        if xy[i][j] > 0:
            area = area + 1

print(area)