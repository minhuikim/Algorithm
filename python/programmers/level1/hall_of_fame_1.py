def solution(k, score):
    answer = []

    hall = []
    for i in score:
        if len(hall) < k:
            hall.append(i)
        elif min(hall) < i:
            hall[hall.index(min(hall))] = i
        answer.append(min(hall))
            
    return answer

k = 3
score = [10, 100, 20, 150, 1, 100, 200]
print(solution(k, score))