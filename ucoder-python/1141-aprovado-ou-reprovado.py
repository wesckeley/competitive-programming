a, b = map(int, input().split())
m = (a + b) / 2

if m < 7.0:
    print("REPROVADO")
elif m < 10.0:
    print("APROVADO")
else:
    print("APROVADO COM DISTINCAO")
