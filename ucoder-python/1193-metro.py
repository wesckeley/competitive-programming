n, m = map(int, input().split())

graph = [[] for i in range(n)]

for i in range(m):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)

center_station = 0
for i in range(n):
    if len(graph[i]) >= 5:
        center_station = i
        break

parent = [-1 for i in range(n)]
distance = [-1 for i in range(n)]
idx = [0 for i in range(n)]

parent[center_station] = center_station
distance[center_station] = 0

q = [center_station]
flag = False

while len(q) > 0 and not flag:

    u = q[-1]

    black = True
    for i in range(idx[u], len(graph[u])):
        v = graph[u][i]
        if distance[v] == -1:
            parent[v] = u
            distance[v] = distance[u] + 1
            q.append(v)
            black = False
            idx[u] = i + 1
            break
        elif v == center_station:
            continue
        elif v == parent[u]:
            continue
        else:
            answer = abs(distance[u] - distance[v]) + 1
            flag = True
            break

    if black:
        q.pop(-1)

print(answer)
