word = input("Enter word: ")

check = 1

for i in range(len(word)//2):

    if word[i] != word[-i-1]:
        check = 0

if check == 1:
    print("Palindrome")
else:
    print("Not palindrome")