num = int(input("Enter terms"))

f = 0
s = 1

i = 1

while i <= num:

    print(f)

    t = f + s
    f = s
    s = t

    i += 1