n = int(input())
numbers = []

for i in range(n):
    numbers.insert(i, input())

for i in range(n):
    for j in range(n):
        if int(numbers[i]) < int(numbers[j]):
            temp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = temp

for i in range(n):
    print(numbers[i])