def backtracking(n):
    if n == 1:
        return 1
    else:
        return n * backtracking(n - 1)


print(backtracking(int(input())))
