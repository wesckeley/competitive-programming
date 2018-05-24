n = int(input())

data = []
for i in range(n):
    data.append([])
    data[i] = [int(x) for x in input().split()]

for i in range(1, n):
    for j in range(1, n):
        values = [data[i - 1][j], data[i][j - 1], data[i - 1][j - 1]]
        values.sort()
        data[i][j] = (values[1] + 1) % 2

print(data[n - 1][n - 1])
