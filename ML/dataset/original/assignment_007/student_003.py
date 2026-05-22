a = input("String : ")

count = 0
i = 0

while i < len(a):
    if a[i].lower() in "aeiou":
        count += 1
    i += 1

print(count)