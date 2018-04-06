n = int(input())
pi = [int(x) - 1 for x in input().split(' ')]

is_involution = True
for i in range(0,n):
    is_involution &= (pi[pi[i]] == i)

print("YES" if is_involution else "NO")