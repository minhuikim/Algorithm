n, m = map(int, input().split())
basket = list(range(1, n+1))

for k in range(m):
    i, j = map(int, input().split())

    tmp = basket[i-1]
    basket[i-1] = basket[j-1]
    basket[j-1] = tmp

for k in range(n):
    print(basket[k], end=" ")