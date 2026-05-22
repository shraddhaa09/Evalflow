data = input("Enter string ")

c = 0

for i in data:
    match i.lower():
        case 'a' | 'e' | 'i' | 'o' | 'u':
            c += 1

print(c)