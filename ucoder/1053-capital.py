import itertools

data = [int(x) for x in input().split(' ')]
answer = False

for p in list(itertools.permutations(range(4))):
    answer |= data[p[0]] * data[p[1]] == data[p[2]] * data[p[3]]

print('S' if answer else 'N')