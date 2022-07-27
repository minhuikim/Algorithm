num = int(input())

if num<10:
    print(0)
else:
    for n in range(10, num):
        i = int(10)
        sum = int(n)
        m = int(n)

        while i < n:
            if sum == n:
                sum += n % i
            sum += n // i % i
            i *= 10
        
        if sum == num:
            break
        elif n == num:
            m = 0
            break 

    print(n)
