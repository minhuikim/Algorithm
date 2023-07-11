def solution(players, callings):
    p_idx_dict = {player:i for i, player in enumerate(players)} # 선수:등수
    idx_p_dict = {i:player for i, player in enumerate(players)} # 등수:선수
    
    for call in callings:
        cur_idx = p_idx_dict[call]          # 현재 등수
        pre_idx = cur_idx - 1               # 이전 등수
        
        cur_player = call                   # 추월한 선수
        pre_player = idx_p_dict[pre_idx]    # 추월된 선수, 등수:선수에서 이전 등수로 추출
        
        # 선수:등수 dict에서 현재 선수, 이전 선수 등수 업데이트
        p_idx_dict[cur_player] = pre_idx
        p_idx_dict[pre_player] = cur_idx
        
        # 등수:선수 dict에서 현재 등수, 이전 등수의 선수 업데이트
        idx_p_dict[pre_idx] = cur_player
        idx_p_dict[cur_idx] = pre_player
        
    # 등수:선수 dict에서 value만 추출해서 리스트로 변환하여 출력    
    return list(idx_p_dict.values()) 

players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]

print(solution(players, callings))
#['mumu', 'kai', 'mine', 'soe', 'poe']