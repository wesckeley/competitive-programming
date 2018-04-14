class Team:

    def __init__(self,fatec_id,team_id,solved_problems,total_time):
        self.fatec_id = fatec_id
        self.team_id = team_id
        self.solved_problems = solved_problems
        self.total_time = total_time

    def __repr__(self):
        return str(self.team_id)

    def __lt__(self,other):
        if self.solved_problems != other.solved_problems:
            return self.solved_problems > other.solved_problems
        else:
            return self.total_time < other.total_time

first_line = input().split(' ')
available = int(first_line[0])
fatecs_count = int(first_line[1])
teams_count = int(first_line[2])

fatec_flag = dict()
team_flag = [False for i in range(teams_count)]
team_list = []
for i in range(teams_count):
    line = input().split(' ')
    team_list.append(Team(int(line[0]),int(line[1]),int(line[2]),int(line[3])))
    fatec_flag[int(line[0])] = False

team_list.sort()

for i in range(teams_count):
    if fatec_flag[team_list[i].fatec_id] == False:
        fatec_flag[team_list[i].fatec_id] = True
        team_flag[i] = True

i = 0
while fatecs_count < available and i < teams_count:
    if team_flag[i] == False:
        team_flag[i] = True
        fatecs_count += 1
    i += 1
    
answer = [team_list[i].team_id for i in range(teams_count) if team_flag[i] == True]
answer.sort()

for i in range(len(answer) - 1):
    print("{0},".format(answer[i]), end = ' ')
print("{0}.".format(answer[len(answer) - 1]), end = '\n')