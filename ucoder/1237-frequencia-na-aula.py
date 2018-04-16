# TLE
# The input data is huge enough to cause TLE in Python on this online judge
# A "C" version with a getchar_unlocked() was used in order to get ACC

n = int(input())
students = set()

for i in range(n):        
    x = int(input())
    students.add(x)

print(len(students))