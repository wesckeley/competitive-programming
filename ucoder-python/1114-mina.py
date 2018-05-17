import heapq

inf = 0x1FFFFFFF
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def dijkstra():
    global mapping, n

    cost = [[] for i in range(n)]
    visited = [[] for i in range(n)]
    for i in range(n):
        cost[i] = [inf for j in range(n)]
        visited[i] = [False for j in range(n)]

    cost[0][0] = mapping[0][0]
    visited[0][0] = True
    q = []
    heapq.heappush(q, (cost[0][0], 0, 0))

    while len(q) > 0:
        top = heapq.heappop(q)
        x = top[1]
        y = top[2]
        for i in range(4):
            to_x = x + dx[i]
            to_y = y + dy[i]
            if 0 <= to_x and 0 <= to_y and to_x < n and to_y < n:
                if visited[to_x][to_y] is False:
                    if cost[x][y] + mapping[to_x][to_y] < cost[to_x][to_y]:
                        cost[to_x][to_y] = cost[x][y] + mapping[to_x][to_y]
                        visited[to_x][to_y] = True
                        heapq.heappush(q, (cost[to_x][to_y], to_x, to_y))

    return cost[n-1][n-1]


n = int(input())
mapping = []
for i in range(n):
    mapping.append([])
    mapping[i] = [int(x) for x in input().split()]

print(dijkstra())
