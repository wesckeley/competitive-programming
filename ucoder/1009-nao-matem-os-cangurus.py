while(True):
    try:
        test = int(input())
    except:
        break
    
    matrix = [[],[],[],[]]
    matrix[0] = [int(x) for x in input().split(' ')]
    matrix[1] = [int(x) for x in input().split(' ')]
    matrix[2] = [int(x) for x in input().split(' ')]
    matrix[3] = [int(x) for x in input().split(' ')]

    row_sum = [0,0,0,0]
    col_sum = [0,0,0,0]
    for i in range(4):
        for j in range(4):
            row_sum[i] += matrix[i][j]
            col_sum[j] += matrix[i][j]

    row_from = -1
    col_from = -1
    row_to = -1
    col_to = -1

    for i in range(4):
        if row_sum[i] == 1: row_to = i
        if row_sum[i] == 3: row_from = i
        if col_sum[i] == 1: col_to = i
        if col_sum[i] == 3: col_from = i

    if row_to == -1:
        print("Caso {0}: CORRETO".format(test))
    else:
        print("Caso {0}: MOVER CANGURU DE ({1},{2}) PARA ({3},{4})".format(test,row_from+1,col_from+1,row_to+1,col_to+1))