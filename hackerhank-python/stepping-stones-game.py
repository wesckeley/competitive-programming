import math


t = int(input())

for i in range(t):
    n = int(input())
    delta = math.sqrt(1 + 8 * n)

    flag = True
    if delta != int(delta):
        flag = False
    else:
        delta = int(delta) - 1
        if delta % 2 != 0:
            flag = False
        else:
            delta //= 2

    print('Go On Bob {0}'.format(delta) if flag else 'Better Luck Next Time')
