def gcd(x,y):
    g = 1
    while x & 0x01 == 0x00 and y & 0x01 == 0x00:
        g <<= 1
        x >>= 1
        y >>= 1
    while x != 0:
        while x & 0x01 == 0x00:
            x >>= 1
        while y & 0x01 == 0x00:
            y >>= 1
        if x >= y:
            x = (x - y) >> 1
        else:
            y = (y - x) >> 1
    return g * y

def lcm(a, b):
    return a * b // gcd(a, b)

data = [int(x) for x in input().split(' ')]

q = lcm(data[1],data[3])
data[0] *= q // data[1]
data[2] *= q // data[3]
p = data[0] + data[2]

div = gcd(p,q)
p //= div
q //= div

print('{0} {1}'.format(p, q))
