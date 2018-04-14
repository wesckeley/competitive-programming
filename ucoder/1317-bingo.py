first_line = input().split(' ')
row_count = int(first_line[0])
col_count = int(first_line[1])
players = int(input())

graph = dict()

player_row_count = []
player_col_count = []
for i in range(players):
    player_row_count.append([])
    player_col_count.append([])
    player_row_count[i] = [0 for j in range(row_count)]
    player_col_count[i] = [0 for j in range(col_count)]

for k in range(players):
    for i in range(row_count):
        items = [int(x) for x in input().split(' ')]
        for j in range(col_count):
            try:
                graph[items[j]].append([k,i,j])
            except KeyError:
                graph[items[j]] = [[k,i,j]]
            if items[j] != 0:
                player_row_count[k][i] += 1
                player_col_count[k][j] += 1

balls_count = int(input())
for l in range(balls_count):
    ball = int(input())
    
    try:
        list_players = list(graph[ball])
    except KeyError:
        list_players = []

    winner = -1
    winner_count = 0

    for player in list_players:        
        player_row_count[player[0]][player[1]] -= 1
        player_col_count[player[0]][player[2]] -= 1
        if player_row_count[player[0]][player[1]] == 0 or player_col_count[player[0]][player[2]] == 0:
            winner = player[0] + 1
            winner_count += 1

    if winner_count > 0:    
        time = l + 1    
        break
    
if winner_count == 0:
    print("NADA")
elif winner_count == 1:
    print("{0} {1}".format(winner,time))
else:
    print("EMPATE")