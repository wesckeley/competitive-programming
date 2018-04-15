n = int(input())
counting_sort = [0 for i in range(201)]
data = [int(x) for x in input().split(' ')]

for x in data:
    counting_sort[x] += 1

idx_max = 0
for i in range(201):
    if counting_sort[i] >= counting_sort[idx_max]:
        idx_max = i

print(idx_max)