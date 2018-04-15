ns = [int(x) for x in input().split(' ')]

min_value = ns[1]
for i in range(ns[0]):
    value = int(input())
    ns[1] += value
    min_value = min(min_value,ns[1])

print(min_value)