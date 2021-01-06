#!/usr/bin/env python
# coding: utf-8

# # 9-1. Restaurant: Make a class called Restaurant. The __init__() method foraRestaurant should store two attributes: a restaurant_name and a cuisine_type.
# # Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
# # Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.

# In[1]:


class Restaurant():
    """class which represents a restaurant."""
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        """A method which describes the restaurant."""
        print(f"Restaurant name : {self.restaurant_name.title()}")
        print(f"Cuisine type : {self.cuisine_type.title()}")
    
    def open_restaurant(self):
        """A method which indicate that the restaurant is open or not."""
        print(f"{self.restaurant_name.title()} is Open.")


# In[2]:


restaurant1 = Restaurant("royal dine", "a/c")


# In[3]:


restaurant1.describe_restaurant()


# In[4]:


restaurant1.open_restaurant()


# In[7]:


restaurant1.restaurant_name


# In[8]:


restaurant1.cuisine_type

