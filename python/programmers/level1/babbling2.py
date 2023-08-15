def solution(babbling):
    answer = 0
    pron = ['aya', 'ye', 'woo', 'ma']

    for b in babbling:
        i = 0
        tmp = ''
        while i < len(b):
            if b[i:i+2] == tmp or b[i:i+3] == tmp:
                break
            if b[i:i+2] in pron:
                tmp = b[i:i+2]
                i += 2
            elif b[i:i+3] in pron:
                tmp = b[i:i+2]
                i += 3
            else:
                break
        if i == len(b):
            answer += 1

    return answer

babbling = ["ayayemaaya"]
print(solution(babbling))