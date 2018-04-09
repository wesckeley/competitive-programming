'''
6 10
0 0 0 0 0 D
0 0 0 0 0 0
0 A 0 A 0 0
0 0 B 0 D 0
0 E B 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
D 0 0 0 0 A
0 C 0 A 0 0
25 2
D 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 A 0
0 0 0 A 0 B 0 B 0 0 0 0 0 0 0 0 A E 0 E 0 0 0 0 0
'''

f = {'0': 0, 'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}
is_valid = [
    [True,True,True,True,True,True],
    [True,True,False,True,False,True],
    [True,False,True,False,True,True],
    [True,True,False,True,True,True],
    [True,False,True,True,True,True],
    [True,True,True,True,True,True]]
dx = [1,0,-1,0]
dy = [0,1,0,-1]

while(True):
    line = input().split(' ')
    col_count = int(line[0])
    row_count = int(line[1])

    if row_count == 0 and col_count == 0:
        break

    mapping = []    
    for i in range(row_count):
        mapping.append([])
        line = input().split(' ')        
        mapping[i] = [f[x] for x in line]    
        #for j in range(0,len(line),2):            
        #    mapping[i].append(f[line[j]])

    i = 0
    j = 0
    answer = True
    while i < row_count and answer == True:
        j = 0
        while j < col_count and answer == True:
            #melhorar
            if 1 <= mapping[i][j] and mapping[i][j] <= 4:
                for k in range(4):
                    _i = i + dx[k]
                    _j = j + dy[k]
                    if 0 <= _i and 0 <= _j and _i < row_count and _j < col_count:
                        answer &= is_valid[mapping[i][j]][mapping[_i][_j]]
            j += 1
        i += 1

    print("V" if answer == True else "F")