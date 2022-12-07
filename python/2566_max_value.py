a = []

for i in range(9):
    a.append(list(map(int, input().split())))

max = x = y = 0

for i in range(9):
    for j in range(9):
        if max < a[i][j]:
            max = a[i][j]
            x = i
            y = j

print(max)
print(x + 1, y + 1)