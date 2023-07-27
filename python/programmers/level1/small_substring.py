def solution(t, p):
    answer = 0 

    for i in range(len(t)-len(p)+1):
        if p >= t[i:i+len(p)]:
            answer += 1
    
    return answer

t = "3141592"
p = "271"
# 2
print(solution(t, p))