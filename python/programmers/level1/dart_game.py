import re

def solution(dartResult):
    score_dict = {'S':1, 'D':2, 'T':3}
    result_list = re.split('([^0-9])', dartResult)
    result_list = list(filter(None, result_list))

    score, j = [], 0
    for i in range(len(result_list)):
        if result_list[i].isdigit():
            score.append(int(result_list[i]))
            if i > 0:
                j += 1
        else:
            if result_list[i] == '*':
                if(len(score)>1):
                    score[j-1] *=2
                score[j] *= 2
            elif result_list[i] == '#':
                score[j] *= -1
            else:
                score[j] **= score_dict[result_list[i]]

    return sum(score)

dartResult = "1S2D*3T" # 37
# dartResult = "1D2S#10S" # 9
# dartResult = "1S*2T*3S" # 23
dartResult = "1T2D3D#" # -4
dartResult = "1D2S3T*" # 59
print(solution(dartResult))