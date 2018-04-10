dx = [1,0,-1,0]
dy = [0,1,0,-1]

def dfs(mapping,x,y,row_count,col_count):

    value = mapping[x][y]
    mapping[x][y] = -value
    q = [[x,y]]
    answer = 0

    while len(q) > 0:
        x = q[0][0]
        y = q[0][1]
        q.pop(0)
        answer += 1

        for i in range(4):
            x += dx[i]
            y += dy[i]

            if 0 <= x and 0 <= y and x < row_count and y < col_count:
                if mapping[x][y] == value:
                    mapping[x][y] = -value
                    q.append([x,y])

            x -= dx[i]
            y -= dy[i]

    return answer

while(True):
    line = input().split(' ')
    row_count = int(line[0])
    col_count = int(line[1])

    if row_count == 0 and col_count == 0:
        break

    mapping = []
    for i in range(row_count):
        mapping.append([])
        mapping[i] = [int(x) for x in input().split(' ')]

    line = input().split(' ')
    x = int(line[0]) - 1
    y = int(line[1]) - 1
    
    print(dfs(mapping,x,y,row_count,col_count))