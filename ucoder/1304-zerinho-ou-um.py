data = [int(x) for x in input().split(' ')]

if data[0] != data[1] and data[0] != data[2]:
    print("A")
elif data[1] != data[0] and data[1] != data[2]:
    print("B")
elif data[2] != data[0] and data[2] != data[1]:
    print("C")
else:
    print("*")