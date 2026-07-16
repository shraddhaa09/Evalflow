year=int(input("Enter year"))

x=False

if year%4==0:
    if year%100==0:
        if year%400==0:
            x=True
    else:
        x=True

if x:
    print("Leap")
else:
    print("Not Leap")