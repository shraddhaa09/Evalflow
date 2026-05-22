n=int(input("Year = "))

x=False

if n%4==0:
    if n%100==0:
        if n%400==0:
            x=True
    else:
        x=True

if x:
    print("Yes")
else:
    print("No")