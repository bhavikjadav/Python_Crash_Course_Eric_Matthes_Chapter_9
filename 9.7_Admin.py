#!/usr/bin/env python
# coding: utf-8

# # 9-7. Admin: An administrator is a special kind of user. Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 (page 162) or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", and so on. Write a method called show_privileges() that lists the administrator’s set of privileges. Create an instance of Admin, and call your method.

# In[5]:


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
        
class Admin(User):
    """A class that inherits from User class."""
    
    def __init__(self, first_name, last_name, dob, email, phoneno):
        """a structure of Admin class."""
        super().__init__(first_name, last_name, dob, email, phoneno)
        self.previleges = ["can add post", "can delete post", "can block user", "can mute user", "can hide user"]
    
    def show_previleges(self):
        """A method that shows [revileges of a Admin."""
        print("Admin have following previleges : ")
        for previlege in self.previleges:
            print(previlege.title())


# In[6]:


user1 = Admin("bhavik", "jadav", "01-01-1111", "jadav@mail.com", 1111112222)


# In[7]:


user1.show_previleges()

