def solution(food):
    answer = ''
    for i in range(1, len(food)):
        for j in range(food[i]//2):
            answer += str(i)
    return answer + "0" + answer[::-1]

food = [1, 3, 4, 6]
print(solution(food))