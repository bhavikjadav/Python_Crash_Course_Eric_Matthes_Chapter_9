#!/usr/bin/env python
# coding: utf-8

# # 9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3 (page 162). Write a method called increment_login _attempts() that increments the value of login_attempts by 1. Write another method called reset_login_attempts() that resets the value of login_attempts to 0.
# # Make an instance of the User class and call increment_login_attempts() several times. Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.

# In[4]:


class User:
    """A class that related to the user."""
    
    def __init__(self, first_name, last_name, dob, email, phoneno):
        """A default method which accepts arguments for class User()."""
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.email = email
        self.phoneno = phoneno
        self.login_attempts = 0
        
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
    
    def increment_login_attempts(self, attempts):
        """A method which increment attempts."""
        self.login_attempts += attempts
        print(f"Login Attempts : {self.login_attempts}")
    
    def reset_login_attempts(self):
        """A method which resets the login attempts."""
        self.login_attempts = 0
        print(f"Login ateempts successfully reseted.")


# In[5]:


user1 = User("bhavik", "jadav", "18-11-2001", "jadav@bcj.com", 1231231231)


# In[6]:


user1.increment_login_attempts(1)


# In[7]:


user1.increment_login_attempts(1)


# In[8]:


user1.increment_login_attempts(1)


# In[9]:


user1.reset_login_attempts()


# In[10]:


user1.login_attempts # To verify that the attempts are reseted or not.

