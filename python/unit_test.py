
park = ["OSO","OOO","OXO","OOO"]
park_len = [len(park[i]) for i in range(len(park))]
start = [(i, j) for j in range(park_len[0]) for i in range(len(park)) if park[i][j]=='S']
