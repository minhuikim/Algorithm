n = int(input())
numbers = []

for i in range(n):
    numbers.append(int(input()))

# nums = sorted(numbers)
numbers.sort()

# print(*nums, sep='\n')
print(*numbers, sep='\n')