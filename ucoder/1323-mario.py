# TLE no último caso de teste
# Versão em C++ passou

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(row_count,col_count):
    global mapping

    distance = []
    visited = []
    for i in range(row_count):
        distance.append([])
        visited.append([])
        distance[i] = [-1 for j in range(col_count)]
        visited[i] = [False for j in range(col_count)]

    for i in range(row_count):
        for j in range(col_count):
            if mapping[i][j] == 'S':
                x = i
                y = j

    visited[x][y] = True
    distance[x][y] = 0
    q = [[x,y]]

    while len(q) > 0:
        x = q[0][0]
        y = q[0][1]        
        q.pop(0)

        for k in range(4):
            to_x = x + dx[k]
            to_y = y + dy[k]
            if 0 <= to_x and 0 <= to_y and to_x < row_count and to_y < col_count:
                if mapping[to_x][to_y] != 'x' and visited[to_x][to_y] == False:
                    if mapping[to_x][to_y] == 'T':
                        return distance[x][y] + 1
                    visited[to_x][to_y] = True
                    distance[to_x][to_y] = distance[x][y] + 1
                    q.append([to_x,to_y])
    
    return -1

first_line = input().split(' ')
row_count = int(first_line[0])
col_count = int(first_line[1])

mapping = []
for i in range(row_count):
    mapping.append([])
    mapping[i] = input()

life_count = int(input())

distance = bfs(row_count,col_count)

if distance != -1:
    life_needed = distance  // 4
    if distance % 4 != 0: life_needed += 1
    print("SIM" if life_needed <= life_count else "NAO")
else:
    print("NAO")