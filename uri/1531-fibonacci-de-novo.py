#
matrix_q = [1,1,1,0]
matrix_id = [1,0,0,1]

#
primes_check = []
primes_list = []
primes_pisano = []
primes_upper_bound = 2165

#
def matrix_mult_mod(a,b,mod):
    x = [0,0,0,0]
    x[0] = (a[0]*b[0] + a[1]*b[2]) % mod
    x[1] = (a[0]*b[1] + a[1]*b[3]) % mod
    x[2] = (a[2]*b[0] + a[3]*b[2]) % mod
    x[3] = (a[2]*b[1] + a[3]*b[3]) % mod
    return x    
#
def matrix_exp_mod(base,exponent,mod):
    result = matrix_id
    while exponent > 0:
        if (exponent % 2) == 1:
            result = matrix_mult_mod(result,base,mod)
        exponent = exponent // 2
        base = matrix_mult_mod(base,base,mod)
    return result

#
def matrix_compare(a,b):
    answer = True
    for i in range(4):
        answer &= (a[i] == b[i])
    return answer

#
def get_divisors(number):
    divisors = []    
    i = 2    
    while (i*i) < number:
        if number % i == 0:
            divisors.append(i)
        i += 1
    if (i*i) == number:
        divisors.append(i)
        i = len(divisors) - 2
    else:
        i = len(divisors) - 1
    while i >= 0:
        divisors.append(number // divisors[i])
        i -= 1
    divisors.append(number)
    return divisors
    
#
def get_pisano_prime(prime_number):
    mod = prime_number % 10
    if (mod == 1) or (mod == 9):
        divisors = get_divisors(prime_number-1)
        for x in divisors:
            if (((x % 2) == 0) and (matrix_compare(matrix_exp_mod(matrix_q,x,prime_number),matrix_id) == True)):
                return x
    else:
        divisors = get_divisors((prime_number+1)*2)
        for x in divisors:
            if (((prime_number+1)%x) != 0) and matrix_compare(matrix_exp_mod(matrix_q,x,prime_number),matrix_id) == True:
                return x

#
def set_primes(limit):
    global primes_check, primes_pisano, primes_list
    
    primes_check = [True for i in range(limit + 1)]
    primes_pisano = [0 for i in range(limit + 1)]

    primes_check[0] = False
    primes_check[1] = False

    i = 2
    while(i<=limit):
        if(primes_check[i] == True):
            j = i*i
            while(j<=limit):
                primes_check[j] = False
                j += i
        i += 1

    primes_list = [2,3,5]
    primes_pisano[2] = 3
    primes_pisano[3] = 8
    primes_pisano[5] = 20
 
    for i in range(7,limit+1):
        if primes_check[i] == True:
            primes_list.append(i)
            primes_pisano[i] = get_pisano_prime(i)

def gcd(a,b):
    while( b > 0):
        t = a
        a = b
        b = t % b
    return a

def lcm(a,b):
    return (a * b) // gcd(a,b)             

#
def get_pisano(number):
    last_factor = 0
    i = 0
    j = -1
    factor = []
    power = []

    while((number > 1) and (i < len(primes_list))):
        if (number % primes_list[i]) == 0:
            if last_factor == primes_list[i]:
                power[j] *= primes_list[i]
            else:
                j += 1
                factor.append(primes_list[i])
                power.append(1)
                last_factor = primes_list[i]
            number //= primes_list[i]
        else:
            i += 1

    for i in range(0,len(factor)):
        factor[i] = primes_pisano[factor[i]] * power[i]

    if number > 1:
        factor.append(get_pisano_prime(number))

    answer = factor[0]
    for i in range(1,len(factor)):
        answer = lcm(answer,factor[i])

    return answer            

#
set_primes(primes_upper_bound)
while(True):
    try:
        line = input().split(' ')
        n = int(line[0])
        m = int(line[1])        
    except:
        break
    p1 = get_pisano(m)
    p2 = get_pisano(p1)
    n %= p2
    n = matrix_exp_mod(matrix_q,n,p1)[1]
    n = matrix_exp_mod(matrix_q,n,m)[1]
    print(n)