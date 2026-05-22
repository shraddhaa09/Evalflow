a = input()

total = 0
x = 0

while x < len(a):
    if a[x].lower() in "aeiou":
        total = total + 1
    x += 1

print(total)