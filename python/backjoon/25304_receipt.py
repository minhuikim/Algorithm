X = int(input())
N = int(input())
c = 0

for n in range(N):
    ab = input()
    ab = ab.split(" ")
    a = int(ab[0])
    b = int(ab[1])
    c = c + (a * b)

if X==c:
    print("Yes")
else:
    print("No")
