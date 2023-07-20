def solution(sequence, k):
    end = 0
    seq_sum = 0
    seq_list, count = [], []
    for start in range(len(sequence)):
        # 부분합이 k보다 작으면 end포인터 뒤로 이동
        while seq_sum < k and end < len(sequence):
            seq_sum += sequence[end]
            end += 1
        # 부분합이 k값이면 배열에 배열의 길이, 시작점, 끝점 저장
        if seq_sum == k:
            count.append(end-start-1)
            seq_list.append([start, end-1])
        # 부분합이 k보다 크면 start포인터 뒤로 이동(for), 부분합에서 감소
        seq_sum -= sequence[start]

    # 가장 짧은 길이, 여러개인 경우 앞의 수열 출력
    return seq_list[count.index(min(count))]

sequence = [1, 2, 3, 4, 5]
k = 7
print(solution(sequence, k))

# 참고:투포인터 알고리즘 https://butter-shower.tistory.com/226