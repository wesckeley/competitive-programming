
def bfs(g,n):

    visited = [False for i in range(n)]
    visited_count = 0

    visited[0] = True
    q = [0]

    while len(q) > 0:
        
        u = q[0]
        q.pop(0)

        visited_count += 1

        for v in g[u]:
            if visited[v] == False:
                visited[v] = True
                q.append(v)

    return visited_count

n = int(input())

graph = [[] for i in range(n)]
r_graph = [[] for i in range(n)]

for i in range(n):
    ft = [int(x) - 1 for x in input().split(' ')]
    graph[ft[0]].append(ft[1])
    r_graph[ft[1]].append(ft[0])

print('S' if bfs(graph,n) == n and bfs(r_graph,n) == n else 'N')