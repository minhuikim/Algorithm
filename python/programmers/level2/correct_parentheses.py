# 스택, 큐를 통해 풀이하여 유효성 검사 통과
def solution(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')' and stack and stack[len(stack)-1] == '(':
            stack.pop()
        else:
            return False
    
    return len(stack) == 0

s = "(())()"
s = "(()("
print(solution(s))