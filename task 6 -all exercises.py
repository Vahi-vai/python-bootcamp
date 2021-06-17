# Exercise 1
Names =  { 1 : "Vaishnav", 2 : "Sai" , 3 : "shiva" , 4 : "Dev"}
Names1 =  { 5 : "Vaishu" , 6 : "Sai pallavi " , 7 : "shivangi" , 9 : "Diya"}
Names.update(Names1)
print(Names)
# Exercise 2
print("\n")
Names.pop(2) # pops second item
print(Names)
# Exercise 3
print("\n")
fruits = ["banana" , "grapes" , " Orange"]
favourite = ["1st" , "2nd" , "3rd"]
newdict = {k : v for k, v in zip(favourite, fruits)}
print(newdict)
# Exercise 4
print("\n")
brands = {"sony", "apple", "samsung", "redmi"}
print(len(brands)) #Displays the length of set
# Exercise 5
print("\n")
countries1 = {"India" , "Pakistan" , "Afghanistan", "China" , "Iran"}
countries2 = {"Pakistan" , "Russia" , "New Zealand" ,"China"}
print(countries1 , countries2) # Before removing intersection of values
countries2 -= countries1
print( countries1 , countries2 ) #After removing intersection of values