mans = int(input())
x = y = {}
score = {}

for man in range(mans):
    xy = input()

    x[man] = int(xy[:xy.find(" ")])
    y[man] = int(xy[xy.find(" ")+1:])

    if man > 0:
        if x[man-1] < x[man]:
            big_x = x[man]

        if y[man-1] < y[man]:
            big_y = y[man]

        if x[man] == big_x & y[man] == big_y:
            score[man] = 1
        else:
            score[man] = 2

for s in score:
    print(s)

