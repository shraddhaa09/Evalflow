y=eval(input("Enter any year: "))

if y%4!=0:
    print("Not a leap year")
else:
    if y%100==0 and y%400!=0:
        print("Not a leap year")
    else:
        print("Leap year")