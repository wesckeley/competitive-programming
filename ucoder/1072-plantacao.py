def sim(x):
    global data
    answer = 0

    for i in data:
        x += i
        answer += x
        if x == 0:
            break

    return answer

pi = {'E': -1, 'C': 1}

nk = [int(x) for x in input().split(' ')]
data = [int(x) for x in input().split(' ')]
counting = [0 for i in range(101)]
for x in data:
    counting[x] += 1
data = [pi[x] for x in input().split(' ')]

answer = 0
for i in range(101):
    if counting[i] != 0:
        answer += sim(i) * counting[i]

print(answer)
