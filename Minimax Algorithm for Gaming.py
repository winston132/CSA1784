def minimax(a, maxp):
    if len(a) == 1:
        return a[0]
    if maxp:
        return max(minimax(a[:len(a)//2], False),
                   minimax(a[len(a)//2:], False))
    else:
        return min(minimax(a[:len(a)//2], True),
                   minimax(a[len(a)//2:], True))

scores = [3, 5, 2, 9]
print("Best value for MAX player:", minimax(scores, True))