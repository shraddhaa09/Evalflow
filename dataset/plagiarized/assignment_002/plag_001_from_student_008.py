def check(s):

    if len(s) <= 1:
        return True

    if s[0] == s[-1]:
        return check(s[1:-1])

    return False


word = input("Enter string: ")

if check(word):
    print("Palindrome")
else:
    print("Not palindrome")