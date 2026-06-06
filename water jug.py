a, b = 0, 0

while b != 2:
    if a == 0:
        a = 4
    elif b == 3:
        b = 0
    else:
        t = min(a, 3 - b)
        a -= t
        b += t

    print("(", a, ",", b, ")")

print("Goal Reached")