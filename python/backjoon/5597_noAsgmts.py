n = []

for i in range(28):
    n.append(int(input()))

for i in range(1, 31):
    if n.count(i) < 1:
        print(i)



# n = set()
# for i in range(8):
#     n.add(int(input()))

# a = set(range(1, 11))

# b = a - n

# print(min(b))
# print(max(b))