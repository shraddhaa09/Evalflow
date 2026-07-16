a=int(input())

if a%400==0:
    print("Leap")
elif a%100==0:
    print("Not Leap")
elif a%4==0:
    print("Leap")
else:
    print("Not Leap")