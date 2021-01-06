#!/usr/bin/env python
# coding: utf-8

# # 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). Either version of the class will work; just pick the one you like better. Add an attribute called flavors that stores a list of ice cream flavors. Write a method that displays these flavors. Create an instance of IceCreamStand, and call this method.

# In[8]:


class Restaurant:
    """class which represents a restaurant."""
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        """A method which describes the restaurant."""
        print(f"Restaurant name : {self.restaurant_name.title()}")
        print(f"Cuisine type : {self.cuisine_type.title()}")
    
    def open_restaurant(self):
        """A method which indicate that the restaurant is open or not."""
        print(f"{self.restaurant_name.title()} is Open.")
    
    def set_number_served(self, number):
        """A method which sets the value of number served customer."""
        self.number_served = number
        print(f"{self.restaurant_name.title()} have served {self.number_served} customers.")
    
    def increment_number_served(self, increment_by):
        """A method which increments the numbers of served customers."""
        self.number_served += increment_by
        print(f"Today, {self.restaurant_name.title()} has successfully served to {increment_by} loyal customers.")

class IceCreamStand(Restaurant):
    """A class that inherits from Restaurant class."""
    
    def __init__(self, restaurant_name, cuisine_type):
        """initializing attributes for IceCreamStand class."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["vanila", "butter scotch", "mango blast", "real pista", "fruit mix"]
    
    def describe_flavors(self):
        """A method that displays the flavors given in a list."""
        print(f"The {self.restaurant_name.title()} has following flavors of Ice-Cream : ")
        for flavor in self.flavors:
            print(flavor.title())
    


# In[9]:


restaurant1 = IceCreamStand("royal dine", "a/c")


# In[10]:


restaurant1.describe_flavors()

