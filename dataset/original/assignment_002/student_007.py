str1 = input("Enter value: ")

a = list(str1)
b = list(str1)

b.reverse()

if a == b:
    print("Palindrome")
else:
    print("Not Palindrome")