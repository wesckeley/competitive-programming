def ft_update(i,n):
    global ft_data
    while i <= n:
        ft_data[i] += 1
        i += i & (-i)

def ft_query(i):
    global ft_data
    answer = 0
    while i > 0:
        answer += ft_data[i]
        i -= i & (-i)
    return answer

n = int(input())
data = [int(x) for x in input().split(' ')]
ft_data = [0 for i in range(n+1)]

answer = 0
for i in range(n-1,-1,-1):
    answer += ft_query(data[i]-1)
    ft_update(data[i],n)
print(answer)