import bisect

ct = [int(x) for x in input().split(' ')]

r = [0 for x in range(ct[0])]
for i in range(ct[0]):
    r[i] = int(input())
    r[i] *= r[i]

answer = 0
for i in range(ct[1]):
    xy = [int(x) for x in input().split(' ')]
    d = (xy[0] * xy[0]) + (xy[1] * xy[1])
    answer += ct[0] - bisect.bisect_left(r,d)
print(answer)
