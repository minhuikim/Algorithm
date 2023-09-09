def solution(A,B):
    answer = 0

    A.sort()
    B.sort(reverse = True)

    for i in range(len(A)):
        for j in range(i, i + 1):
            answer += A[i] * B[j]

    return answer

A = [1, 4, 2]
B = [5, 4, 4]
print(solution(A,B))