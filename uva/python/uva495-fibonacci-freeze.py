fib = [0,1]

for i in range(2,5001):
    fib.append(fib[i-1] + fib[i-2])

while True:
    try:
        i = int(input())
        print(fib[i])
    except EOFError:
        break
        
