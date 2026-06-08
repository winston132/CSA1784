def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)

# Test cases
print("Sum =", sum_n(5))   # 15
print("Sum =", sum_n(10))  # 55