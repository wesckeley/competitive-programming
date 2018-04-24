while(True):
    try:
        line = input()
    except EOFError:
        break

    line = line.split(' ')

    if len(line) > 1:
        str_list = line[1].split('_')
        str_answer = 'class '
        for x in str_list:
            str_answer += x.capitalize()
    else:
        str_answer = ''
        j = 0
        for i in range(len(line[0])):
            if line[0][i].isupper() == True:
                str_answer += line[0][j:i]
                str_answer += '_'
                str_answer += line[0][i].lower()
                j = i + 1

        str_answer += line[0][j:]

    print(str_answer)
