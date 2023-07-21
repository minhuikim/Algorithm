def solution(keymap, targets):
    answer = []
    key_dict = {}
    for key in keymap:
        for char in key:
            # char의 index가 dict에 있는 경우 dict에 있는 값보다 크면 저장하지않음
            if char in key_dict.keys() and key.index(char) + 1 > key_dict[char]:
                continue
            key_dict[char] = key.index(char)+1

    # 간소화
    # for key in keymap:
    #     for i, char in enumerate(key):
    #         key_dict[char] = min(i + 1, key_dict[char]) if char in key_dict else i + 1
    
    for target in targets:
        count = 0
        for char in target:
            if char not in key_dict.keys():
                count = -1
                break
            count += key_dict[char]
                
        answer.append(count)

    return answer

keymap = ["BCEFD", "ABACD"]
targets = ["ABCD","AABB"]
# [9, 4]

# keymap = ["BC"]
# targets = ["AC", "BC"]
# [-1, 3]

print(solution(keymap, targets))