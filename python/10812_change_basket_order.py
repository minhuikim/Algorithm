n, m = map(int, input().split())

# 바구니 초기화 (1~x)
basket = [i+1 for i in range(n)]
tmp = []

for i in range(m):
    # 시작, 끝, 중심
    begin, end, mid = map(int, input().split())

    # 배열 index 순서를 맞추기 위해 1씩 감소
    begin = begin - 1
    end = end - 1
    mid = mid - 1

    tmp = basket.copy()

    # basket[begin] = basket[mid]
    # basket[mid] = basket[begin]
    # basket[end] = basket[mid-1]

    for j in range(mid):
        basket[begin+j] = tmp[mid+j]
        basket[mid+j] = tmp[begin+j]

        print(basket)

    basket[end] = tmp[mid-1]

print(basket)

'''
1 2 3 4 5 6 7 8 9 10
1 6 4
2 3 4 5 6 1 7 8 9 10
3 4 5 6 1 2 7 8 9 10
4 5 6 1 2 3 7 8 9 10
3 9 8
4 5 8 9 6 1 2 3 7 10




'''

        # tmp = basket[mid+j]
        # basket[mid+j] = basket[j]
        # basket[j] = tmp
