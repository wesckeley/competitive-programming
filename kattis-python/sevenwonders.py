data = input()
data_sum = [0, 0, 0]
for x in data:
    if x == 'T':
        data_sum[0] += 1
    elif x == 'C':
        data_sum[1] += 1
    else:
        data_sum[2] += 1

seven = min(data_sum) * 7
data_sum = [x * x for x in data_sum]
print("{0}".format(seven + sum(data_sum)))
