message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0) #The setdefault(0 ensures that the key is in the count dictionary  so the program does not show any KeyEron when count[character=count[character]+1
    count[character] = count[character] + 1

print(count)