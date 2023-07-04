score = 0
count = 0

def rtn_score(c):
    if c[0] == 'A':
        score = 4
    elif c[0] == 'B':
        score = 3
    elif c[0] == 'C':
        score = 2
    elif c[0] == 'D':
        score = 1
    else:
        score = 0
    
    if c[-1:] == '+':
        return float(score) + 0.5
    else:
        return float(score)

for i in range(20):
    a, b, c = input().split()

    if c == 'P' :
        continue

    score = score + rtn_score(c) * float(b)
    count = count + float(b)
        
print(round(score/count, 6))