import re

x = input()
y = input()
z = input()
n = int(input())

matches = set()
for i in range(0,len(x)-n+1):
    pattern = re.compile(x[i:i+n])
    if pattern.search(y) and pattern.search(z):
        matches.add(pattern)
print(len(matches))