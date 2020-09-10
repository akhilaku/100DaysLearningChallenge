#!/usr/bin/env python
# coding: utf-8

# In[5]:


# IF, ELIF AND ELSE in python.

username = "akhildasks"
password = "akhildasks123"

input_username = str(input("Enter the username : "))
input_password = str(input("Enter the password : "))

if ((username == input_username) and (password == input_password)):
    print(f"Hello {username} your user login is Successfull")
else:
    print("your username or password is incorrect!!!")


# In[1]:


#TERNARY OPERATOR

# It is writing the IF and ELSE conditions in single line.

#QUESTION) if a person in your facebook is your friend he can direct message you else he cant.

if_friend = True     #if your FB friend then True or False
can_message = "Direct Message Allowed" if if_friend else "Message not alowed"
print(can_message)


# In[13]:


# LOGICAL OPERATORS   < , > , == , != or , and, <=, >=

print(4 > 5)

print(4 < 5)

print(4 == 5)

print(4 != 5)

a = 5
b = 10

if(a is not b):
    print("True")


# In[20]:


# EXERCISE 65.

is_magician = True
is_expert = False


if( is_magician and is_expert):
    print("You are a master magician")
elif((is_magician == True) and (is_expert == False)):
    print("Atleast you are getting there")
else:
    print("You need magic powers")
    
    
#completed and perfect answer :)


# In[23]:


# just for fun checking silly things.....ie    "==" vs "is

#using "=="  equal checks for equality and finds whether it is True or False

print('' == 1)
print([] == [])
print(10 == 10.0)
print([] == 1)
print(True == 1)

# using "is"  

print('' is 1)
print([] is [])
print(10 is 10.0)
print([] is 1)
print(True is 1)


# In[1]:


# lOOPS

for i in ('AKHILDAS KS'):
    print(i)

print("<--------------------------------------------------------------->")


# In[2]:


for i in (1, 2, 3, 4, 5):
    for k in ["a", "b", "c"]:
        print(i, k)

print("<------------------------------------>")       
        
for j in range(1, 5):
    for h in ["a", "b", "c"]:
        print(j, h)


# In[19]:


user = {'001':"AKhil", '002':"hjsc", "003":"adks"}

for i in user.items():
    print(i)
    
print("<---------------------------------------------->")

for i in user.keys():
    print(i)
    
print("<---------------------------------------------->")

for i in user.values():
    print(i)
    
print("<==============================================>")

for i in user.items():
    keys, values = i
    print(keys, values)


# In[21]:


#EXERCISE Counter

my_list = [1,2,3,4,5,6,7,8,9,10]
counter = 0

for i in my_list:
    counter = counter + i
    print(counter)


# In[24]:


# Range()

i = 0
for i in range(10):
    i = i + 2
    print(i)

    
for k in range(5):
    print("Akhildas")
  
print("To print reverse")
i = 0
for i in range(10, 0 , -1):
    i = i + 2
    print(i)


# In[4]:


#enumerate()        it is used to print the characters along with the indexes

for i, name in enumerate('AKHILDAS KS'):
    print(i, name)


# In[5]:


i = 0
while (i < 5):
    print(i)   
    break                 #break statement is used to stop the crashing of program due to infinite loop.


# In[7]:


i = 0
while (i <= 10):
    print(i)
    i = i+1
print("Reached till 10")


# In[11]:


#Iterating a list using while loop

i = 0
list1 = [1, 2, 6, 10, 15]
while (i < len(list1)):
    print(list1[i])
    i = i + 1


# In[15]:


# To find Duplicates in a list using conditional statements 

My_List = [ 'a', 'b', 'c', 'd', 'a', 'a', 'b', 'a', 'c', 'b','e', 'f']

duplicates = []

for values in My_List:
    if My_List.count(values) > 1:
        if values not in duplicates:
            duplicates.append(values)
print(duplicates)


# In[19]:


#FUNCTIONS
#######################################################################


# In[ ]:




