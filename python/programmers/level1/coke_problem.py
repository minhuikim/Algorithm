def solution(a, b, n):
    answer = 0
    while n // a > 0:
        print("현재 병", n
            , "바꾼 병수", (n // a) * b
            , "남은 병", n % a)

        answer += ((n // a) * b)
        n = ((n // a) * b) + n % a
    return answer

a = 2
b = 1
n = 20
print(solution(a, b, n))