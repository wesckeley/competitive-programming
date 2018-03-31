n = int(input())

x = [int(i) for i in input().split(' ')]
w = [int(i) for i in input().split(' ')]

denominator = 0.0
numerator = 0.0

for i in range(0,n):
    numerator = numerator + (x[i] * w[i])
    denominator = denominator + w[i]

print("{0:.1f}".format(numerator / denominator))

