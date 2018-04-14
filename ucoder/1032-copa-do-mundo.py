def ds_find(x):
    global ds_parent, ds_rank
    if x != ds_parent[x]:
        ds_parent[x] = ds_find(ds_parent[x])
    return ds_parent[x]

def ds_link(x,y):
    global ds_parent, ds_rank
    if ds_rank[x] > ds_rank[y]:
        ds_parent[y] = x
    else:
        ds_parent[x] = y
        if ds_rank[x] == ds_rank[y]:
            ds_rank[y] += 1

def ds_union(x,y):
    ds_link(ds_find(x),ds_find(y))

head = [int(x) for x in input().split(' ')]
graph =[]

for i in range(head[1]):
    body = [int(x) for x in input().split(' ')]
    graph.append((1,body[2],body[0]-1,body[1]-1))
    graph.append((1,body[2],body[1]-1,body[0]-1))

for i in range(head[2]):
    body = [int(x) for x in input().split(' ')]
    graph.append((2,body[2],body[1]-1,body[0]-1))
    graph.append((2,body[2],body[0]-1,body[1]-1))

graph.sort()
ds_parent = [i for i in range(head[0])]
ds_rank = [0 for i in range(head[0])]

answer = 0
for x in graph:
    if ds_find(x[2]) != ds_find(x[3]):
        ds_union(x[2],x[3])
        answer += x[1]
print(answer)