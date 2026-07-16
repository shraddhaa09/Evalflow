string = input()

count = sum(1 for ch in string if ch.lower() in "aeiou")

print(count)