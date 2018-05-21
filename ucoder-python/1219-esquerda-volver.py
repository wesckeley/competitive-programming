data = ['N', 'O', 'S', 'L']
cmd = {'D': -1, 'E': 1}

n = int(input())
seq = input()

idx = 0
for x in seq:
    idx += cmd[x]
    if idx < 0:
        idx += 4
    else:
        idx %= 4

print(data[idx])
