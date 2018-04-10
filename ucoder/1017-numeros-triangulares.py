numbers = [0]
for i in range(1,45001):
    numbers.append(numbers[i-1] + i)
while(True):
    n = int(input())
    if n != 0:
        print(numbers[n])
    else:
        break