# Question 1

list1 = [1,2,3,4, [44,55,66, True], False, (34,56,78,89,34), {1,2,3,3,2,1}, {1:34, "key2": [55, 67, 78, 89], 4: (45,
22, 61, 34)}, [56, 'data science'], 'Machine Learning']
def product_list(list1):
    flat_list = []
    for item in list1:
        if type(item) == list or type(item) == tuple or type(item) == dict:
            for sub_item in item:
                if type(sub_item) == int or type(sub_item) == float:
                    flat_list.append(sub_item)
        elif type(item) == int or type(item) == float:
            flat_list.append(item)

    product = 1 
    for num in flat_list: 
        product *= num 

    return product 

  
print("Product of all the numbers in the given list is :",product_list(list1))

# Question 2 

s =("I want to become a Data Scientist")
message=s.lower()

encrypted_message = ""

for char in message:
    if char == 'a':
        encrypted_message += 'z'
    elif char == 'b':
        encrypted_message += 'y'
    elif char == 'c':
        encrypted_message += 'x'
    elif char == ' ':  # whitespace character 
        encrypted_message += '$'  # replace with dollar sign 
    else:  # keep punctuation marks unchanged 
        encrypted_message += char  

        
print("Encrypted Message:", encrypted_message)