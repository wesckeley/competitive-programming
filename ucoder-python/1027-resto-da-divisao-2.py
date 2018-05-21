a, b = map(int, input().split())
print(a % b if a % b > b % a else b % a)
