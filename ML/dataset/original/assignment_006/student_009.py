n=int(input())

def factorial(x):
    f=1
    for i in range(1,x+1):
        f=f*i
    return f

print(factorial(n))