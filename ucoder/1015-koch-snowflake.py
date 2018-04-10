import math

four_nines = [1]
for i in range(1,16):
    four_nines.append(four_nines[i-1]*4/9)

while(True):
    line = input().split(' ')
    s = float(line[0])
    n = int(line[1]) - 1

    if n == -1:
        break

    a0 = s * s * math.sqrt(3) / 4
    area = 8 - (3 * four_nines[n])
    area *= a0
    area /= 5
    print("{0:.8f}".format(area))


