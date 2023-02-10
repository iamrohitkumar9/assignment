
# Question 1
list_of_tuples=[('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]
sorted_list = sorted(list_of_tuples, key=lambda x: x[1]) 
print(sorted_list) 

# Question 2
#Given list of integers
nums = [1, 2, 3, 4, 5,6,7,8,9,10]
result = list(map(lambda x: x**2, nums))
print(result)

# Question 3
list_of_integers = [1, 2, 3, 4,5,6,7,8,9,10]
result = tuple(map(lambda x: str(x), list_of_integers)) 
print(result)

# Question 4
from functools import reduce

list_of_numbers = [x for x in range(1,26)]
product = reduce((lambda x, y: x * y), list_of_numbers) 
print("Product of the list is :  ", product)

# Question 5
list1 = [2, 3, 6,9,27,60,90,120,55,46]
filtered_list = list(filter(lambda x: (x % 2 == 0 and x % 3 == 0), list1)) 
print("Numbers divisible by 2 and 3 are :  ", filtered_list)

# Question 6
list_of_strings = ['python', 'php', 'aba', 'radar', 'level']
palindromes = list(filter(lambda x: x == "".join(reversed(x)), list_of_strings)) 
print("Palindromes in the given list of strings:  ", palindromes)
