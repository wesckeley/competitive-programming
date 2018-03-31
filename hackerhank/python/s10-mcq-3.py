x = [1,1,1,1,0,0,0]
y = [1,1,1,1,1,0,0,0,0]
z = [1,1,1,1,0,0,0,0]

fullData = [(x[i],y[j],z[k]) for i in range(len(x)) for j in range(len(y)) for k in range(len(z))]

chosenData = [i for i in fullData if (i[0] + i[1] + i[2]) == 2]

print(len(fullData))
print(len(chosenData))
