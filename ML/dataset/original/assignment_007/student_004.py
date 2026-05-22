name = input()

x = ['a','e','i','o','u']
total = 0

for i in name.lower():
    if i in x:
        total = total + 1

print(total)