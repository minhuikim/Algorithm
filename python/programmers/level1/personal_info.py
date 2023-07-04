def date_to_time(date):
    year, month, day = map(int, date.split("."))
    return year * 12 * 28 + month * 28 + day

def solution(today, terms, privacies):
    answer = []
    today_time = date_to_time(today)
    
    for i in range(len(privacies)):
        pdate, exp = privacies[i].split()     
        p_time = date_to_time(pdate)
        
        for term in terms:
            t, m = term.split()
            if exp == t:
                p_time = p_time + int(m) * 28

        if p_time <= today_time:
            answer.append(i+1)      
        
    return answer
    
# test case
today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

print(solution(today, terms, privacies))