t = int(input())

for i in range(t):
    n = int(input())
    width = 0
    for j in range(n):
        line = input()
        width = max(width,len(line))
    print("{0} {1}".format(n*30 + (n-1)*2, width * 20))
