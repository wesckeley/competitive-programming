import statistics

n = int(input())
data = [int(x) for x in input().split(' ')]
data.sort()

lower = data[0:n // 2]

if (n % 2) == 0:
    upper = data[n // 2:n]
else:
    upper = data[(n // 2) + 1:n]

print("{0:.0f}".format(statistics.median(lower)))
print("{0:.0f}".format(statistics.median(data)))
print("{0:.0f}".format(statistics.median(upper)))