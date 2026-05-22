word = input("Enter a string: ")

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")