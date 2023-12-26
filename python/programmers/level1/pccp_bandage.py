# [PCCP 기출문제] 1번 / 붕대 감기
# https://school.programmers.co.kr/learn/courses/30/lessons/250137
def solution(bandage, health, attacks):
    max_health = health
    tmp = 0
    for attack in attacks:
        health += ((attack[0] - tmp - 1) * bandage[1])

        if (attack[0] - tmp) > bandage[0]:
            health += (bandage[2] * ((attack[0] - tmp) // bandage[0]))
        
        if max_health < health:
            health = max_health
            
        health -= attack[1]
        
        if health < 1:
            return -1
        
        tmp = attack[0]

    return health

bandage = [3, 2, 7]
health = 20
attacks = [[1, 15], [5, 16], [8, 6]]

# bandage = [5, 1, 5]
# health = 30
# attacks = [[2, 10], [9, 15], [10, 5], [11, 5]]

# health=20
# bandage =[2, 1, 3]
# attacks=[[1, 15], [6, 2]] 

print(solution(bandage, health, attacks))

'''
0 20        0 X
1 5(-15)    0 O
2 6(+1)     1 X
3 10(+4)    2 X
4 11(+1)    1 X
5 15(+4)    2 X
6 13(-2)    0 O
'''