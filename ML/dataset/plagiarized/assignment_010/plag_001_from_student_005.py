n=int(input())

ans=(n%4==0 and n%100!=0) or n%400==0

print(ans)