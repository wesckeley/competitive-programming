class Team:
    def __init__(self,time,team_id):
        self.time = time
        self.team_id = team_id

    def __repr__(self):
        return str(self.team_id)

    def __lt__(self,other):
        return self.time < other.time

podium =[]

for i in range(3):
    podium.append(Team(int(input()),i+1))

podium.sort()

for i in range(3):
    print(podium[i])