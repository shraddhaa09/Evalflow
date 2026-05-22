text = input("Enter text: ")

v = 0

for i in text:
    if i.lower() == 'a':
        v += 1
    elif i.lower() == 'e':
        v += 1
    elif i.lower() == 'i':
        v += 1
    elif i.lower() == 'o':
        v += 1
    elif i.lower() == 'u':
        v += 1

print("Answer:", v)