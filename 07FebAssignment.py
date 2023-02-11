# Question 1

def check_password(password):
    if len(password) != 10:
        return "Invalid Password"

    upper_count = 0
    lower_count = 0
    for char in password:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    if upper_count < 2 or lower_count < 2:
        return "Invalid Password"

    num_count = 0 
    special_char_count = 0 

    for char in password: 
        if char.isdigit(): 
            num_count += 1 

        elif not char.isalnum(): 
            special_char_count += 1

    if num_count == 0 or special_char_count < 3: 
        return "Invalid Password"


    return "Valid Password"
    

# Question 2 


# Check if the string starts with a particular letterY
string=input("Enter the string : ")
result = list(filter(lambda x: x.startswith('letter'), string))

# Check if the string is numeric
string=input("Enter the string : ")
result = list(filter(lambda x: x.isnumeric(), string))

# Sort a list of tuples having fruit names and their quantity. [("mango",99),("orange",80), ("grapes", 1000)
fruits_list = [("mango",99),("orange",80), ("grapes", 1000)]  
sorted_fruits_list = sorted(fruits_list , key= lambda item : item[1])  

# Find the squares of numbers from 1 to 10
result = list(map(lambda x: x**2, range(1,11)))

# Find the cube root of numbers from 1 to 10
result = list(map(lambda x: x**3, range(1,11)))

# Check if a given number is even
number=int(input("Enter a number : "))
result = list(filter(lambda x: x % 2 == 0, number))

# Filter odd numbers from the given list - [1,2,3,4,5,6,7,8,9,10]
result = list(filter(lambda x :x % 2 != 0, [1,2,3,4,5,6,7,8,9,10]))

# Sort a list of integers into positive and negative integers lists - [1,2,3,4,5,6,-1,-2,-3,-4,-5,0]
positive_list=[x for x in [1,2,3,4,5,-1,-2,-3,-4,-5] if x>=0]  
negative_list=[x for x in [1,2,3,4,-5,-1,-2,-3] if x<0]


