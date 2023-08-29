def solution(numbers):
    return sum(set(range(10)) - set(numbers))
    # return 45 - sum(numbers)
    # solution = lambda x: sum(range(10)) - sum(x)

numbers = [1,2,3,4,6,7,8,0]
print(solution(numbers))