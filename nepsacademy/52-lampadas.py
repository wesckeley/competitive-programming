count = [0,0]

n = int(input())
data = [int(x) - 1 for x in input().split( ' ')]

for x in data:    
    count[x] += 1

count[0] += count[1]

print(count[0] & 1)
print(count[1] & 1)

