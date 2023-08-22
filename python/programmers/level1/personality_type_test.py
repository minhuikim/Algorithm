from collections import defaultdict

def addVal(score):
    if score in [1, 7]:
        return 3
    elif score in [2, 6]:
        return 2
    elif score in [3, 5]:
        return 1
    else:
        return 0
    
def solution(survey, choices):
    answer = ''
    mbti = ['RT', 'CF', 'JM', 'AN']
    survey_dict = defaultdict(int)
    for i in range(len(survey)):
        if choices[i] < 4:
            survey_dict[survey[i][0]] += addVal(choices[i])
            # survey_dict[survey[i][0]] += 4 - choices[i]
        elif choices[i] > 4:
            survey_dict[survey[i][1]] += addVal(choices[i])
            # survey_dict[survey[i][1]] += choices[i] - 4
    
    for a, b in mbti:
        if survey_dict[a] < survey_dict[b]:
            answer += b
        else:
            answer += a
            
    return answer

survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]
print(solution(survey, choices))