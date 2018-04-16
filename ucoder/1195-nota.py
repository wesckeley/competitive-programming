right_ones = [x for x in input().split(' ')]
mine_ones = [x for x in input().split(' ')]

answer = 0
for i in range(len(right_ones)):
    answer += (right_ones[i] == mine_ones[i]) & 1
print(answer << 1)