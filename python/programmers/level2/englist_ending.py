#https://school.programmers.co.kr/learn/courses/30/lessons/12981
def solution2(n, words):
    for p in range(1, len(words)):
        if words[p][0] != words[p-1][-1] or words[p] in words[:p]: return [(p%n)+1, (p//n)+1]
    else:
        return [0,0]

def solution(n, words):
    end = ''
    old_words = []
    man_cnt, end_cnt = 1, 1
    for i in range(len(words)):
        if man_cnt > n:
            man_cnt = 1
            end_cnt += 1
        
        if end != '' and end != words[i][0] or old_words.count(words[i]):
            return [man_cnt, end_cnt]

        old_words.append(words[i])
        end = words[i][-1]
        man_cnt += 1

    return [0,0]

n = 5
words = ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]
# [0, 0]

n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
# [3, 3]

n = 2
words = ["hello", "one", "even", "never", "now", "world", "draw"]
# [1, 3]
print(solution2(n, words))