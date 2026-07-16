year=int(input())

c1=year%4
c2=year%100
c3=year%400

if c1==0 and c2!=0:
    print("Leap Year")
elif c3==0:
    print("Leap Year")
else:
    print("Not Leap Year")