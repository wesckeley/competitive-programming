# Canadian Computing Competition 2017
# Junior
# https://cemc.math.uwaterloo.ca/contests/computing/2017/index.html
# https://open.kattis.com/problems/quadrant

dict_answer = {(1,1): 1, (-1,1): 2, (-1,-1): 3, (1,-1): 4}

x = int(input())
y = int(input())

x /= abs(x)
y /= abs(y)

print(dict_answer[(x,y)])
