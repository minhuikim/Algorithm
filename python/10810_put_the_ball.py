n, m = map(int, input().split())

basket = [0 for i in range(n)]

for _ in range(m):
    i, j, k = map(int, input().split())

    for a in range(i-1, j):
        basket[a] = k

for i in range(n):
    print(basket[i], end=" ")
