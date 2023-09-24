def binary(n):
    tmp = ''
    while n > 0:
        tmp = str(n % 2) + tmp

        if n % 2 == 1:
            n = (n - 1) // 2
        else:
            n = n // 2

    return tmp

def solution(s):
    answer = [0, 0]
    
    while int(s) > 1:
        answer[0] += 1
        answer[1] += s.count('0')
        
        s = binary(s.count('1'))
        
    return answer

s = "110010101001" # [3, 8]
print(solution(s))