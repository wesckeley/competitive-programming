while(True):
    try:
        line = [x for x in input().split(' ')]
        heap = []
        for i in range(0,int(line[0]) + 1):
            heap.append(int(line[i]))
    except:        
        break
    
    is_min_heap = True
    is_max_heap = True
    
    i = len(heap) - 1
    while( i > 1):        
        is_min_heap &= heap[i//2] <= heap[i]
        is_max_heap &= heap[i//2] >= heap[i]
        i -= 1

    if is_max_heap: 
        print("max")
    elif is_min_heap:
        print("min")
    else:
        print("nada")