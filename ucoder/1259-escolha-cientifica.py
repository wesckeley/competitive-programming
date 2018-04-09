while(True):
    n = int(input())
    if n != -1:
        print(31 % n if n < 31 else "31")
    else:
        break