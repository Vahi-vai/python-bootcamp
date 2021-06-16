# Exercise 1
n = int(input("Enter the number of integers: "))
c = list()
for i in range(0 , n):
    a = int(input("Enter number"))
    c.append(a)
print(c)
d = int(input("Enter a number to add in the list:"))
c.append(d)  # adds am item
print(c)
c.remove(c[3]) #removes an item
print (" List after deleting an item",c)
c.sort()  #sorts the list
e = c[len(c) - 1] #saving the largest number
print("Largest number is", e )
f = c[0] # saving the smallest number
print("smallest number", f)

#Exercise 2
h = ("vaishnav", 52,'aisha')
print( h[::-1])

#Exercise 3
j = ("ganesha", 956,"shiva")
k = list(j)
print(k)