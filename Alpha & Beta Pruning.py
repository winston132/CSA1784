def alphabeta(scores, a, b):
    v = max(min(scores[0], scores[1]),
            min(scores[2], scores[3]))
    return v

scores = [3, 5, 9, 12]
print("Optimal value with Alpha-Beta pruning:", alphabeta(scores, -999, 999))