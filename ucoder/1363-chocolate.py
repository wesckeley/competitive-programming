# WA
# https://gitlab.com/pufe/elixir-day-2/blob/master/chocolate/input

import ctypes

t = int(input())

for i in range(t):
    nm = [int(x) for x in input().split(' ')]

    sum_list = [0 for i in range(nm[1])]
    sum_total = 0
    for j in range(nm[0]):
        data = [int(x) for x in input().split(' ')]
        for k in range(nm[1]):
            sum_list[k] += data[k]
            sum_total += data[k]

    q = int(input())

    a = ctypes.c_float(sum_list[q-1])
    b = ctypes.c_float(sum_total)
    a.value /= b.value

    print("{0:0.2f}".format(a.value))
