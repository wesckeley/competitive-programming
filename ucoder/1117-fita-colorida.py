n = int(input())
data = [int(x) for x in input().split(' ')]

right = [-1 for i in range(n)]
left = [-1 for i in range(n)]

i = 0
while data[i] != 0:
    i += 1

j = i
while i < n:
    if data[i] == 0:
        j = i
    right[i] = j
    i += 1

i = j
while i >= 0:
    if data[i] == 0:
        j = i
    left[i] = j
    i -= 1

answer = [0 for i in range(n)]
for i in range(n):
    if right[i] == -1:
        answer[i] = left[i] - i
    elif left[i] == -1:
        answer[i] = i - right[i]
    else:
        answer[i] = min(left[i] - i,i - right[i])

for i in range(n-1):
    print(min(answer[i],9), end = ' ')
print(min(answer[n-1],9))