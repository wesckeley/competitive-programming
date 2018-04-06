n = int(input())
function = [int(x) for x in input().split(' ')]

inverse = [0 for x in range(0,n)]

for i in range(0,n):
    inverse[function[i]-1] = i+1

for i in range(0,n):
    print(inverse[i])