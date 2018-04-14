head = [int(x) for x in input().split(' ')]
body = [int(x) for x in input().split(' ')]

movs = 0
for i in range(len(body)-1):
    movs += abs(head[1] - body[i])
    body[i+1] += head[1] - body[i]
print(movs)