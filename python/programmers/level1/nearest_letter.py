def solution(s):
    answer = []
    for i in range(len(s)-1, -1, -1):
        for j in range(i-1, -1, -1):
            if s[i]==s[j]:
                answer.append(i-j)
                break
        else:
            answer.append(-1)

    answer = answer[::-1]
    
    return answer


s = "banana"
print(solution(s))


# def solution(s):
#     answer = []
#     dic = dict()
#     for i in range(len(s)):
#         if s[i] not in dic:
#             answer.append(-1)
#         else:
#             answer.append(i - dic[s[i]])
#         dic[s[i]] = i

#     return answer