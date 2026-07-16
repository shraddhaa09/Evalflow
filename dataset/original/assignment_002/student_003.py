text = input("Enter word: ")

i = len(text) - 1
reverse = ""

while i >= 0:
    reverse = reverse + text[i]
    i = i - 1

if reverse == text:
    print("Palindrome")
else:
    print("Not palindrome")