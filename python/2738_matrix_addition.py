mat1, mat2 = [], []

n, m = map(int, input().split())

for row in range(n):
    row = list(map(int, input().split()))
    mat1.append(row)

for row in range(n):
    row = list(map(int, input().split()))
    mat2.append(row)

for i in range(n):
    for j in range(m):
        print(mat1[i][j] + mat2[i][j], end=" ")
    print()