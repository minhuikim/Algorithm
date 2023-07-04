n = int(input())
numbers = input()
find = int(input())

numlist = numbers.split()
cnt = 0;

for num in numlist:
    if int(num)==find:
        cnt = cnt + 1

print(cnt)