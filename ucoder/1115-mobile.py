a = int(input())
b = int(input())
c = int(input())
d = int(input())

print('S' if (a == (b + c + d)) and (d == (b + c)) and (b == c) else 'N')