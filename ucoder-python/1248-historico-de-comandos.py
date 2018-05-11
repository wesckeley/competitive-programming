while(True):
    n = int(input())
    if n == 0:
        break
    data = [int(x) for x in input().split(' ')]

    last_seen = dict()
    acc = 0
    global_ans = 0

    for x in data:
        try:
            local_ans = acc - last_seen[x] + 1
        except KeyError:
            local_ans = x + acc

        global_ans += local_ans
        acc += 1
        last_seen[x] = acc

    print(global_ans)
