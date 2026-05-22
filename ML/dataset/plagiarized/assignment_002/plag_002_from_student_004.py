n = int(input("Enter any number: "))

copy = n
rev = 0

while n != 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

if copy == rev:
    print("Palindrome")
else:
    print("Not palindrome")