# 값이 0인 2차원 배열 생성
rows = 5
cols = 5
array = [[0 for j in range(cols)] for i in range(rows)]

print(array)
# [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

#------------------------------------------------------------#

# 10칸의 배열에 띄어쓰기 형식으로 입력되는 값 int형식으로 저장
tmp1 = 5
tmp2 = []
for p in range(tmp1):
    tmp2.append(list(map(int, input().split())))

print(tmp2)
# input
# 1 2 3 4 5 
# 1 2 3 
# 1 2 
# 1 2 3 4 5 6 7
# 3 2 1

# result
# [[1, 2, 3, 4, 5], [1, 2, 3], [1, 2], [1, 2, 3, 4, 5, 6, 7], [3, 2, 1]]