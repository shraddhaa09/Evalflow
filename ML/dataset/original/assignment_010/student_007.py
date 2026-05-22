year=int(input())

leap=0

if year%4==0:
    leap=1

if year%100==0 and year%400!=0:
    leap=0

if leap==1:
    print("Leap year")
else:
    print("Not leap year")