from collections import defaultdict

def solution(id_list, report, k):
    id_dict = {i:0 for i in id_list}
    report_dict = defaultdict(set)
    
    for i in report:
        report_dict[i.split()[1]].add(i.split()[0])
    
    for i in report_dict:
        if len(report_dict[i]) >= k:
            for j in report_dict[i]:
                id_dict[j] += 1
                
    return list(id_dict.values())

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
print(solution(id_list, report, k))