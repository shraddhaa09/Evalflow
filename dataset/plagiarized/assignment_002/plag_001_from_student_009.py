s = input("Enter string: ")

flag = True

for i in range(0, len(s)//2):

    if s[i] != s[len(s)-1-i]:
        flag = False
        break

if flag:
    print("Palindrome")
else:
    print("Not palindrome")