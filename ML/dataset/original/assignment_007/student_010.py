txt = input()

count = sum(1 for i in txt if i.lower() in "aeiou")

print(count)