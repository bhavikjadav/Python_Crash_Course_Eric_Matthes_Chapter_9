#!/usr/bin/env python
# coding: utf-8

# # 9-8. Privileges: Write a separate Privileges class. The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7. Move the show_privileges() method to this class. Make a Privileges instance as an attribute in the Admin class. Create a new instance of Admin and use your method to show its privileges.

# In[18]:


class User:
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
        
class Previleges:
    """A method that displays the previleges of an Admin."""
    
    def __init__(self):
        """A structure of class Prevleges."""
        self.previleges = ["can add post", "can delete post", "can block user", "can mute user", "can hide user"]
        
    def show_previleges(self):
        """A method that shows [revileges of a Admin."""
        print("Admin have following previleges : ")
        for previlege in self.previleges:
            print(previlege.title()) 
        
class Admin(User):
    """A class that inherits from User class."""
    
    def __init__(self, first_name, last_name, dob, email, phoneno):
        """a structure of Admin class."""
        super().__init__(first_name, last_name, dob, email, phoneno)
        self.previleges = Previleges()
    
   


# In[19]:


user1 = Admin("bhavik", "jadav", "01-01-1111", "jadav@mail.com", 1111112222)


# In[20]:


user1.previleges.show_previleges()

