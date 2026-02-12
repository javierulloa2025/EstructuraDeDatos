a = int(input("Núm 1: "))
b = int(input("Núm 2: "))
c = int(input("Núm 3: "))

if a > b and b > c:
    if b > c:
        print(a, b, c)
    else:
        print(a, c, b)
elif b > a and b > c:
    if a > c:
        print(b,a,c)
    else:
        print(b, c, a)
else: 
          