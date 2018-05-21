data = [
    (1501.00, 5, 1.05),
    (701.00, 10, 1.10),
    (281.00, 15, 1.15),
    (0.00, 20, 1.20)]

n = float(input())

for x in data:
    if n >= x[0]:
        print('{:.2f}'.format(n))
        print('{0}%'.format(x[1]))
        print('{:.2f}'.format(n * x[1] / 100))
        print('{:.2f}'.format(n * x[2]))
        break
