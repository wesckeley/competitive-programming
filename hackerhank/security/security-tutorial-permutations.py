n = int(input())
pi = [int(x) - 1 for x in input().split(' ')]

for i in range(0,n):
    print(pi[pi[i]] + 1)