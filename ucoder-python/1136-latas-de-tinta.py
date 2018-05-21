m = int(input())

m = (m // 3) if m % 3 == 0 else (m // 3) + 1
m = (m // 18) if m % 18 == 0 else (m // 18) + 1

print('{0} {1}'.format(m, m * 80))
