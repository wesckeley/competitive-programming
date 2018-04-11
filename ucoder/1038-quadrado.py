n = int(input())

matrix = []
for i in range(n):
    matrix.append([])
    matrix[i] = [int(x) for x in input().split(' ')]

row_sum = [0 for x in range(n)]
col_sum = [0 for x in range(n)]

for i in range(n):
    for j in range(n):
        row_sum[i] += matrix[i][j]
        col_sum[j] += matrix[i][j]

row_dict = dict()
col_dict = dict()
for i in range(n):
    try:
        row_dict[row_sum[i]] += 1
    except KeyError:
        row_dict[row_sum[i]] = 1

    try:
        col_dict[col_sum[i]] += 1
    except KeyError:
        col_dict[col_sum[i]] = 1

row_keys = list(row_dict.keys())
col_keys = list(col_dict.keys())

if row_dict[row_keys[0]] < row_dict[row_keys[1]]:
    row_value = row_keys[0]
else:
    row_value = row_keys[1]

if col_dict[col_keys[0]] < col_dict[col_keys[1]]:
    col_value = col_keys[0]
else:
    col_value = col_keys[1]