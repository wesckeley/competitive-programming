def gcd_stein(x,y):
    
    g = 1

    while x % 2 == 0 and y % 2 == 0:
        x //= 2
        y //= 2
        g *= 2

    while x != 0:
        while x % 2 == 0:
            x //= 2
        while y % 2 == 0:
            y //= 2
        if x >= y:
            x = (x - y) // 2
        else:
            y = (y - x) // 2

    return g * y

first_line = input().split(' ')
n = int(first_line[0])
m = int(first_line[1])

while gcd_stein(m,n) != 1:
    m -= 1

print(m)