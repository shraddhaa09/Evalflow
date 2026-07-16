def reverse(x):
    if len(x)==0:
        return x
    return reverse(x[1:])+x[0]

a=input()
print(reverse(a))