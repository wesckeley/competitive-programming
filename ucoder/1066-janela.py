data = [int(x) for x in input().split(' ')]

window = [True for i in range(600)]

for x in data:
    for i in range(x,x+200):
        window[i] = False

area = 0
for x in window:
    if x == True:
        area += 100

print(area)
