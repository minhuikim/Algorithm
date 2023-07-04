import sys

n = int(input())
nums = [0] * 10001                  # 입력숫자가 10000이하의 자연수

for i in range(n):
    num = int(sys.stdin.readline()) # input보다 빠른 입력
    nums[num] += 1                  # 입력된 자리에 +1

for i in range(10001):
    if nums[i] != 0:
        for j in range(nums[i]):    # 입력된 숫자만큼 출력
            print(i)