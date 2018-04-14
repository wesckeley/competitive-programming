def check(symbol,word):
    for i in range(len(word)):
        if symbol == word[i]:
            return True
    return False

symbol = input()
words = [x for x in input().split(' ')]

counting = 0
total = 0

for x in words:
    if check(symbol,x):
        counting += 1
    total += 1

print("{0:0.1f}".format(100 * counting / total))