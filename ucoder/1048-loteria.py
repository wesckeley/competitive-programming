answer = ['azar','azar','azar','terno','quadra','quina','sena']

data_dict = dict()

data = [int(x) for x in input().split(' ')]
for x in data:
    data_dict[x] = 1

data = [int(x) for x in input().split(' ')]
idx = 6
for x in data:
    try:
        data_dict[x] += 1
    except KeyError:
        idx -= 1

print(answer[idx])