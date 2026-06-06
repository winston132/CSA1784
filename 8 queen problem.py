N = 8
count = 0

def safe(b, r, c):
    for i in range(c):
        if b[i] == r or abs(b[i] - r) == abs(i - c):
            return False
    return True

def solve(b, c):
    global count
    if c == N:
        count += 1
        if count == 1:
            for r in range(N):
                print(*["Q" if b[col] == r else "-" for col in range(N)])
        return

    for r in range(N):
        if safe(b, r, c):
            b[c] = r
            solve(b, c + 1)

b = [-1] * N
solve(b, 0)
print("\nTotal solutions:", count)