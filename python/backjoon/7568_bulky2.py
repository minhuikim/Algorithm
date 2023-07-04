mans = int(input())
bulky = [[0 for i in range(2)] for j in range(mans)]
max_x = max_y = 9
min_x = min_y = 201
grade = [] * mans
g = 1

for man in range(mans):
    xy = input()
    xy = xy.split()
    xy[0] = xy[0]
    xy[1] = xy[1]
    bulky[man] = [xy[0], xy[1]]

    if int(max_x) < int(xy[0]) and int(max_y) < int(xy[1]):
        max_x = xy[0]
        max_y = xy[1]

    if int(min_x) > int(xy[0]) and int(min_x) > int(xy[1]):
        min_x = xy[0]
        min_y = xy[1]

print(bulky)
print("max: " + max_x + " " + max_y)
print("min: " + min_x + " " + min_y)

for man in range(mans):

    print(bulky[man][0] + " " + bulky[man][1])

    if int(bulky[man][0]) == int(max_x) and int(bulky[man][1]) == int(max_y[1]):
        print(1)
        grade.insert(man, g)
        g = g + 1
    elif int(bulky[man][0]) == int(min_x) and int(bulky[man][1]) == int(min_y[1]):
        print(2)
        grade.insert(man, mans)
    else:
        print(3)
        grade.insert(man, 2)
        
        # if int(bulky[man][0]) >= int(bulky[m][0]) & int(bulky[man][1]) >= int(bulky[m][0]):
            # grade[man] = 1
        # print(bulky[man][0] + " " + bulky[man][1])


print(grade)
