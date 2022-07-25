n = int(input())
num = int(0)

if n<10:
    print(n)
else:
    for num in range(10, n):
        i = int(10)
        sum = int(num)
        print("print")
        
        while num > 0:
            sum += num % i
            num = num // i
            i = i * 10
        if sum==n:
            m = n
            exit
    print(m)
