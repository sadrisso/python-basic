
year = int(input())


# method 1
if year % 400 == 0:
    print("Leap Year")
elif year % 100 == 0:
    print("Not Leap Year")
elif year % 4 == 0:
    print("Leap Year")
else:
    print("Not Leap Year")


# method 2
if year % 400 == 0 and year % 100 == 0:
    print("Leap year")
elif year % 4 == 0 and year % 100 != 0:
    print("Leap year")
else:
    print("Not leap year")


# method 3
if year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
    print("Lear year")
else:
    print("Not leap year")