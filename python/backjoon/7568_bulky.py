mans = int(input())
wh = ""
x = y = 0
man_x = {}
man_y = {}
man_s = {}
max = 0
score = {}

for n in range(0, mans):
    wh = input()

    x = wh[:wh.find(" ")]
    y = wh[wh.find(" ")+1:]

    man_x[n] = x
    man_y[n] = y

for n in range(0, mans):
    for m in range(0, n):
        break

print(score)