while(True):
    try:
        t = input()
    except EOFError:
        break

    data = [[int(x) for x in input().split()] for i in range(4)]

    sum_i = [[0, i + 1] for i in range(4)]
    sum_j = [[0, j + 1] for j in range(4)]

    for i in range(4):
        for j in range(4):
            sum_i[i][0] += data[i][j]
            sum_j[j][0] += data[i][j]

    min_i = min(sum_i)
    min_j = min(sum_j)
    max_i = max(sum_i)
    max_j = max(sum_j)

    if min_i[0] == max_i[0] and min_j[0] == max_j[0]:
        print('Caso {0}: CORRETO'.format(t))
    else:
        print('Caso {0}: MOVER CANGURU DE ({1},{2}) PARA ({3},{4})'.format(
            t, max_i[1], max_j[1], min_i[1], min_j[1]))
