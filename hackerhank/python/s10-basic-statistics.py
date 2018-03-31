import pandas

n = int(input())

data = pandas.Series((int(x) for x in input().split(' ')))

print(data.mean())
print(data.median())
print(data.mode()[0])