tests_count = int(input())
for i in range(tests_count):
    n = int(input())
    zeros = n*n - 3*n + 2
    n *= n
    n -= zeros
    print("S {0}".format(zeros) if zeros > n else "N {0}".format(zeros))