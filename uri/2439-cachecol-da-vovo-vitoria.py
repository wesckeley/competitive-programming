def matrix_mult(a,b,n,mod):

    c = []
    for i in range(n):
        c.append([])
        c[i] = [0 for j in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += (a[i][k] * b[k][j]) % mod
            c[i][j] %= mod

    return c

def modular_pow(base,exponent,modulus):

    result = []
    for i in range(len(base)):
        result.append([])
        result[i] = [0 for j in range(len(base))]
        result[i][i] = 1

    while exponent > 0:
        if exponent % 2 == 1:
            result = matrix_mult(result,base,len(base),modulus)
        exponent //= 2
        base = matrix_mult(base,base,len(base),modulus)

    return result

valid = [[x,y,z] for x in range(3) for y in range(3) for z in range(3) if x !=y and y != z]

graph = []
for i in range(len(valid)):
    graph.append([])
    graph[i] = [0 for j in range(len(valid))]

for i in range(len(valid)):
    for j in range(len(valid)):
        if valid[i][0] != valid[j][0] and valid[i][1] != valid[j][1] and valid[i][2] != valid[j][2]:
            graph[i][j] = 1

n = int(input())
result = modular_pow(graph,n-1,1000000007)

answer = 0
for i in range(len(result)):
    for j in range(len(result)):
        answer += result[i][j]
print(answer%1000000007)
