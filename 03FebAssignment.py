
# Question 1

# "def" keyword is used to create function .
# A function to return a list of odd numbers in the
# range of 1 to 25.

def createOddList():
    odd_list = []
    for num in range(1, 26):
        if num % 2 != 0:
            odd_list.append(num)
    return odd_list
print(createOddList())


# Question 2

#   *args and **kwargs are used in functions to allow for an arbitrary number of arguments to be passed into the function. *args is used to pass a non-keyworded, variable-length argument list, while **kwargs is used to pass a keyworded, variable-length argument list. 

#Function for *args

def sum_args(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(sum_args(1,2,3))
 
#Function for **kwargs

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")
 
print_kwargs(name="John", age=25)


# Question 3
# An iterator in Python is an object that can be used to iterate over a sequence of values. The method used to initialise the iterator object is the iter() method, and the method used for iteration is the next() method.


my_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
my_iter = iter(my_list)

print(next(my_iter))
print(next(my_iter)) 
print(next(my_iter)) 
print(next(my_iter)) 
print(next(my_iter))


# Question 4 
# A generator function is a special type of function in Python that returns an iterable set of items, one at a time, in a special way. The yield keyword is used to return each item one at a time from the generator function.

def my_generator():
    yield 1
    yield 2
    yield 3
    
for item in my_generator(): 
    print(item) 


# Question 5

def prime_numbers():
    num = 2
    while num < 1000:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            yield num
        num += 1


prime_gen = prime_numbers()
   
print("The first 20 prime numbers are :  ") 
for i in range(20): 
    print(next(prime_gen), end=" ")

# Question 6

a = 0 
b = 1 
print("The first 10 Fibonacci numbers are : ") 
while b < 10: 
    print(b) 
    a, b = b, a + b


# Question 7

[letter for letter in 'pwskills']


# Question 8 
# Program to check if a number is palindrome or not

num = int(input("Enter a number: "))
temp = num
reverse = 0
while(num > 0):
    remainder = num % 10
    reverse = (reverse * 10) + remainder
    num = num // 10
if(temp == reverse):  
    print("The number is a palindrome! ")  
else:  
    print("The number isn't a palindrome! ")


# Question 9

odd_numbers = [x for x in range(1,101) if x % 2 != 0]
print(odd_numbers)



