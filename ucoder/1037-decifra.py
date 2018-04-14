pi = input()
sentence = input()

dict_pi = dict()
for i in range(len(pi)):
    dict_pi[pi[i]] = chr(ord('a') + i)

original = ''
for i in range(len(sentence)):
    original += dict_pi[sentence[i]]

print(original)