n = int(input())
data = [int(x) for x in input().split(' ')]

max_l = data[0]
max_g = data[0]

for i in range(1,n):
    max_l = max(data[i],max_l + data[i])
    max_g = max(max_g,max_l)

print(max_g)