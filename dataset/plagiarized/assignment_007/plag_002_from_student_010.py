txt = input("Enter string: ")

vowels = sum(1 for i in txt if i.lower() in "aeiou")

print(vowels)