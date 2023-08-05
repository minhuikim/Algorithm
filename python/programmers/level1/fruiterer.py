def solution(k, m, score):
    answer = 0
    box = []
    score.sort(reverse=True)
    for i in range(len(score)):
        box.append(score[i])
        if i % m == m - 1:
            answer += min(box) * m
            box = []
    return answer

# def solution(k, m, score):
#     return sum(sorted(score)[len(score)%m::m])*m

k = 4
m = 3
score = [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]
print(solution(k, m, score))