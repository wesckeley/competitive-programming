abc = [int(x) for x in input().split(' ')]
hl = [int(x) for x in input().split(' ')]

abc.sort()
hl.sort()

print('S' if abc[0] <= hl[0] and abc[1] <= hl[1] else 'N')