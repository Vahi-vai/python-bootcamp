# Exercise 1
import re
def is_allowed_specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)
    return not (string)
c = input("Enter anything")
print(is_allowed_specific_char(c))

#Exercise 2
import re

a = input("Enter any word")
b  = re.search("ab",a)
print(b)

# Exercse 3
j = input("Enter a sentence")
res= re.finditer(r"([0-9]{1,3})", j)
print(" words end with")
for i in res:
    print(i.group(0))

# Exercise 4
import re
results = re.finditer(r"([0-9]{1,3})", "i got 93 in maths, 96 in chemistry and 100 in physics")
print("Number of length 1 to 3")
for n in results:
     print(n.group(0))

# Exercise 6
import re
def text_match(text):
        if re.search("^[A-Z]*$",  text):
                return ("all the letters in the entered word is uppercase")
o = input("Enter a word")
print( text_match(o))