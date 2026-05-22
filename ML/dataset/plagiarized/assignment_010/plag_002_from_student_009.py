year=int(input("Enter year: "))

print("Leap" if (year%400==0 or (year%4==0 and year%100!=0)) else "Not Leap")