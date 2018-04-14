import heapq

f = {'A': 0, 'C': 1, 'S': 2}
g = ['H','M']

e_des = [[0,1,1],[0,1,1,1],[0,0,1]]
e_mod = [3,4,3]
e_time = [[3,10],[5,15],[1,5]]

tests_i = 0

while(True):
    tests_i += 1
    
    first_line = input().split(' ')
    
    b_count = int(first_line[0])
    if(b_count == 0):
        break

    b_list = [(0,i) for i in range(1,b_count+1)]
    e_type = f[first_line[1]]

    heapq.heapify(b_list)

    n = int(input())
    answer = [(0,0) for i in range(1000)]

    for i in range(1000):
        answer[i] = heapq.heappop(b_list)
        heapq.heappush(b_list, (e_time[e_type][e_des[e_type][i % e_mod[e_type]]] + answer[i][0],answer[i][1]))

    query = [int(x)-1 for x in input().split(' ')]

    print("Consulta {0}:".format(tests_i))
    for x in query:        
        print("{0} {1} {2}".format(answer[x][0],answer[x][1],g[e_des[e_type][x % e_mod[e_type]]]))