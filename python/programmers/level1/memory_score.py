def solution(name, yearning, photo):
    answer = []

    score_dict = dict(zip(name, yearning))
    
    for mans in photo:
        score = 0
        for man in mans:
            if man in score_dict:
                score = score + score_dict[man]
        answer.append(score)
    
    return answer

name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"], ["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]

print(solution(name, yearning, photo))
