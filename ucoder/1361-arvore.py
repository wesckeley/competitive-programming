def post_order(depth,counter):
    global list_depth

    if depth == 0:
        return counter

    counter = post_order(depth-1,counter)
    counter = post_order(depth-1,counter)
    list_depth[counter] = depth - 1
    counter += 1

    return counter

list_depth = [0 for i in range(131071)]
post_order(17,0)

t = int(input())

for i in range(t):
    n = int(input())
    print(list_depth[n])
