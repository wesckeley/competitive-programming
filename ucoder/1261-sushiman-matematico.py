def is_prime(number):
    i = 2
    while (i * i) <= number:
        if number % i == 0:
            return False
        i += 1
    return True

super_primes = [[],[2,3,5,7],[],[],[],[],[],[],[]]

n = int(input())

for i in range(2,n+1):
    for x in super_primes[i-1]:
        base = x * 10
        if is_prime(base + 1): super_primes[i].append(base + 1)
        if is_prime(base + 3): super_primes[i].append(base + 3)
        if is_prime(base + 7): super_primes[i].append(base + 7)
        if is_prime(base + 9): super_primes[i].append(base + 9)

for x in super_primes[n]:
    print(x)