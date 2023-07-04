t = int(input())

change = [25, 10, 5, 1]

for i in range(t):
    c = int(input())

    for chg in change:
        print(c//chg, end=" ")
        c = c % chg