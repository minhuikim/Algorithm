def solution(s):
    answer = ''
    s = s.lower()
    for i in range(len(s)):
        if (i == 0 or s[i-1] == ' ') and s[i].isalpha() == True:
            answer += s[i].upper()
        else:
            answer += s[i]
    return answer

s = "3people unFollowed me"
print(solution(s))