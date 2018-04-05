box =[0,0,0]
window = [0,0]

for i in range(0,3):
    box[i] = int(input())
for i in range(0,2):
    window[i] = int(input())

box.sort()
window.sort()

print("S" if(box[0]<=window[0]) and (box[1]<=window[1]) else "N")