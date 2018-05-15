n = int(input())
binary = []

mult = 1
while n > 0:
    binary.append(n % 2)
    n //= 2
    mult *= 2

for x in binary:
    mult //= 2
    n += mult * x

print(n)
