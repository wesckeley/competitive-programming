import statistics

n = int(input())
data = [int(x) for x in input().split(' ')]

print("{0:.1f}".format(statistics.pstdev(data)))