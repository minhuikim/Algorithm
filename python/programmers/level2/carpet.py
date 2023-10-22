# https://school.programmers.co.kr/learn/courses/30/lessons/42842
def solution(brown, yellow):
    answer = []
    i = 1
    while i <= yellow:
        # 6 * 2 + 4 * 2 + 4 = 24
        if yellow % i == 0 and i * 2 + (yellow // i) * 2 + 4 == brown:
            answer = [yellow//i + 2, i + 2]
            break
        i += 1
    return answer

brown = 10
yellow = 2
# [4, 3]

brown = 24
yellow = 24
# [8, 6]
print(solution(brown, yellow))