# 피보나치 수열 https://namu.wiki/w/%ED%94%BC%EB%B3%B4%EB%82%98%EC%B9%98%20%EC%88%98%EC%97%B4
def solution(n):
    answer = 0
    fx, fy = 0, 1
    for i in range(2, n + 1):
        answer = fx + fy
        fx = fy
        fy = answer
    return answer % 1234567

# 시간초과
# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         # print(n, n-2, n-1)
#         return fibonacci(n - 2) + fibonacci(n - 1)

# def solution(n):
#     answer = 0
#     return fibonacci(n)

n = 3
#2
print(solution(n))