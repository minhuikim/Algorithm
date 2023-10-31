from collections import deque
def solution(people, limit):
    people.sort()
    people_deque = deque(people)
    answer = 0
    while people_deque:
        if len(people_deque) <= 1:
            answer += 1
            break
                
        if people_deque[0] + people_deque[-1] <= limit:
            people_deque.popleft()
            people_deque.pop()
        else:
            people_deque.pop()
        answer += 1

    return answer

people = [70, 50, 80, 50]
limit = 100
# 3

people = [70, 80, 50]
limit = 100
# 3

people = [10,20,30,40,50,60,70,80,90]
limit = 100
# 5

# people = [40,40,40]
# limit = 100
# 2

print(solution(people, limit))