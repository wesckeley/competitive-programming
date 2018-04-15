dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(i,j,n):
    global mapping

    answer = 0
    q = [[i,j]]
    mapping[i][j][1] = True    

    while len(q) > 0:

        answer += 1
        i = q[0][0]
        j = q[0][1]
        q.pop(0)
        
        for k in range(4):
            to_i = i + dx[k]
            to_j = j + dy[k]

            if 0 <= to_i and 0 <= to_j and to_i < n and to_j < n:
                if mapping[i][j][0] <= mapping[to_i][to_j][0] and mapping[to_i][to_j][1] == False:
                    q.append([to_i,to_j])
                    mapping[to_i][to_j][1] = True

    return answer

n = int(input())

ij = [int(x) - 1  for x in input().split(' ')]

mapping = []
for i in range(n):
    mapping.append([])
    mapping[i] = [[int(x),False] for x in input().split(' ')]

print(bfs(ij[0],ij[1],n))