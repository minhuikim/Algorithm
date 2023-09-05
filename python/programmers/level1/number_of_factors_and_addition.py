def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        div_list = []
        for j in range(1, int(i**(1/2))+1):
            if (i % j) == 0:
                div_list.append(j // 1)
                if (j**2) != i:
                    div_list.append(i // j)
        if len(div_list) % 2 == 0:
            answer += i
        else:
            answer -= i
        print(div_list, answer)
    return answer

left = 24
right = 27
print(solution(left, right))