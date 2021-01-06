#!/usr/bin/env python
# coding: utf-8

# # 9-4. Number Served: Start with your program from Exercise 9-1 (page 162). Add an attribute called number_served with a default value of 0. Create an instance called restaurant from this class. Print the number of customers the restaurant has served, and then change this value and print it again. Add a method called set_number_served() that lets you set the number of customers that have been served. Call this method with a new number and print the value again.
# # Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. Call this method with any number you like that could represent how many customers were served in, say, a day of business.

# In[41]:


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


# In[42]:


restaurant = Restaurant("royal dine", "a/c")


# In[43]:


restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(10)
restaurant.increment_number_served(10)
print(f"Total served : {restaurant.number_served}")

