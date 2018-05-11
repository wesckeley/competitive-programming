class Person:

    def __init__(self, name, timing):
        self.name = name
        self.time = max(timing)

    def __repr__(self):
        return self.name + ' {0}m{1}c'.format(self.time // 100, self.time % 100)

    def __lt__(self, other):
        return self.time > other.time


data = []

for i in range(3):
    name = input()
    data_in = input()

    data_out = ''
    for x in data_in:
        if x != 'm' and x != 'c':
            data_out += x
        elif x == 'm':
            data_out += ' '

    data_out = [int(x) for x in data_out.split(' ')]

    timing = []
    for i in range(0, 6, 2):
        timing.append((data_out[i] * 100) + data_out[i + 1])

    data.append(Person(name, timing))

data.sort()

for i in range(3):
    print(data[i])
