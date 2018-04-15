dx = [0,1,0,-1]
dy = [1,0,-1,0]

rc = [int(x) for x in input().split(' ')]
xy = [int(x) - 1 for x in input().split(' ')]

mapping = []
for i in range(rc[0]):
    mapping.append([])
    mapping[i] = [int(x) for x in input().split(' ')]

q = [[xy[0],xy[1]]]

while len(q) > 0:
    
    x = q[0][0]
    y = q[0][1]
    q.pop(0)

    mapping[x][y] = 0

    for i in range(4):
        x += dx[i]
        y += dy[i]

        if 0 <= x and 0 <= y and x < rc[0] and y < rc[1] and mapping[x][y] == 1:
            q.append([x,y])

        y -= dy[i]
        x -= dx[i]
    
print('{0} {1}'.format(x+1,y+1))