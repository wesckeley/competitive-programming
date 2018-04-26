# Canadian Computing Competition 2017
# Junior
# https://cemc.math.uwaterloo.ca/contests/computing/2017/index.html
# https://open.kattis.com/problems/exactlyeletrical

ab = [int(x) for x in input().split(' ')]
cd = [int(x) for x in input().split(' ')]
t = int(input())

m_dist = abs(ab[0] - cd[0]) + abs(ab[1] - cd[1])

print("Y" if m_dist <= t and m_dist % 2 == t % 2 else 'N')
