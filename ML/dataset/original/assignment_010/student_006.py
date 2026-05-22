yr=int(input("Enter year"))

if yr%400==0:
    print("Leap Year")
else:
    if yr%100==0:
        print("Not Leap Year")
    else:
        if yr%4==0:
            print("Leap Year")
        else:
            print("Not Leap Year")