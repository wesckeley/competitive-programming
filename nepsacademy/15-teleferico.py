c = int(input()) - 1
a = int(input())

answer = a // c
if a % c != 0:
    answer += 1

print(answer)