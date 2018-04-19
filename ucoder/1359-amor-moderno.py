while(True):
    line = input()
    if len(line) == 1 and line[0] == '*':
        break

    upper_case = 0
    for i in range(len(line)):
        if ord('A') <= ord(line[i]) and ord(line[i]) <= ord('Z'):
            upper_case += 1

    if upper_case == 0:
        print('oi')
    elif upper_case <= len(line) * 0.05:
        print('entendi')
    elif upper_case <= len(line) * 0.2:
        print('eu gosto dessa musica')
    else:
        print('desculpe')
