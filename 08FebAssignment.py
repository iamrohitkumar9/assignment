                # Question 1 :
# Abstraction in OOPs is the process of hiding the implementation details from the user. 
# It helps to reduce complexity and also improves security of an application.
# For example, when you use a mobile phone, you only need to know how to make calls or 
# send messages. You don't need to know how the underlying hardware and software works. 
# This is an example of abstraction.

class Car: 
    def __init__(self, model, color): 
        self.model = model 
        self.color = color 

    def show_model(self): 
        return self.model 

    def show_color(self): 
        return self.color 

obj = Car("Ford", "Red") 
print("Model of the car is", obj.show_model()) 
print("Color of the car is", obj.show_color())



                # Question 2 :
# Abstraction is the process of hiding the implementation details from the user and 
# showing only the functionality. It helps in reducing complexity and is used to 
# focus on relevant data of an application.
# Encapsulation is the process of binding data and code together into a single unit. 
# It helps in protecting data from outside world and allows access to methods and 
# variables only through an interface.
# For example, a car is an example of abstraction as it hides all its internal components 
# from the user and only shows its functionality like starting, stopping, accelerating etc. 
# On the other hand, encapsulation can be seen in a car's engine where all its components 
# like spark plugs, pistons etc are bound together into a single unit which can be accessed 
# only through an interface like oil filter or air filter.

# Example of Abstraction :

class Car: 
    def __init__(self, model, color): 
        self.model = model 
        self.color = color 

    def show_model(self): 
        return self.model 

    def show_color(self): 
        return self.color 

obj = Car("Ford", "Red") 
print("Model of the car is", obj.show_model()) 
print("Color of the car is", obj.show_color())

# Example of Encapsulation :

class EncapsulationExample:
    def __init__(self):
        self.public_data = "This is public data"
        self._protected_data = "This is protected data"
        self.__private_data = "This is private data"

    def get_private_data(self):
        return self.__private_data

    def set_private_data(self, value):
        self.__private_data = value
        
example = EncapsulationExample() 
print(example.public_data)  
print(example._protected_data)  
print(example.get_private_data())


            # Question 3 :
# The ABC (Abstract Base Classes) module in Python is a set of abstract base classes that
# provide a way to create interfaces and enforce contracts for subclasses. 
# It is used to define abstract base classes that can be used to test whether 
# a class provides a particular interface or has a particular property. 
# This helps developers ensure that their code is consistent and follows certain standards.

            # Question 4:
# Data abstraction can be achieved through encapsulation, which is the process of 
# hiding the implementation details of a class from its users. This allows users to
# interact with an object without needing to know how it works internally.
# we can achieve by using classobjectname._classname__privatevariablename

class EncapsulationExample:
    def __init__(self):
        self.public_data = "This is public data"
        self._protected_data = "This is protected data"
        self.__private_data = "This is private data"

    def get_private_data(self):
        return self.__private_data

    def set_private_data(self, value):
        self.__private_data = value
        
example = EncapsulationExample() 
print(example.public_data)  
print(example._protected_data)  
print(example.get_private_data())


                # Question 5 :
# No, we cannot create an instance of an abstract class. An abstract class is a 
# class that contains one or more abstract methods, which are methods that do not
# have any implementation. Abstract classes cannot be instantiated, meaning they 
# cannot be used to create objects.
