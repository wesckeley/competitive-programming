n = int(input())
data = [int(x) for x in input().split()]

flag = False
for i in range(2, n - 1):
    flag = data[i - 1] > data[i] and data[i] < data[i + 1]
    if flag:
        break

print('S' if flag else 'N')
