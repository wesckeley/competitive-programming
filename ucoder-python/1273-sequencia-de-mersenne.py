mersenne = [0]
two = 2

for i in range(1, 29):
    mersenne.append(mersenne[i-1] + two - 1)
    two *= 2

while(True):
    n = int(input())
    if n == -1:
        break
    else:
        print(mersenne[n])
