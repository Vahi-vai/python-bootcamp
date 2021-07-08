# Exercises 1
def merge(list1, list2):
    merged_list = tuple(zip(list1, list2))
    return merged_list
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
print(merge(list1, list2))
def merge(list1, list2):
    merged_list = [(list1[i], list2[i]) for i in range(0, len(list1))]
    return merged_list
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
print(merge(list1, list2))
# Exercise 2
lst1 = ["E", "A", "I", "T", "F", "U", "P"]
rng1 = (list(range(1 , 8)))
lst = zip(lst1,rng1)
print(lst)
#Exercise 3
listt = [1,23,4,5,89,6,7,58,56,35,698,41,25,46,48,2]
listt.sort()
print(listt)
#Exercise 4
numbers = [1,2,6,7,13,14,12,17,16,53,67,34,75,48]
def even_numbers(num):
    if(num%2 == 0):
        return True
    else:
        return False
evenNums = filter(even_numbers, numbers)
list6 = []
for num in evenNums:
    list6.append(num)
print(list6)
for ele in list6:
    if ele in numbers:
        numbers.remove(ele)
list8 = numbers
print(list8)



