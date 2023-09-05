def find_last(n, deliveries, pickups):
    print(n, deliveries, pickups)
    # for i in reversed(range(n)):
    #     print(i, deliveries[i], pickups[i])
    #     if deliveries[i] > 0 or pickups[i] > 0:
    return 0

def solution(cap, n, deliveries, pickups):
    answer = 0
    
    x, y = cap, n - 1
    flag = True
    while max(deliveries) > 0 or max(pickups) > 0:
        # 배달
        if flag == True:
            if x > 0:
                x -= 1
                deliveries[y] -= 1
            else:
                answer += n
                # 차 비면 끝에서 회수
                y = n - 1
                flag = False
        else:
            if x < cap:
                # 회수 하나씩 추가
                x += 1
                pickups[y] -= 1
            else:
                answer += n
                y = find_last(n, deliveries, pickups)
                n = y + 1
                break
                                
    return answer

cap = 4
n = 5
deliveries = [1, 0, 3, 1, 2]
pickups = [0, 3, 0, 4, 0]

print(solution(cap, n, deliveries, pickups))