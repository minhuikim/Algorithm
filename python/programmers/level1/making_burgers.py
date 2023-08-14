def solution(ingredient):
    answer = 0
    i = 0
    while (i + 3) < len(ingredient):
        if ingredient[i:i+4] == [1, 2, 3, 1]:
            del ingredient[i:i+4]
            answer += 1
            if i < 4:
                i = 0
            else:
                i -= 3
        else:
            i += 1
    return answer

ingredient =  [1, 1, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1]
print(solution(ingredient))