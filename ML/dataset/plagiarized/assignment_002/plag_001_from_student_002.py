s = input("Enter string: ")

r = ""

for ch in s:
    r = ch + r

if r == s:
    print("Palindrome")
else:
    print("Not palindrome")