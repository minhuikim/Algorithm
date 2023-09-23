def solution(x, n):
    # end = x * n - 1 if x < 0 else x * n + 1
    # return [0 for x in range(x, n)] if x == 0 else [i for i in range(x, end, x)]
    
    # return [0 for x in range(x, n)] if x == 0 else [i for i in range(x, x*(n+1), x)]
    
    return [i * x + x for i in range(n)] 
        
# [2,4,6,8,10]
x = 2
n = 5

# [-4, -8]
x = -4
n = 2

# [0, 0, 0]
x = 0
n = 3
print(solution(x, n))