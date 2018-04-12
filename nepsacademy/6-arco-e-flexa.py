# TLE

class Point():
    def __init__(self,x,y,i):
        self.distance = (x*x)+(y*y)
        self.i = i

    def __repr__(self):
        return str(i)

    def __lt__(self,other):
        if self.distance != other.distance:
            return self.distance < other.distance
        else:
            return self.i < other.i

    def __eq__(self,other):
        return self.distance == other.distance

def ft_update(i,n):
    global ft_data
    while i <= n:
        ft_data[i] += 1
        i += i & (-i)

def ft_query(i,n):
    global ft_data
    answer = 0
    while i > 0:
        answer += ft_data[i]
        i -= i & (-i)
    return answer

n = int(input())
points = [Point(0,0,0) for i in range(n)]
for i in range(n):
    x = [int(x) for x in input().split(' ')]
    points[i].distance = x[0]*x[0] + x[1]*x[1]
    points[i].i = i
points.sort()

data = [0 for i in range(n)]

relative_distance = 1
data[points[0].i] = relative_distance
for i in range(1,n):
    if points[i] != points[i-1]:
        relative_distance += 1
    data[points[i].i] = relative_distance

ft_data = [0 for i in range(n+1)]
total = 0
for i in range(n):
    total += ft_query(data[i], n)
    ft_update(data[i],n)
print(total)