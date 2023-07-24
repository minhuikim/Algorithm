def solution(cards1, cards2, goal):
    x, y = 0, 0
    for word in goal:
        if x < len(cards1) and word == cards1[x]:
            x += 1
        elif y < len(cards2) and word == cards2[y]:
            y += 1
        else:
            return 'No'
    return 'Yes'

cards1 = ["i", "drink", "water"]
cards2 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]

# cards1 = ["i", "water", "drink"]
# cards2 = ["want", "to"]
# goal = ["i", "want", "to", "drink", "water"]

print(solution(cards1, cards2, goal))