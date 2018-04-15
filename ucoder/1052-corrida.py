data = []
while(True):
    try:
        line = [int(x) for x in input().split(' ')]
    except:
        break

    data.append((line[1] / line[2],line[0]))

data.sort()

print(data[0][1])