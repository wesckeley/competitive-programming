euler = [1]
factorial = 1

for i in range(1,13):
    factorial *= i
    euler.append(euler[i-1] + (1 / factorial))

while(True):
    n = int(input())
    if n != -1:
        print("{0:0.6f}".format(euler[n]))
    else:
        break