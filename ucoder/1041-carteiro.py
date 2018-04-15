nm = [int(x) for x in input().split(' ')]

i = 0
data = input().split(' ')
data_dict = {int(data[i]):i for i in range(len(data))}
first = int(data[0])

data = [int(x) for x in input().split(' ')]

answer = abs(data_dict[data[0]] - data_dict[first])
for i in range(1,nm[1]):
    answer += abs(data_dict[data[i]] - data_dict[data[i-1]])

print(answer)