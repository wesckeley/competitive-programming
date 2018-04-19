t = int(input())

for i in range(t):
    n = int(input())

    drinking_dict = dict()
    for j in range(n):
        data = [x for x in input().split(' ')]
        try:
            drinking_dict[data[0]] += int(data[1])
        except KeyError:
            drinking_dict[data[0]] = int(data[1])

    drinking_list = [(x,drinking_dict[x]) for x in drinking_dict]
    drinking_list.sort()

    for (x,y) in drinking_list:
        print("{0} {1}".format(x,y))
    print("")
