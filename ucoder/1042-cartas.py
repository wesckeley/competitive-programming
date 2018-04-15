data = [int(x) for x in input().split(' ')]
c = True
d = True

for i in range(4):
    c &= data[i] < data[i+1]
    d &= data[i] > data[i+1]

if c == True:
    print('C')
elif d == True:
    print('D')
else:
    print('N')