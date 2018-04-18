n = int(input())
data = [int(x) & 0x07 for x in input().split(' ')]

answer = 1 if data[0] == 0 else 0

data_sum = []
data_sum.append([0 for i in range(8)])
data_sum[0][data[0]] = 1

for i in range(1,n):
    data_sum.append([0 for i in range(8)])
    data_sum[i][data[i]] = 1
    for j in range(8):
        data_sum[i][(j + data[i]) & 0x07] += data_sum[i-1][j]
    answer += data_sum[i][0]

print(answer)
