def palindrome(txt):

    if len(txt) == 0 or len(txt) == 1:
        return True

    if txt[0] != txt[-1]:
        return False

    return palindrome(txt[1:-1])


a = input("Enter word: ")

if palindrome(a):
    print("Palindrome")
else:
    print("Not Palindrome")