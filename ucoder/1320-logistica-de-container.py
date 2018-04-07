
container = [[] for i in range(50)]
container_full = [8 for i in range(50)]

def find_container(size):
    global container_full
    i = 0
    while(size > container_full[i]):
        i += 1
    return i

pallet = [int(x) for x in input().split(' ')]
pallet_container_map = [-1 for i in range(len(pallet))]

for i in range(0,len(pallet)):
    j = find_container(pallet[i])
    container[j].append(i)
    container_full[j] -= pallet[i]
    pallet_container_map[i] = j

while(True):
    try:
        i = int(input())
    except:
        break
    i -= 1
    j = pallet_container_map[i]
    k = len(container[j])-1
    print( "Pallet {0} Container {1}".format(i + 1, j + 1), end = '')
    
    if container[j][k] == i:
        print(" TOPO")
    else:
        print(" Retirar", end = '')
        while(container[j][k] != i):
            print(" {0}".format(container[j][k] + 1), end = '')
            k -= 1
        print( "")