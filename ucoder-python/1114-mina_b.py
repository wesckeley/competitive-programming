inf = 0x1FFFFFFF
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def dijkstra():
    global mapping, n

    cost = [[] for i in range(n)]
    on_queue = [[] for i in range(n)]
    for i in range(n):
        cost[i] = [inf for j in range(n)]
        on_queue[i] = [False for j in range(n)]

    cost[0][0] = mapping[0][0]
    on_queue[0][0] = True
    q = [(0, 0)]

    while len(q) > 0:
        x = q[0][0]
        y = q[0][1]

        q.pop(0)
        on_queue[x][y] = False

        for i in range(4):
            to_x = x + dx[i]
            to_y = y + dy[i]
            if 0 <= to_x and 0 <= to_y and to_x < n and to_y < n:
                    if cost[x][y] + mapping[to_x][to_y] < cost[to_x][to_y]:
                        cost[to_x][to_y] = cost[x][y] + mapping[to_x][to_y]
                        if on_queue[to_x][to_y] is False:
                            on_queue[to_x][to_y] = True
                            q.append((to_x, to_y))

    return cost[n-1][n-1]


n = int(input())
mapping = []
for i in range(n):
    mapping.append([])
    mapping[i] = [int(x) for x in input().split()]

print(dijkstra())
