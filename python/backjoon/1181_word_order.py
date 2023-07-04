import sys

word = []
n = int(sys.stdin.readline())

for _ in range(n):
    word.append(sys.stdin.readline().replace("\n", ""))

# 중복제거
word = list(set(word))

# 사전 순서로 정렬
list.sort(word)

# 글자 길이 순서로 정렬
word.sort(key=lambda word:len(word))                # sort + lambda
# word = sorted(word, key=lambda word:len(word))    # sorted + lambda

for i in range(len(word)):
    print(word[i])