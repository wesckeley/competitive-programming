class Athlet:

    def __init__(self, name, speed):
        self.name = name
        self.time = 4500 / speed
        self.time = int(self.time)

    def __repr__(self):
        return self. name + ' {0}h{1}'.format(self.time // 60, self.time % 60)

    def __lt__(self, other):
        return self.time < other.time


data = []
for i in range(3):
    name = input()
    speed = int(input())
    data.append(Athlet(name, speed))

data.sort()

for i in range(3):
    print(data[i])
