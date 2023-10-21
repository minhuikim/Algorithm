#https://school.programmers.co.kr/learn/courses/30/lessons/12973
def solution(s):
    stack = []
    for i in s:
        if len(stack) > 0 and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)

    if len(stack) == 0:
        return 1
    else:
        return 0

s = 'aaa'       # 0
s = 'baabaa'    # 1
s = 'cdcd'      # 0
print(solution(s))