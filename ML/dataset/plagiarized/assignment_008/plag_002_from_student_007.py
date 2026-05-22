n=[55,22,11,99,77]

big=n[0]
k=0

while k<len(n):
    if n[k]>big:
        big=n[k]
    k=k+1

print("Biggest number is",big)