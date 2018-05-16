n = int(input())

for i in range(n):
    recording = input().split()
    sounds = set()
    while(True):
        sound = input().split()
        if len(sound) > 3:
            sounds_fox = [x for x in recording if x not in sounds]
            print(' '.join(sounds_fox))
            break
        else:
            sounds.add(sound[2])
