def solution(wallpaper):
    
    x, y = [], []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                x.append(i)
                y.append(j)
            
    return [min(x), min(y), max(x)+1, max(y)+1]
            
'''
    h, w = len(wallpaper), len(wallpaper[0])
    sharp = [(i, j) for j in range(w) for i in range(h) if wallpaper[i][j]=='#']
    
    lux, luy, rdx, rdy = h, w, 0, 0
    
    for i, j in sharp:
        if lux > i :
            lux = i
        if luy > j :
            luy = j
        if rdx < i :
            rdx = i
        if rdy < j :
            rdy = j
            
    return [lux, luy, rdx+1, rdy+1]
'''

wallpaper = [".#...", "..#..", "...#."]
print(solution(wallpaper)) # [0, 1, 3, 4]