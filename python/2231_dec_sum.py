num = int(input())

if num<=10:
    print(num)
else:
    for n in range(10, num):
        i = int(10)
        sum = int(n)
        m = int(0)

        while i <= n:
            if sum == n:
                sum += n % i
            sum += n // i % i
            i *= 10
        
        if sum == num:
            m = int(n)
            break

    print(m)