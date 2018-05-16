n = int(input())

for i in range(n):
    a, b, c = map(int, input().split())
    is_possible = (a + b == c)
    is_possible |= (a * b == c)
    is_possible |= (a - b == c)
    is_possible |= (b - a == c)
    is_possible |= (a % b == 0) and (a // b == c)
    is_possible |= (b % a == 0) and (b // a == c)
    print('Possible' if is_possible else 'Impossible')
