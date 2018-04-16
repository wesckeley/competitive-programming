# TLE
# The input data is huge enough to cause TLE in Python on this online judge
# A "C++"" version with a getchar_unlocked() was used in order to get ACC

def check_distance(x,y,_x,_y,d):
    x -= _x
    y -= _y
    x *= x
    y *= y
    d *= d
    return (x + y) <= d

def bfs(n):
    global graph
    visited = [False for i in range(n)]
    answer = 0

    q = [0]
    visited[0] = True

    while len(q) > 0:
        u = q[0]
        q.pop(0)
        answer += 1

        for v in graph[u]:
            if visited[v] == False:
                q.append(v)
                visited[v] = True

    return answer

nd = [int(x) for x in input().split(' ')]
xy = []
for i in range(nd[0]):
    xy.append([])
    xy[i] = [int(x) for x in input().split(' ')]

graph = [[] for i in range(nd[0])]
for i in range(nd[0]):
    for j in range(i+1,nd[0]):
        if check_distance(xy[i][0],xy[i][1],xy[j][0],xy[j][1],nd[1]):
            graph[i].append(j)
            graph[j].append(i)

print('S' if nd[0] == bfs(nd[0]) else 'N')