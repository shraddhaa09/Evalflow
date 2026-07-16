s = input("Enter string: ")

flag = 1

for i in range(len(s)//2):

    if s[i] != s[len(s)-i-1]:
        flag = 0
        break

if flag == 1:
    print("Palindrome")
else:
    print("Not Palindrome")