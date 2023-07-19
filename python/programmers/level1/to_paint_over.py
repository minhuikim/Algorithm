def solution(n, m, section):
    
    answer = 0
    brush = 0
    for sec in section:
        if brush <= sec:
            brush = sec + m
            answer = answer + 1

    return answer

n = 8
m = 4
section = [2, 3, 6]
print(solution(n, m, section))