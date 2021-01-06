#!/usr/bin/env python
# coding: utf-8

# # 9-3. Users: Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile. Make a method called describe_user() that prints a summary of the user’s information. Make another method called greet_user() that prints a personalized greeting to the user.
# # Create several instances representing different users, and call both methods for each user.

# In[6]:


class User():
    """A class that related to the user."""
    
    def __init__(self, first_name, last_name, dob, email, phoneno):
        """A default method which accepts arguments for class User()."""
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.email = email
        self.phoneno = phoneno
        
    def describe_user(self):
        """A method which decribes the user."""
        print(f"First name : {self.first_name.title()}")
        print(f"Last name : {self.last_name.title()}")
        print(f"Date of Birth : {self.dob.title()}")
        print(f"Email : {self.email}")
        print(f"Phone No : {self.phoneno}")
    
    def greet_user(self):
        """A method which greets the user."""
        print(f"Good Morning, {self.first_name.title()}.")


# In[17]:


user1 = User("mehul", "rana", "01-01-2001", "mehul@hmail.com", 1234567891)
user2 = User("bhavik", "jadav", "18-11-2001", "bhavik@bmail.com", 2323232323)


# In[18]:


user1.describe_user()
print()
user1.greet_user()


# In[19]:


user2.describe_user()
print()
user2.greet_user()

