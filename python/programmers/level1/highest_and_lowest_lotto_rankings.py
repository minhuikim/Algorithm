# https://school.programmers.co.kr/learn/courses/30/lessons/77484
def solution(lottos, win_nums):
    rank_dict = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    zero = lottos.count(0)
    match = 0
    for i in lottos:
        if i in win_nums:
            match += 1
            
    return [rank_dict[match+zero], rank_dict[match]]

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
# [3, 5]
print(solution(lottos, win_nums))