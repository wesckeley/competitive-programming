first_line = input().split(' ')
n = int(first_line[0])
m = int(first_line[1])
data = [int(x) for x in input().split(' ')]


data[0] = min(data[0],m - data[0])
total = data[0]

for i in range(1,n):
    min_value = min(data[i],m - data[i])
    max_value = max(data[i],m - data[i])
    
    if min_value >= data[i-1]:
        data[i] = min_value
    elif max_value >= data[i-1]:
        data[i] = max_value
    else:
        total = -1
        break

    total += data[i]

print(total)