def solution(absolutes, signs):
    # answer = 0        
    # for i, j in zip(absolutes, signs):
    #     if j:
    #         answer += i
    #     else:
    #         answer -= i
    # return answer
    return sum(i if j else -i for i, j in zip(absolutes, signs))

absolutes = [4,7,12]
signs = [True,False,True]
print(solution(absolutes, signs))