#Exercie 1
file01 = open("30 days 30 hours  operations.txt", "w+")
file01.write("I have completed 10 days successfully \t")
file01.close()
file01 = open("30 days 30 hours  operations.txt", "r+")
print(file01.read())
# Exercise 2
file01 = open("30 days 30 hours  operations.txt", "a+")
file01.write(" R VAISHNAV ")
file01.close()
file01 = open("30 days 30 hours  operations.txt", "r+")
print(file01.read())
