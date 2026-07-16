first = input("Enter first string: ").lower()
second = input("Enter second string: ").lower()

if sorted(first) == sorted(second):
    print("Anagram")
else:
    print("Not Anagram")