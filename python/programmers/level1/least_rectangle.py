def solution(sizes):
    max_x, max_y = 0, 0
    for x, y in sizes:
        if x < y:
            x, y = y, x
        if max_x < x:
            max_x = x
        if max_y < y:
            max_y = y
    return max_x * max_y

    #   return max(max(x) for x in sizes) * max(min(x) for x in sizes)

sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
print(solution(sizes))