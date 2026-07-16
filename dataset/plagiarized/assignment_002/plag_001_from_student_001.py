text = input("Enter text: ")

if text[::-1] == text:
    print("Palindrome")
else:
    print("Not Palindrome")