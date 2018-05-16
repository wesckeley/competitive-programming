data = input().split()
data_dict = dict()
answer = True

for x in data:
    try:
        data_dict[x] += 1
    except KeyError:
        data_dict[x] = 1
    answer &= data_dict[x] <= 1

print('yes' if answer else 'no')
