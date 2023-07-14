def solution(park, routes):
    h = len(park)
    w = len(park[0])
    for i in range(h):
        for j in range(w):
            if park[i][j] == 'S':
                x, y = i, j

    for route in routes:
        op, n = route.split()
        n = int(n)
        flag = True
        for i in range(1, n+1):
            if op == 'E':
                if y + n > w - 1 or park[x][y+i] == 'X':
                    flag = False
                    break
            elif op == 'W':
                if y - n < 0 or park[x][y-i] == 'X':
                    flag = False
                    break
            elif op == 'S':
                if x + n > h - 1 or park[x+i][y] == 'X':
                    flag = False
                    break
            else:
                if x - n < 0 or park[x-i][y] == 'X':
                    flag = False
                    break

        if flag == True:
            if op == 'E':
                y = y + n
            elif op == 'W':
                y = y - n
            elif op == 'S':
                x = x + n
            else:
                x = x - n
    
    return [x, y]
    
park = ["OXXO", "XSXO", "XXXX"]
routes = ["E 1", "S 1"]
print(solution(park, routes))