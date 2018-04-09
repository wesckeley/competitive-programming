tests_count = int(input())

for i in range(tests_count):
    line = input().split(' ')
    funds = int(line[0])
    items = int(line[1])

    values = [0]
    voters = [0]
    for i in range(items):
        line = input().split(' ')
        if int(line[0]) <= funds:
            values.append(int(line[0]))
            voters.append(int(line[1]))

    items = len(values)

    dp = [[]]
    dp[0] = [0 for i in range(funds + 1)]

    for i in range(1,items):
        dp.append([])                        
        for j in range(values[i]):
            dp[i].append(dp[(i - 1)][j])
        for j in range(values[i],funds + 1):
            dp[i].append(max(dp[i - 1][j],dp[i - 1][j - values[i]] + voters[i]))

    i = items - 1
    j = funds
    k = funds

    while i > 0 and j > 0:
        if dp[i][j] != dp[i-1][j]:
            funds -= values[i]
            i -= 1
            j -= values[i]
        else:
            i -= 1

    print(dp)
    print("{0} {1}".format(dp[items - 1][len(dp[items - 1]) - 1],funds))