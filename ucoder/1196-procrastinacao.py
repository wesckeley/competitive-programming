from datetime import date, timedelta

line = input().split(' ')
line = line[1].split('/')

d = date(int(line[2]),int(line[1]),int(line[0]))
d -= timedelta(days = 1)

print("{0:02d}/{1:02d}/{2:02d}".format(d.day,d.month,d.year))