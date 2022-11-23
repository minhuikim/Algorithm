import math

value = []
sum = 0

for i in range(5):
    value.append(int(input()))
    sum = sum + value[i]

for i in range(5):
    for j in range(5):
        if value[i] < value[j]:
            temp = value[i]
            value[i] = value[j]
            value[j] = temp

print(math.floor(sum/5))
print(value[2])        


# lst = []
# for i in range(5):
#     lst.append(int(input()))
# lst.sort()
# print(sum(lst)//5)
# print(lst[5//2])