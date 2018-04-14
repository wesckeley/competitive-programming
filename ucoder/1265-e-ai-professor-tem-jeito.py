import ctypes

n = int(input())

for i in range(n):
    data = [float(x) for x in input().split(' ')]
    data.sort()

    e_sum = ctypes.c_float(0)
    for j in range(3,12):
        e_sum.value += data[j]
    e_sum.value /= 9
    e_sum.value *= 0.2
    e_sum.value = 5.75 - e_sum.value
    e_sum.value *= 2.5
    
    print("{0:0.2f}".format(e_sum.value) if e_sum.value <= 10 else "REPROVADO")