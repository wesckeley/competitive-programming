data = input().split(' ')

hbv = float(data[0])
hev = float(data[1])
qh = float(data[2])
dpb = float(data[3])
dpe = float(data[4])
ct = float(data[5])

hbv *= ((100 - dpb) / 100)
hbv *= qh

hev *= ((100 - dpe) / 100)
hev *= qh

total_b = 0
total_e = 0

for i in range(3):

    hbv *= 1.01
    hev *= 1.01
    
    total_b += hbv
    total_e += hev

print("{0:0.2f}BR {1:0.2f}ES".format(total_b,total_e*ct))