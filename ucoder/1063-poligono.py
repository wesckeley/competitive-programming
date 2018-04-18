n = int(input())
data = [int(x) for x in input().split(' ')]
data.sort()

count = 0
sum_sides = 0

for i in range(n):
    if data[i] < sum_sides:
        count = i + 1
    sum_sides += data[i]

print(count)
