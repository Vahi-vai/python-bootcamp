# Exercise1
r = lambda x, y : x * y
print(r(5625, 5358))
# Exercise 2
def fibonacci(count):
	fib_list = [0, 1]

	any(map(lambda _: fib_list.append(sum(fib_list[-2:])),
										range(2, count)))

	return fib_list[:count]

print(fibonacci(20))
# Exercise 3
nums = [2, 4, 6, 9 , 11]
n = 2
print("Original list: ", nums)
print("Given number: ", n)
filtered_numbers=list(map(lambda number:number*n,nums))
print("Result:")
print(' '.join(map(str,filtered_numbers)))
# Exercise 4
mlist = [12, 65, 54, 39, 102, 36, 225,]

result = list(filter(lambda x: (x % 9 == 0), mlist))

print("Numbers divisible by 9 are",result)
# Exercise 5
list1 = [10, 21, 4, 54, 65, 38, 112]

odd_count = len(list(filter(lambda x: (x%2 != 0) , list1)))
even_count = len(list(filter(lambda x: (x%2 == 0) , list1)))

print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)



