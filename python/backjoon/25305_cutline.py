n, k = map(int, input().split())

x = list(map(int, input().split()))

for i in range(n):
    for j in range(n):
        if x[i] > x[j]:
            tmp3 = x[j]
            x[j] = x[i]
            x[i] = tmp3

print(x[k-1])