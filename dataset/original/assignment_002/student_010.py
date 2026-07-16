a = input("Enter any word : ")

b = ""

for x in range(len(a)-1,-1,-1):
    b = b + a[x]

print("Reverse is =", b)

if(a==b):
    print("palindrome")
else:
    print("not palindrome")