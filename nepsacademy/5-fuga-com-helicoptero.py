data = [int(x) for x in input().split(' ')]

if data[3] == 1:
    if data[0] < data[2]:
        data[0] += 16
    if data[1] < data[2]:
        data[1] += 16
    print("S" if data[0] < data[1] else "N")
else:
    if data[0] > data[2]:
        data[0] -= 16
    if data[1] > data[2]:
        data[1] -= 16
    print("S" if data[0] > data[1] else "N")