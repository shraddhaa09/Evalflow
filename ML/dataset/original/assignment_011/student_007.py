num = input()

count = 0

i = 0
while i < len(num):
    count += int(num[i])
    i += 1

print(count)