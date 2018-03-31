import statistics

n = int(input())
value = [int(x) for x in input().split(' ')]
freq = [int(x) for x in input().split(' ')]

data = [value[i] for i in range(n) for j in range(freq[i])]
data.sort()

n = len(data)

lower = data[0:n // 2]

if (n % 2) == 0:
    upper = data[n // 2:n]
else:
    upper = data[(n // 2) + 1:n]

print("{0:.1f}".format(statistics.median(upper) - statistics.median(lower)))

