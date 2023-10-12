def solution(n):
    answer = n
    bin_n_cnt = bin(n).count("1");
    while True:
        answer += 1
        if bin_n_cnt == bin(answer).count("1"):
            break;
    return answer

n = 78
# 83
print(solution(n))