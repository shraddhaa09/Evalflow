name = input()

count = 0

for ch in name:
    if ch.lower() == 'a':
        count += 1
    elif ch.lower() == 'e':
        count += 1
    elif ch.lower() == 'i':
        count += 1
    elif ch.lower() == 'o':
        count += 1
    elif ch.lower() == 'u':
        count += 1

print(count)