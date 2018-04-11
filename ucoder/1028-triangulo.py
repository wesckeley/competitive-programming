def is_triangle(a,b,c):
    return a < b + c and b < c + a and c < a + b

data = [int(x) for x in input().split(' ')]

answer = is_triangle(data[0],data[1],data[2])
answer |= is_triangle(data[0],data[1],data[3])
answer |= is_triangle(data[0],data[2],data[3])
answer |= is_triangle(data[1],data[2],data[3])

print("S" if answer else "N")