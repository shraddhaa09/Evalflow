text = input()

v = "aeiouAEIOU"
c = 0

for ch in text:
    if ch in v:
        c += 1

print("Vowels =", c)