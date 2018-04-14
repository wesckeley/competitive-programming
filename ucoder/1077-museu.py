f = {'0': False, '1': True}
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def flood_fill(i,j,row_count,col_count):
    global mapping

    q = [[i,j]]
    mapping[i][j] = False

    while len(q) > 0:
        i = q[0][0]
        j = q[0][1]
        q.pop(0)

        for k in range(4):
            i += dx[k]
            j += dy[k]

            if 0 <= i and 0 <= j and i < row_count and j < col_count:
                if mapping[i][j] == True:
                    mapping[i][j] = False
                    q.append([i,j])

            j -= dy[k]
            i -= dx[k]

    return 0

while(True):
    try:
        line = input().split(' ')
    except EOFError:
        break
    
    col_count = int(line[0])
    row_count = int(line[1])

    mapping = []
    for i in range(row_count):
        mapping.append([])
        mapping[i] = [f[x] for x in input().split(' ')]

    answer = 0
    for i in range(row_count):
        for j in range(col_count):
            if mapping[i][j] == True:
                answer += 1
                flood_fill(i,j,row_count,col_count)

    print(answer)