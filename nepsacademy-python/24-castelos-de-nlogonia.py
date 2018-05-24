def bfs(u, v, c):
    global graph, color
    parent = [-1 for i in range(len(graph))]

    q = [u]
    parent[u] = u

    while len(q) > 0:
        u = q[0]
        q.pop(0)

        if u == v:
            break

        for w in graph[u]:
            if parent[w] == -1:
                q.append(w)
                parent[w] = u

    while parent[v] != v:
        color[v] = c
        v = parent[v]
    color[v] = c


n, m = map(int, input().split())

graph = [[] for i in range(n)]
color = [0 for i in range(n)]
for i in range(n - 1):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)

for i in range(m):
    p, q, c = map(int, input().split())
    bfs(p - 1, q - 1, c)

print(' '.join(str(color[x]) for x in range(len(color))))
