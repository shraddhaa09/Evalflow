def palindrome(s):

    if len(s) <= 1:
        return True

    if s[0] == s[-1]:
        return palindrome(s[1:-1])
    else:
        return False


word = input("Enter string: ")

if palindrome(word):
    print("Palindrome")
else:
    print("Not palindrome")