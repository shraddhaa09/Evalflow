num = int(input("Enter number: "))

temp = num
reverse = 0

while num > 0:
    rem = num % 10
    reverse = reverse * 10 + rem
    num = num // 10

if temp == reverse:
    print("Palindrome Number")
else:
    print("Not Palindrome")