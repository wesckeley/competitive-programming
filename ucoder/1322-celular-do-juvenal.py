data_lower = [1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,4,1,2,3,1,2,3,4]
data_upper = [4,5,6,4,5,6,4,5,6,4,5,6,4,5,6,5,6,7,8,4,5,6,5,6,7,8]

line = input()

answer = 0
for i in range(len(line)):
    if line[i] == ' ':
        answer += 1
    elif ord('a') <= ord(line[i]) and ord(line[i]) <= ord('z'):
        answer += data_lower[ord(line[i]) - ord('a')]
    else:
        answer += data_upper[ord(line[i]) - ord('A')]

print(answer)