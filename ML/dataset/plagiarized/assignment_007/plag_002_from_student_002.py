s = input()

vowels = "AEIOUaeiou"
c = 0

for ch in s:
    if ch in vowels:
        c = c + 1

print("Vowels =", c)