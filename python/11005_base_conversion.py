n, b = map(int, input().split())
base = ""

while n > 0:
    # 나머지를 구하고 10보다 크면 A, B, C.. 로 변환
    num = n % b

    if num > 9:
        num = chr(num + 55)

    # 나머지를 마지막 자리부터 작성
    base = str(num) + base
    n = n // b

print(base)