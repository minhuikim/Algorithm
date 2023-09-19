# 동적계획법
# https://codedrive.tistory.com/49
def solution(triangle):
    # 아래로 갈수록 값을 더해가며 진행
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][0] += triangle[i-1][0]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                if triangle[i-1][j-1] < triangle[i-1][j]:
                    triangle[i][j] += triangle[i-1][j]
                else:
                    triangle[i][j] += triangle[i-1][j-1]
    
    return max(triangle[len(triangle)-1])

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))