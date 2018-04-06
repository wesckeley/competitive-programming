line = input()

answer = ""
for i in range(0,len(line)):
    answer += chr(((int(line[i]) + 1) % 10) + ord('0'))

print(answer)   