# first print python start

print("Hello World");

# first print python end

# variable declire and print start

numberOne = 1
numberTwo = 2

nameOne = 'Shoeb Akter Drisso'
nameTwo = 'Shakib Al Hasan'

listOne = ['Alu', 'Piyaj', 1, 'Tomato', 1.2]

print(numberOne + numberTwo)
print(nameOne + nameTwo)
print(listOne)

# variable declire and print end

# taking user input start

userName = input("Enter your name: ")
userAge = input("Enter your age: ")
print("Hello ",userName, "Your age is ",userAge)

# taking user input end

# conditional statement start

rain = True
if rain:
    print('I will not go')
else:
    print('I will go')

age = 17
if age >= 18:
    print('You are adult')
else:
    print('Under 18')

# conditional statement end

# logical operator & if elif
    
print(10 + 5 == 15 and 10 - 5 == 10) # if one true and one false then he returns false
print(10 + 5 == 15 and 10 - 5 == 5) # if both are true then he returns true

print(10 > 5 or 10 < 5) # if one logic is true then he return true 
print(10 > 55 or 100 < 20) # he returns false when both are false

print(not (10 >= 100)) # it reverse 

marks = 89
if marks >= 90 and marks <= 100:
    print('You get 2 box of chocolate')
elif marks >= 80 and marks <= 90:
    print('You get 1 box of chocolate')
else:
    print('You got nothing')

# logical operator and if elif end