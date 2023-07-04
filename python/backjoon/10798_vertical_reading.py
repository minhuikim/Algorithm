words = [None for _ in range(5)]

for i in range(5):
    word = input()
    words[i] = word[0:len(word)]

for j in range(15):
    for i in range(5):
        if len(words[i]) <= j:
            continue
        else:
            print(words[i][j], end="")