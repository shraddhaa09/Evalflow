def checkPalindrome(a):
    if a == a[::-1]:
        return True
    else:
        return False

x = input("Enter string: ")

if checkPalindrome(x):
    print("Palindrome")
else:
    print("Not Palindrome")