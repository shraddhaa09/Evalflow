word = input("Enter text: ")

count = 0

for letter in word:
    if letter.lower() == 'a':
        count += 1
    elif letter.lower() == 'e':
        count += 1
    elif letter.lower() == 'i':
        count += 1
    elif letter.lower() == 'o':
        count += 1
    elif letter.lower() == 'u':
        count += 1

print("Answer:", count)