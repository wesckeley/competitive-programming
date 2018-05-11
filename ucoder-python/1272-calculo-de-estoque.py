n = int(input())

total_global = 0
for i in range(n):
    p = int(input())
    total_local = 0
    for j in range(p):
        values = [int(x) for x in input().split(' ')]
        total_local += values[0] * values[1]
    total_global += total_local
    print(total_local)
print(total_global)
