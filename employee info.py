#importing library
from tkinter import *
from tkinter import ttk

window = Tk()
#Declaring Window Title
window.title("EMPLOYEE INFO")
#Declaring Window size
window.geometry('500x500')
#Declaring Window Color
window.configure(background = "orange");
#below four fields are declared
Firstname = Label(window ,text = "First Name").grid(row = 0,column = 0)
LastName = Label(window ,text = "Last Name").grid(row = 1,column = 0)
Email = Label(window ,text = "Email Id").grid(row = 2,column = 0)
Mobile = Label(window ,text = "Contact Number").grid(row = 3,column = 0)
Location = Label(window ,text = "location").grid(row = 4,column = 0)
Bloodgroup = Label(window ,text = "Blood Group").grid(row = 5,column = 0)
Aadharnum = Label(window ,text = "Aadhaar number").grid(row = 6 ,column = 0)
salary = Label(window ,text = "salary/annum").grid(row = 7,column = 0)
degree = Label(window ,text = "Degree").grid(row = 8,column = 0)
transport = Label(window ,text = "Transport").grid(row = 9,column = 0)
role =  Label(window ,text = "Role").grid(row = 10,column = 0)

Firstname1 = Entry(window).grid(row = 0,column = 1)
Lastname1 = Entry(window).grid(row = 1,column = 1)
Email1 = Entry(window).grid(row = 2,column = 1)
Mobile1 = Entry(window).grid(row = 3,column = 1)
Location1 =Entry(window).grid(row = 4,column = 1)
Bloodgroup1 =Entry(window).grid(row = 5,column = 1)
Aadharnum1 =Entry(window).grid(row = 6,column = 1)
salary1 =Entry(window).grid(row = 7,column = 1)
degree1 =Entry(window).grid(row = 8,column = 1)
role1 =  Radiobutton(window, text="SAP CONSULTANT",value=1).grid(row = 10 , column = 1)
role2 =  Radiobutton(window, text="Sales" , value=2).grid(row = 11 , column = 1)
role3 =  Radiobutton(window, text="logistics", value=3).grid(row = 12 , column = 1)
options = ["bike","car","bus","train"]
clicked = StringVar()
clicked.set("Select")
drop = OptionMenu(window, clicked, *options)
drop.grid( row =9 , column  =1)




#fubction declaration
def clicked():
    res = "Welcome to " + txt.get()
    lbl.configure(text= res)
btn = ttk.Button(window ,text="Submit").grid(row=13,column=3)
window.mainloop()
