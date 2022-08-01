num = int(input())
r = 0

for n in range(1, num+1):
    a = list(map(int, str(n)))
    r = n + sum(a)

    if r == num:
        print(n)
        break
    
    if n == num:
        print(0)
    