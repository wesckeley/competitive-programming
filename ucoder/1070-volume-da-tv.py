vt = [int(x) for x in input().split(' ')]
data = [int(x) for x in input().split(' ')]

for x in data:
    vt[0] += x
    if vt[0] < 0:
        vt[0] = 0
    if vt[0] > 100:
        vt[0] = 100

print(vt[0])
