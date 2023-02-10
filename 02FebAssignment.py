
# Question 1 

# For Loop:
# A for loop is used when you know the exact number of times you want to iterate through a loop. For example, if you wanted to print out the numbers 1-10, you could use a for loop like this:

numbers = [1,2,3,4,5,6,7,8,9,10]
for num in numbers:
    print(num)
    
# While Loop: 
# A while loop is used when you don't know how many times you need to iterate through a loop. For example, if you wanted to keep asking the user for input until they enter 'q', you could use a while loop like this:

user_input = ""
while user_input != "q": 
    user_input = input("enter something (enter 'q' to quit): ")


# Question 2
# To print sum and product of the first 10 natural number .
#Using for loop

sum = 0
product = 1
for i in range(1,11):
    sum += i
    product *= i
print("Sum of first 10 natural numbers are : ",sum)
print("Product of first 10 natural numbers are : ",product)


#Using while loop

sum = 0 
product = 1 
i = 1 
while i<=10: 
    sum += i 
    product *= i 
    i += 1 
print("Sum of first 10 natural numbers are : ",sum) 
print("Product of first 10 natural numbers are : ",product)

# Question 3
# Program to calculate electricity bill for a given unit 

unit = float(input("Enter total units consumed :  ")) 
  
if unit <= 100: 
    amount = unit * 4.5 
elif unit <= 200: 
    amount = 100 * 4.5 + (unit-100) * 6 
elif unit <= 300: 
    amount = 100 * 4.5 + 100 * 6 + (unit-200) * 10 
else: 
    amount = 100 * 4.5 + 100 * 6 + 100 * 10 + (unit-300) * 20 
  
print("Total Amount = ",amount)

# Question 4
# Creating a list of numbers from 1 to 100 
#Using for loop

cube_list = []
for i in range(1,101):
  cube = i**3
  if cube % 4 == 0 or cube % 5 == 0:
    cube_list.append(i)
print(cube_list)

#Using while loop
i = 1 
cube_list = [] 
while i <= 100: 
    cube = i**3 
    if cube % 4 == 0 or cube % 5 == 0: 
        cube_list.append(i) 
    i += 1  
print(cube_list)


# Question 5
s = "I want to become a data scientist"
vowels = 0
for i in s:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        vowels=vowels+1
print("Number of vowels are : ") 
print(vowels)

