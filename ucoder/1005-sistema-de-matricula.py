class person(object):

    def __init__(self,name,is_close,income,welfare,brother,mother):
        self.name = name
        self.is_close = is_close
        self.income = income
        self.welfare = welfare
        self.brother = brother
        self.mother = mother

    def __repr__(self):
        return self.name

    def __lt__(self,other):
        if self.is_close != other.is_close:
            return self.is_close == True
        elif self.income != other.income:
            return self.income < other.income
        elif self.welfare != other.welfare:
            return self.welfare == True
        elif self.brother != other.brother:
            return self.brother == True
        elif self.mother != other.mother:
            return self.mother == True
        else:
            return self.name < other.name

    def __eq__(self,other):
        return self.is_close == other.is_close and self.income == other.income and self.welfare == other.welfare and\
        self.brother == other.brother and self.mother == other.mother


f = {'S': True, 'N': False}
data = []
i = 0

while(True):
    try:
        line = input().split(';')
    except EOFError:
        break
    data.append(person(line[0],f[line[1]],int(line[2]),f[line[3]],f[line[4]],f[line[5]]))

data.sort()

i = 1
print("{0} {1}".format(i, data[0]))

for j in range(1,len(data)):
    if data[j] != data[j-1]:
        i += 1
    print("{0} {1}".format(i, data[j]))