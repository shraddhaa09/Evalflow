s = input("Enter text: ")

rev = ""

for i in s:
    rev = i + rev

if s == rev:
    print("It is palindrome")
else:
    print("It is not palindrome")