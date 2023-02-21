# Question 1 :
class Vehicle:
    def __init__(self, name_of_vehicle, max_speed, average_of_vehicle):
        self.name_of_vehicle = name_of_vehicle
        self.max_speed = max_speed
        self.average_of_vehicle = average_of_vehicle

# Question 2 :
class Vehicle:
    def __init__(self, name_of_vehicle, max_speed, average_of_vehicle):
        self.name_of_vehicle = name_of_vehicle
        self.max_speed = max_speed
        self.average_of_vehicle = average_of_vehicle


class Car(Vehicle):
    def seating_capacity(self, capacity):
        return f"{self.name_of_vehicle} has a seating capacity of {capacity}"

# Question 3
# Multiple inheritance is a feature of object-oriented programming languages in
# which a class can inherit attributes and methods from more than one parent class.
# Below is an example of multiple inheritance in Python:


class Parent1:
    def p1(self):
        self.str1 = "Parent1"
        print("Calling parent1 constructor")


class Parent2:
    def p2(self):
        self.str2 = "Parent2"
        print("Calling parent2 constructor")


class Child(Parent1, Parent2):
    pass


obj_Child = Child()
obj_Child.p1()
obj_Child.p2()

# Question 4 :
# Getters and setters are methods used to access and modify the values of an
# object's properties. They are used to ensure that the data stored in an object
# is valid and secure.


class gs:
    def __init__(self, age=0):
        self._age = age

    def get_age(self):
        return self._age

    def set_age(self, x):
        self._age = x


raj = gs()

raj.set_age(21)
print(raj.get_age())
print(raj._age)

# Question 5 :
# Method overriding in Python is the ability of a child class to redefine methods
# of its parent class. It is an important feature of object-oriented programming.


class Parent:
    def m1(self):
        print("Parent Method")


class Child(Parent):
    def m1(self):
        print("Child Method")


obj = Child()
obj.m1()
