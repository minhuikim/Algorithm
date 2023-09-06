# 탐욕법 https://school.programmers.co.kr/questions/42177
def solution(cap, n, deliveries, pickups):
    answer = 0
    print(deliveries, pickups, deliveries[0], pickups[0])
    deli = pick = 0
    for i in range(n-1, -1, -1):
        print(i, deliveries[i], pickups[i])
        cnt = 0
        print(deli, deliveries[i], deli < deliveries[i], pick, pickups[i], pick < pickups[i])
        while deli < deliveries[i] or pick < pickups[i]:
            cnt += 1
            deli += cap
            pick += cap
            print(i, cnt, deli, pick, deliveries[i], pickups[i], answer)
        deli -= deliveries[i]
        pick -= pickups[i]
        answer = answer + ((i+1)*cnt*2)
        print(i, deli, pick, deliveries[i], pickups[i], answer)
    return answer

cap = 2
n = 2
deliveries = [1, 0]	
pickups = [1, 0]
# 2
print(solution(cap, n, deliveries, pickups))