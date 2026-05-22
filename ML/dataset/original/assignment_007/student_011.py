string = input("Enter a string: ")

vowels = ['a','e','i','o','u','A','E','I','O','U']

res = 0

for i in string:
    if i in vowels:
        res = res + 1

print("Number of vowels:", res)