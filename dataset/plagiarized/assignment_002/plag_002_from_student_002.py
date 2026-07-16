name = input("Enter value: ")

reverse = ""

for i in name:
    reverse = i + reverse

if name == reverse:
    print("Palindrome")
else:
    print("Not")