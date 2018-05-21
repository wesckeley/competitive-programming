n = int(input())

if n % 100 == 0:
    if n % 400 == 0:
        print('S')
    else:
        print('N')
else:
    if n % 4 == 0:
        print('S')
    else:
        print('N')
