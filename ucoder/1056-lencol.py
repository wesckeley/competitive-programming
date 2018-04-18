import itertools

def swap(i,j):
    global data
    x = data[i]
    data[i] = data[j]
    data[j] = x

def check(x,y,_x,_y,__x,__y):
    return min(x,_x) >= __x and (y+_y) >= __y

data = [int(x) for x in input().split(' ')]

for i in range(0,5,2):
    if data[i] > data[i+1]:
        swap(i,i+1)

pi = [(0,1,2,3),(0,1,3,2),(1,0,2,3),(1,0,3,2)]
answer = False

for p in pi:
    answer |= check(data[p[0]],data[p[1]],data[p[2]],data[p[3]],data[4],data[5])

answer |= (data[0] >= data[4]) and (data[1] >= data[5])
answer |= (data[2] >= data[4]) and (data[3] >= data[5])

print('S' if answer else 'N')
