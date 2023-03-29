n, m = map(int, input().split())
basket = []

for k in range(n):
    basket.append(k + 1)

for k in range(m):
    i, j = map(int, input().split())
    i = i - 1
    j = j - 1

    tmp = basket[i]
    basket[i] = basket[j]
    basket[j] = tmp

for k in range(n):
    print(basket[k], end=" ")