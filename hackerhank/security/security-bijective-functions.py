n = int(input())

counting = [0 for x in range(0,n+1)]

for x in input().split():
    counting[int(x)] += 1

is_bijective = True
for i in range(1,n+1):
    is_bijective &= (counting[i] == 1)

print("YES" if is_bijective == True else "NO")