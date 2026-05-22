str1 = input()

vowels = 0

for i in range(len(str1)):
    if str1[i] == 'a' or str1[i] == 'e' or str1[i] == 'i' or str1[i] == 'o' or str1[i] == 'u':
        vowels += 1

print(vowels)