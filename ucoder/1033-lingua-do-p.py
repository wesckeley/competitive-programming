data_in = input().split(' ')
data_out = ''

for i in range(len(data_in)):
    for j in range(1,len(data_in[i]),2):
        data_out += data_in[i][j]
    if i < len(data_in) - 1:
        data_out += ' '

print(data_out)