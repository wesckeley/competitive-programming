length_first = int(input())
weight_first = int(input())

length_second = int(input())
weight_second = int(input())

area_first = length_first * weight_first
area_second = length_second * weight_second

if area_first < area_second:
    print(area_second)
else:
    print(area_first)