nb = [int(x) for x in input().split(' ')]

data = [int(x) for x in input().split(' ')]
data.sort()

i = 0
j = nb[0] - 1
answer = 0

while(i <= j):
    if data[i] + data[j] <= nb[1]:        
        i += 1
    j -= 1
    answer += 1

print(answer)