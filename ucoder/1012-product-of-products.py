tests = int(input())

for t in range(tests):
    line = input().split(' ')
    p = int(line[0])
    m = int(line[1])

    quantity = []
    for i in range(m):
        quantity.append([])
        quantity[len(quantity) - 1] = [int(x) for x in input().split(' ')]

    values = []
    for i in range(p):
        values.append([])
        values[len(values) - 1] = [int(x) for x in input().split(' ')]

    total = []
    for i in range(m):
        total.append([])
        for j in range(2):
            total[i].append(0)
            for k in range(p):
                total[i][j] += quantity[i][k] * values[k][j]

    print("Case {0}:".format(t+1))
    for i in range(m):
        print("{0} {1}".format(total[i][0],total[i][1]))