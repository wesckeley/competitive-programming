n = int(input())
data = [int(x) for x in input().split(' ')]

ans_local = 1
ans_global = 1
idx = 0

for i in range(1,len(data)):
    if data[i] == data[idx]:
        ans_local += 1
    else:
        ans_global = max(ans_global,ans_local)
        ans_local = 1
        idx = i

print(max(ans_global,ans_local))