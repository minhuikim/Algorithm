def solution(number, limit, power):
    answer = 0
    for i in range(1, number+1):
        cnt = 0
        # n**1/2의 약수를 구하면 짝이되는 약수는 자동으로 구해진다. 시간복잡도 O(N^(1/2))
        for j in range(1, int(i**(1/2))+1):
            if i % j == 0:
                cnt += 1
                # n = a * b 일 때, a == b 일 수 있기 때문에 중복값 제외
                if j != (i // j):
                    cnt += 1
        if cnt > limit:
            answer += power
        else:
            answer += cnt
    return answer

number = 5
limit = 3
power = 2
print(solution(number, limit, power))