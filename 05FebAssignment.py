
# Question 1
# Class:A class is a blueprint or template for creating objects. It defines the data and behavior of a type. In object-oriented programming, classes are used to represent real-world entities such as cars, animals, people, etc.
# Object:An object is an instance of a class. It is a real-world entity that has state (data) and behavior (operations). Objects are created from classes and can interact with each other through methods.
class Car: 
    def __init__(self, model, color): 
        self.model = model 
        self.color = color 

    def show_model(self): 
        print("Model:", self.model) 

    def show_color(self): 
        print("Color:", self.color) 
audi = Car("Audi A4", "black") 
ferrari = Car("Ferrari 488", "red") 
audi.show_model()  
ferrari.show_color()

# Question 2
# The four pillars of OOPS are :
# 1. Abstraction
# 2. Encapsulation
# 3. Inheritance
# 4. Polymorphism

# Question 3
#  "__init__()" function is known as constructor .
# The __init__() function is used to initialize an object's state. It is called when an object of a class is created. It can be used to set the default values for the attributes of the object.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
person1 = Person("Rohit", 36)
print(person1.name)
print(person1.age)  

# Question 4 
# In object-oriented programming system (OOPs), self is a keyword used to refer to the current instance of a class.
# It is used to access the attributes and methods of the class in which it is used. Self allows an object to refer to itself, and makes it possible for the object to access its own attributes and methods.

# Question 5
# Inheritance is a way of creating new classes (called child classes) that are based on existing classes (called parent classes). It allows us to reuse code and add new features or modify existing ones without having to rewrite the entire code.
# There are 3 types of inheritance.

# Example of single inheritance:
class Parent: 
    def __init__(self): 
        self.value = "Parent" 
  
class Child(Parent): 
    def __init__(self): 
        super().__init__() 
        self.value = "Child" 

# Example of multiple inheritance:
class Parent1: 
    def __init__(self): 
        self.value1 = "Parent1" 

class Parent2: 
    def __init__(self): 
        self.value2 = "Parent2"  

class Child(Parent1, Parent2): 
    def __init__(self): 
        super().__init__()  

# Example of multi-level inheritance:
class Grandparent:  
    def __init__(self):  
        self.gp_value = "Grandparent"  

class Parent(Grandparent): 
    def __init__(self):  
        super().__init__()    

class Child(Parent): 
    def __init__(self):  
        super().__init__()