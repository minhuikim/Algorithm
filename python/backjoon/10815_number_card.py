import sys

n = int(sys.stdin.readline())
card = list(map(int, (sys.stdin.readline().split())))

m = int(sys.stdin.readline())
chk_list = list(map(int, (sys.stdin.readline().split())))

# 정렬
card.sort()

# 이진탐색
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

for i in range(m):
    if binary_search(card, chk_list[i], 0, n-1) is not None:
        print(1, end=' ')
    else:
        print(0, end=' ')