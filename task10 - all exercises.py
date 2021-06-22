# Exercise 1
class BankAccount:
	bal = 1000
	def __init__(self, fn, dep):
		self.fn = fn
		self.bal += dep
	def getDetails(self):
		print("Forename: ", self.fn)
	def getBalance(self):
		print("Balance: $ ", self.bal)
j = input("Enter your name")
o = int(input("Enter the amount you want to deposit"))
d = BankAccount("j",o)
print(d.getDetails(), d.getBalance())