mans = int(input())
wh = ""
human = {}
key_val = {}
x = y = 0



for n in range(0, mans):
    wh = input()

    x = wh[:wh.find(" ")]
    y = wh[wh.find(" ")+1:]

    key_val = {}
    key_val[x] = y
    human[n] = key_val

    # print(body)
    

#     body[n].append[x, y, 1]

#     if n > 0:
#         for m in range(0, n):
#             if int(body[m].x) < int(x) & int(body[m].y) < int(y):
#                 body[n][2].append(body[n][2] + 1)


# for n in range(0,mans):
#     print(body[n][2])

# dic_key_max = max(body.keys())
# print(dic_key_max)
# dic_val_max = max(body.values())
# print(dic_val_max)
print(human)
# print(body)