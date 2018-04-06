message = input()
key = int(input())

cipher = ""
for x in message:
    cipher += chr(((int(x) + key) % 10) + ord('0'))

print(cipher)