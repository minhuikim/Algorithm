while True:
    n = int(input())

    if n == -1:
        break

    div = []

    for i in range(1, n):
        if n % i == 0:
            div.append(i)

    if sum(div) == n:
        print(n, "=", end=" ")
        for i in div:
            if i == div[-1]:
                print(i)
            else:
                print(i, "+", end=" ")
    else:
        print(n, "is NOT perfect.")