n = int(input())
data = [int(x) for x in input().split(' ')]

for i in range(n-1,0,-1):
    for j in range(0,i):
        data[j] *= data[j+1]

print('preta' if data[0] == 1 else 'branca')