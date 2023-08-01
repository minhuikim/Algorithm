def solution(s):
    answer = 0

    i, j, x, y = 0, 0, 0, 0
    while i < len(s):
        if s[i] == s[j]:
            x += 1
        else:
            y += 1
        j += 1
        if x == y:
            x, y = 0, 0
            answer += 1
            i = j
            continue
        
        if len(s) <= j + 1:
            answer += 1
            break

    return answer

s = "abracadabra"
print(solution(s))