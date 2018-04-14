head = [int(x) for x in input().split(' ')]

result = True
first_non_zero = -1
for i in range(head[0]):
    j = 0
    body = [int(x) for x in input().split(' ')]
    
    while j < head[1] and body[j] == 0:
        j += 1
    
    if (j < first_non_zero) or (j == first_non_zero and j != head[1]):        
        result = False
        break

    first_non_zero = j

print("S" if result == True else "N")
