n, m = map(int, input().split())

# 바구니 초기화 (1~x)
basket = [i+1 for i in range(n)]

for i in range(m):
    # 시작, 끝, 중심
    begin, end, mid = map(int, input().split())

    # 처음 바구니~시작 + 중심~끝 + 시작~중심 + 끝~마지막 바구니
    basket = basket[:begin-1] + basket[mid-1:end] + basket[begin-1:mid-1]  + basket[end:]

print(basket)