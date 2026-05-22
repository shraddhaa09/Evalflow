year=int(input("Year: "))

check=(year%400==0) or (year%4==0 and year%100!=0)

print(check)