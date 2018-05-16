idx = 0
value = 0
for i in range(5):
    data_sum = sum([int(x) for x in input().split()])
    if data_sum > value:
        value = data_sum
        idx = i + 1
print("{0} {1}".format(idx, value))
