#Exercise 1
a = int(input("Enter first number"))
b = int(input("Enter second number"))
print("Addition of two numbers is" , a+b)
print("Subtraction of two numbers is" , a-b)
print("division of two numbers is" , a/b)
print("multiplication of two numbers is" , a*b)
# Exercise 2
def covid(name, temp):
    print( "patient name is" , name)
    print( "Patient temperature is" , temp)
name = str(input("Enter your name:"))
temperature = 98
temperature = int(input("Enter your body temperature"))
covid(name, temperature )