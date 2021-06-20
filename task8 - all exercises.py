# Exercise 1
dict1 = {1 : "vijay" , 2 : "Ajith" , 3 :"Dhanush"}
dict2 = {4 : "Sivakarthikeyan" , 5: "Sidharth malhotra"}
dict1 = dict1 | dict2
print(dict1)

# Exercise 2
value1 = [1,5,23,69,3]
print(value1)
value1.sort()
print(value1)

# Exercise 3
val1 = {2: 5, 5: 3, 3:2 , 1:5 , 4 : 4}
print(val1)
print(len(val1))
val1 = sorted(val1.items())
print("by built in method",val1)
print("by using function")
for i in range(len(val1)):
    print(val1[i])

# Exercise 4
v = " good morning"
s = v.split()
print(v)
f = int(input("Enter which word to replace (1/2):"))
g = input("Enter the word to Replace with :")
s[f-1] = g
str1 = " "
j = str1.join(s)
print(j)

# Exercise 5
k = "All the best vaishnav"
p = " "
print(k)
l = input("Enter the word : ")
u= k.split()
for i in range(len(u)):
    if (u[i] == l):
        u = k.split()
        o =l .capitalize()
        u[i] = o
        str2 = " "
        q = str2.join(u)
        print(q)

#Exercise 6
from collections import Counter
w = [ 55,23,55,26,2,2,3]
y = Counter(w)
new_list = list([item for item in y if y[item]>1])
print(new_list)

#Exercise 7
num1 = 5
num2 = 6
num3 = 9
sum1 = num1 +num2 + num3
m = int(input("Enter the number to divide the sum"))
b = sum1/m
print(b)

#Exercise 8
list2 = [2,4,3,5,3,1,7]
list2.sort()
sum2 = 0
for i in range(len(list2)):
    sum2 += list2[i]
print("Average" ,(sum2/(len(list2))))
print("Median" ,list2[4])
from collections import Counter
y = Counter(list2)
new_list = list([item for item in y if y[item]>1])
print("mode" , new_list)

# Exercise 9
def swap_case_string(str1):
   result_str = ""
   for item in str1:
       if item.isupper():
           result_str += item.lower()
       else:
           result_str += item.upper()
   return result_str
name23 = input("Enter a sentence")
print(swap_case_string(name23))

#Exercise 10

def decToBinary(n):
    binaryNum = [0] * n
    i = 0
    while (n > 0):
        binaryNum[i] = n % 2
        n = int(n / 2)
        i += 1

    for j in range(i - 1, -1, -1):
        print(binaryNum[j], end="")
    print("\n")
def decToOctal(n):
    octalNum = [0] * 100
    i = 0
    while (n != 0):
        octalNum[i] = n % 8
        n = int(n / 8)
        i += 1
    for j in range(i - 1, -1, -1):
            print(octalNum[j], end="")
n = int(input("Enter the number:"))
decToBinary(n)
decToOctal(n)






