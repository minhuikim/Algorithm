# def solution(s, skip, index):
#     answer = ''
#     for word in s:
#         i = 0
#         word = ord(word)
#         while i < index:
#             word += 1
#             if word == 123:
#                 word = 97
#             if chr(word) not in skip:
#                 i += 1
#         answer += chr(word)
#     return answer

from string import ascii_lowercase

def solution(s, skip, index):
    result = ''

    a_to_z = set(ascii_lowercase)
    a_to_z -= set(skip)
    a_to_z = sorted(a_to_z)
    l = len(a_to_z)

    dic_alpha = {alpha:idx for idx, alpha in enumerate(a_to_z)}

    print(dic_alpha)

    for i in s:
        result += a_to_z[(dic_alpha[i] + index) % l]
        print((dic_alpha[i] + index), l, (dic_alpha[i] + index) % l)

    return result

s = "aukks"
skip = "wbqd"
index = 5
#  "happy"

# s = "y"
# skip = "baz"
# index = 1
# c

print(solution(s, skip, index))