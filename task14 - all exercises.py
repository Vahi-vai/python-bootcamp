# Exercise 1
print(dir(locals()['__builtins__']))
#Exercise 2
print("BASIC CALCI")
print("1. +")
print("2. -")
print("3. *")
print("4. /")

q=int(input("Enter Choice(1-4): "))
a=int(input("Enter A:"))
b=int(input("Enter B:"))

if q==1:
    c= a+b
elif q==2:
    c= a-b
    print("Difference = ",c)
elif  q==3:
    c=a*b
    print("Product = ",c)
elif q==4:
    c=a/b
    print("Quotient = ",c)
else:
    print(" wrong number")
# Exercise 4
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

# Exercise 5
try:
    age=int(input('Enter your age: '))
    if(age>18):
        print(" Get vaccinated soon, vaccines are available for you")
except:
    print ('You have entered an invalid value.')