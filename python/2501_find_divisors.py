n, k = map(int, input().split())
div = []

for i in range(1, n+1):
    if n % i == 0:
        div.append(i)

if len(div) < k:
    print(0)
else:
    print(div[k-1])