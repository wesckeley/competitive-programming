n = int(input())

data = []
for i in range(n):
    line = input().split(' ')
    data.append([-float(line[1]),int(line[2]),line[0]])
data.sort()

grade = data[0][0]
absence = data[0][1]

i = 0
while data[i][0] == grade and data[i][1] == absence:
    print(data[i][2])
    i += 1