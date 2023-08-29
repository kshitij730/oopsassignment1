#!/usr/bin/env python
# coding: utf-8

# In[2]:


"""Create a vehicle class with an init method having instance variables as name_of_vehicle, max_speed
and average_of_vehicle."""


# In[3]:


class vehicle:
    def __init__(self, name_of_vehicle, max_speed, average_of_vehicle):
        self.name_of_vehicle = name_of_vehicle
        self.max_speed = max_speed
        self.average_of_vehicle = average_of_vehicle



# In[4]:


car = vehicle("Car", 300, 12)


# In[5]:


car.name_of_vehicle


# In[6]:


car.max_speed


# In[7]:


car.average_of_vehicle


# In[8]:


"""Create a child class car from the vehicle class created in Que 1, which will inherit the vehicle class.
Create a method named seating_capacity which takes capacity as an argument and returns the name of
the vehicle and its seating capacity."""


# In[9]:


"""What are getter and setter in python? Create a class and create a getter and a setter method in this
class."""


# In[10]:


class Person:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age    # Private attribute

    # Getter method for 'name'
    def get_name(self):
        return self.__name

    # Getter method for 'age'
    def get_age(self):
        return self.__age

    # Setter method for 'name'
    def set_name(self, name):
        self.__name = name

    # Setter method for 'age'
    def set_age(self, age):
        if age >= 0:  # Basic validation for age
            self.__age = age
        else:
            print("Age cannot be negative")

# Creating an instance of the class
person = Person("Alice", 30)

# Using the getter methods
print("Name:", person.get_name())
print("Age:", person.get_age())

# Using the setter methods
person.set_name("Bob")
person.set_age(25)

# Using the getter methods again
print("Updated Name:", person.get_name())
print("Updated Age:", person.get_age())


# In[11]:


"""Q5.What is method overriding in python? Write a python code to demonstrate method overriding."""


# In[12]:


class Shape:
    def area(self):
        pass  # Placeholder method

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

# Creating instances of the subclasses
circle = Circle(5)
square = Square(4)

# Calling the overridden 'area' method for both shapes
print("Circle Area:", circle.area())
print("Square Area:", square.area())


# In[ ]:




