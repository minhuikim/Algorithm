mans = int(input())
wh = ""
body = []
x = y = 0


for n in range(mans):
    wh = input()

    x = wh[:wh.find(" ")]
    y = wh[wh.find(" ")+1:]

    body.insert(n, [x, y, 0])

    print(body)
    

#     body[n].append[x, y, 1]

#     if n > 0:
#         for m in range(0, n):
#             if int(body[m].x) < int(x) & int(body[m].y) < int(y):
#                 body[n][2].append(body[n][2] + 1)


# for n in range(0,mans):
#     print(body[n][2])
