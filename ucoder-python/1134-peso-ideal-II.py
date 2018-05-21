coef = [(62.1, -44.7), (72.7, -58.0)]

line = input().split(' ')
a = float(line[0])
s = int(line[1]) - 1
print("{:.2f}".format(coef[s][0] * a + coef[s][1]))
