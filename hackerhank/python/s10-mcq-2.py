data = [(i,j) for i in range(1,7) for j in range(1,7) if (i + j == 6) and (i != j)]

print(len(data))