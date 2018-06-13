n, c, m = map(int, input().split())
xi = {int(x) for x in input().split()}
yi = [int(x) for x in input().split()]
zi = set()
for x in yi:
    if x in xi:
        zi.add(x)
print(c - len(zi))
