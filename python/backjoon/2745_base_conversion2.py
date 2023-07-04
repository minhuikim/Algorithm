b, n = input().split()
n = int(n)
base = 0

for i in range(len(b)):
    num = b[-1]                 # 마지막 글자만 추출
    
    if num.isalpha():           # 알파벳인 경우 -55 (A-55 = 10)
        num = ord(num) - 55
    
    # 10진법 변환 (진법 거듭제곱 후 더하기)
    base = base + int(num) * (n ** i)
    b = b[0:len(b)-1]

print(base)