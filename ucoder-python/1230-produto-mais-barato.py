answer = 0
value = 101.00

for i in range(1, 4):
    x = float(input())
    if x <= value:
        answer = i
        value = x

print(answer)
