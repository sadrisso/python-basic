
a = int(input("Enter the first value: "))
b = int(input("Enter the second value: "))
c = int(input("Enter the third value: "))

if a>b and a>c:
    print(a, "is big")
elif b>a and b>c:
    print(b, "is big")
else:
    print(c, "is big")