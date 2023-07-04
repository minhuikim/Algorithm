n, m = map(int, input().split())
basket = [(i+1) for i in range(n)]

for k in range(m):
    i, j = map(int, input().split())

    tmp = basket[i-1:j]
    tmp.reverse()
    basket[i-1:j] = tmp
   
for k in range(n):
    print(basket[k], end=" ")
