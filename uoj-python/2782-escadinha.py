n = int(input())
data = [int(x) for x in input().split()]

if len(data) == 1:
    print('1')
else:
    diff_data = [data[i] - data[i - 1] for i in range(1, len(data))]
    answer = 1
    for i in range(1, len(diff_data)):
        if diff_data[i] != diff_data[i - 1]:
            answer += 1
    print(answer)
