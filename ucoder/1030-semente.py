first_line = input().split(' ')
length = int(first_line[0])
count = int(first_line[1])

positions = [int(x) for x in input().split(' ')]

max_distance = 0
for i in range(1,count):
    max_distance = max(max_distance, positions[i] - positions[i-1])
max_distance //= 2

max_distance = max(max_distance,positions[0] - 1)
max_distance = max(max_distance,length - positions[len(positions)-1])

print(max_distance)


