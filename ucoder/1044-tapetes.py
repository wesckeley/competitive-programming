head = [int(x) for x in input().split(' ')]

head[0] -= (head[1] - 1)
head[0] *= head[0]

print(head[0]+head[1]-1)