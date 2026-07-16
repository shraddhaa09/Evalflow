st=input("Enter String")

rev=""

for i in st:
    rev=i+rev

print("Reversed string is",rev)

if st==rev:
    print("Yes Palindrome")
else:
    print("No")