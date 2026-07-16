name = input("Enter string: ")

name = name.lower()

reverse = name[::-1]

if name == reverse:
    print("Palindrome")
else:
    print("Not palindrome")