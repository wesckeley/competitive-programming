n = int(input())

for i in range(n):
    p = int(input())

    total = 0
    for j in range(p):
        line = input().split(' ')
        q = int(line[0])
        v = int(line[1])
        total += (q * v)

    d = int(input())
    print(d - total if d >= total else "DINHEIRO INSUFICIENTE")