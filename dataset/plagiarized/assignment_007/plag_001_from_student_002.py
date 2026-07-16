txt = input()

letters = "aeiouAEIOU"
count = 0

for i in txt:
    if i in letters:
        count += 1

print("Vowels =", count)