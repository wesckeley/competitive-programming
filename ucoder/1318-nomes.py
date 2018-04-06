def get_prefix_size(parent,son):
    max_length = min(len(parent),len(son))
    i = 0
    while i < max_length and parent[i] == son[i]:
        i += 1
    return i

parent = input()
n = int(input())

for i in range(n):
    print("NORMAL" if get_prefix_size(parent,input()) <= 3 else "VERIFICAR")