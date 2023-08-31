import re
def solution(files):
    file_name_list, answer = [], []
    for file in files:
        num = re.findall('\d+', file)
        num_idx = file.index(num[0])
        
        head = file[:num_idx]
        number = file[num_idx:num_idx+len(num[0])]
        tail = file[num_idx+len(num[0]):]
        
        file_name_list.append([head, number, tail])
    
    file_name_list = sorted(file_name_list, key = lambda x:(x[0].lower(), int(x[1])))
    
    for file_name in file_name_list:
        answer.append(file_name[0]+file_name[1]+file_name[2])

    return answer

    # a = sorted(files, key=lambda file : int(re.findall('\d+', file)[0]))
    # b = sorted(a, key=lambda file : re.split('\d+', file.lower())[0])
        
    # return b

files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
print(solution(files))