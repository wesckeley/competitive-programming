n, m = map(int, input().split())

n -= m
print('0' if n < 0 else n * 4)
