# Exercise 1
list1 = [2,6,8,5,4]
for i in range (len(list1)):
    list1[i] += 2
print(list1)
#Exercise 2
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end="")
    print()
# Exercise 3
nterms = int(input("Enter number of terms "))
n1, n2 = 0, 1
count = 0
if nterms <= 0:
   print("Enter a value above 0")
elif nterms == 1:
   print("Fibonacci series for ",nterms,":")
   print(n1)
else:
   print("Fibonacci series:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
# Exercise 4
print("Armstrong Number is a number which is equal to the sum of the cubes of its own digits")
n = int(input("Enter a number: "))
s = 0
t = n

while t > 0:
    d = t% 10
    s += d ** 3
    t //= 10

if n == s:
    print(n, "is an Armstrong number")
else:
    print(n, "is not an Armstrong number")

# Exercise 5
r = 9
for i in range (1,11):
    print( r , "* ", i , "=", r*i)

# Exercise 6
o = int(input("Enter a number: "))
if( o == 0):
    print("neither positive nor negative")
elif( o >0):
    print( o , "is positive")
else:
    print(o , "is negaitive")

# Exercise 7

days = int(input("Enter the number of days"))
ys = days/365
print("you are",ys,"years old")

#Exercise 8
import math

m = math.pi/3

print (" sine (pi/3) is : ", end="")
print (math.sin(m))
print ("cosine (pi/3) is : ", end="")
print (math.cos(m))
print ("tangent (pi/3) is : ", end="")
print (math.tan(m))

# Exercise 9

print("BASIC CALCI")
print("1. +")
print("2. -")
print("3. *")
print("4. /")

q=int(input("Enter Choice(1-4): "))

if q==1:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c= a+b
    print("Sum = ",c)
elif q==2:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c= a-b
    print("Difference = ",c)
elif  q==3:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a*b
    print("Product = ",c)
elif q==4:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a/b
    print("Quotient = ",c)
else:
    print(" wrong number")



