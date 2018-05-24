primes = [True for i in range(101)]

for i in range(2, 11):
    if primes[i]:
        for j in range(i * i, 101, i):
            primes[j] = False

primes_list = [i for i in range(2, 101) if primes[i]]

n = int(input())

i = 0
last_prime = 0
count = []

while n > 1 and i < len(primes_list):
    if n % primes_list[i] == 0:
        if primes_list[i] == last_prime:
            count[-1] += 1
        else:
            last_prime = primes_list[i]
            count.append(1)
        n //= primes_list[i]
    else:
        i += 1

if n > 1:
    count.append(1)

counting = 1
for x in count:
    counting *= (x + 1)

print(counting)
