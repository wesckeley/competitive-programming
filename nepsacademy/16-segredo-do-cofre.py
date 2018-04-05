
ft_data = []

#
def ft_update_point(i,n,value):
    global ft_data
    while i <= n:
        ft_data[i] += value
        i += (i & (-i))

#
def ft_update_range(i,j,n):
    ft_update_point(i,n,1)
    ft_update_point(j+1,n,-1)

#
def ft_query_point(i,n):
    global ft_data
    answer = 0 
    while i > 0:    
        answer += ft_data[i]
        i -= (i & (-i))
    return answer

first_line = input().split(' ')
data = [int(x) for x in input().split(' ')]
pos = [int(x) for x in input().split(' ')]

ft_data = [0 for x in range(0,len(data)+1)]

for i in range(1,len(pos)):
    if(pos[i-1] < pos[i]):
        ft_update_range(pos[i-1] + 1,pos[i],len(data))
    else:
        ft_update_range(pos[i],pos[i-1]-1,len(data))

counting = [0 for x in range(0,10)]
counting[data[pos[0] - 1]] = 1

for i in range(1,len(data)+1):
    counting[data[i-1]] += ft_query_point(i,len(data))

for i in range(0,9):
    print(counting[i], end = ' ')
print(counting[9], end = '\n')