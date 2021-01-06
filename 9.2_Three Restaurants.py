#!/usr/bin/env python
# coding: utf-8

# # 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three different instances from the class, and call describe_restaurant() for each instance.

# In[4]:


class Restaurant():
    """A class that represents a restaurant."""
    
    def __init__(self, restaurant_name, cuisine_type):
        """A method which represents the arguments which will be passing here instead of passing in the Restaurant()"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        """A methos which just simply describes the restaurant."""
        print(f"Restaurant name : {self.restaurant_name.title()}")
        print(f"Cuisine type : {self.cuisine_type.title()}")
        
    def open_restaurant(self):
        """A method that indicates whether the reaturant is open or not."""
        print(f"{self.restaurant_name.title()} is Open.")


# In[5]:


restaurant1 = Restaurant("royal dine", "a/c")
restaurant2 = Restaurant("pizzarino", "a/c")
restaurant3 = Restaurant("pasta ride", "non a/c")


# In[6]:


restaurant1.describe_restaurant()
restaurant1.open_restaurant()


# In[8]:


restaurant2.describe_restaurant()
restaurant2.open_restaurant()


# In[11]:


restaurant3.describe_restaurant()
restaurant3.open_restaurant()


# In[14]:


restaurant1.restaurant_name


# In[15]:


restaurant1.cuisine_type


# In[16]:


restaurant2.restaurant_name


# In[17]:


restaurant2.cuisine_type


# In[20]:


restaurant3.restaurant_name


# In[21]:


restaurant3.cuisine_type

