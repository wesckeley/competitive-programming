n = int(input())
data = []
for i in range(n):
    data.append([])
    data[i] = [int(x) for x in input().split(' ')]

row_sum = [0 for i in range(n)]
col_sum = [0 for i in range(n)]

for i in range(n):
    for j in range(n):
        row_sum[i] += data[i][j]
        col_sum[j] += data[i][j]

row_dict = dict()
col_dict = dict()

for i in range(n):
    
    try:
        row_dict[row_sum[i]].append(i)
    except KeyError:
        row_dict[row_sum[i]] = [i]

    try:
        col_dict[col_sum[i]].append(i)
    except KeyError:
        col_dict[col_sum[i]] = [i]

for x in row_dict:
    if len(row_dict[x]) == 1:
        row = row_dict[x][0]
        sum_wrong = x
    else:
        sum_right = x

for x in col_dict:
    if len(col_dict[x]) == 1:
        col = col_dict[x][0]


print("{0} {1}".format(data[row][col]+sum_right-sum_wrong,data[row][col]))