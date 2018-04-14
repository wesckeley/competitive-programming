p = int(input())
words = dict()

for i in range(p):
    line = input()
    line = '.' + line + '.'
    line = line.split(' ')
    words_temp = dict()
    for x in line:    
        words_temp[str.upper(x)] = 1
    keys = words_temp.keys()
    for x in keys:
        try:
            words[x] += 1
        except KeyError:
            words[x] = 1

n = int(input())

for i in range(n):
    language = input()
    try:
        print("{0} {1}".format(language,words[str.upper(language)]))
    except KeyError:
        print("{0} 0".format(language))