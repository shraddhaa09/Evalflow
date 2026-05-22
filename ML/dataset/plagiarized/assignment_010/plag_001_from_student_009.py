n=int(input())

print("Leap Year" if (n%4==0 and n%100!=0) or n%400==0 else "Not Leap Year")