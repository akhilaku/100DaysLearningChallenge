#!/usr/bin/env python
# coding: utf-8

# In[6]:


# In this Pynb file it consists of variables and Data-Types










#assigning variable

iq = 100
user_age = iq / 5
print(user_age)


# In[9]:


#augmented assignment operator 

some_value = 5
some_value += 3
print(some_value)

some_value -= 2
print(some_value)

some_value = some_value * 2
print(some_value)


# In[15]:


#Strings

#we can use double or single quatation marks for the single line string.

a = "Hello world"
b = "Iam Akhil"

#for printing long strings (strings with multiple lines) we use triple quatation marks.

long_string = '''

WoW
0 0
---
'''

print(a)
print(b)
print(long_string)

first_name = "Akhildas"
last_name = "KS"
full_name = first_name + ' ' + last_name
print(full_name)



#String Concatenation

#type conversion

c = str(100)
d = int(c)
e = type(d)
print(e)


# In[25]:


#Escape Sequence

weather = " It's a \"Kind of\" sunny" #to print sentence with double quotes and single quotes inside it. So we have to separate it with "\".
print(weather)

#to print a sentence in new line
print(weather + ' ' + "\n have a good day")


# In[34]:


#Formated String

name = "Akhil"
age = 21
print('hi ' + name + ' ' + "you are "+ str(age) +' ' + "years old :)") #you have to convert int to str while printing.

#instead of this long procedure we can do it in simpler way

# f denotes it is a formated string.

print(f'hi {name} you are {age} years old :)')  #you no need to convert int to str while printing.


# In[42]:


#String Indexes
name1 = "AKHILDAS KS"

#Indexes [starting index : Ending Index]

print(name1[0:5])
print(name1[5:11])

#Step over [providing gaps between the indexes.]
#that is [starting : ending : gaps]
#example

name2 = "0123456789"
print(name2[0:11:1])
print(name2[0:11:2])
print(name2[0:11:3])

# Reversing of string using indexes stepover methode

print(name2[::-1]) #leaving the starting and ending point blank and giving the Step Over "-1" will give reversed string.


# In[43]:


#string immutability

#strings in python are immutable. once it is declared we cannot change it other than modifying it.

#example

name3 = "AKHILDAS"
name3 = name3 + " KS"
print(name3)


# In[9]:


#Built-in functions

#len
string1 = "hey how are you?"
print(len(string1))              #len function is used to find the length of the string

#to convert to CAPITAL letters

print(string1.upper())

#to convert to small letters

print(string1.lower())

#capitalize this help to capitalize the first letter of the sentence.

print(string1.capitalize())

#find help to find the letter or word in a string.

print(string1.find("are"))

#replace helps to replace the term.

string1 = string1.replace("are", "is")

print(string1)


# In[13]:


#Exercise

birth_year = int(input("Enter your birth year:"))
print(f"Your birth year is {birth_year}")

age = 2020 - birth_year

print(f"your age is {age}")


# In[1]:


#Exercise Password Checker

#username = str(input("Enter your username : "))
#password = str(input("Enter your password : "))

#length = len(password)
#numbers = length * "*"

#print(f"Hey {username} your password {numbers} is {length} digits long")


#practising it again

Username = str(input("Enter the user name : "))
Password = str(input("Enter the password :"))
length_of_password = len(Password)
number_of_digit = length_of_password * "*"
print(f"Hey {Username} your password {number_of_digit} is {length_of_password} digits long")


# In[3]:


#Lists - it is an ordered sequence of objects.

#Examples:

list1 = [1, 2, 3, 4, 5]
print(list1)

list2 = ['a', 'b', 'c', 'd', 'e']
print(list2)

list3 = [1, 2, 3, "akhil", True, "akkhi"] #even boolean can be printed if it is inside an list
print(list3)
    
print(list1[3])
print(list2[4])
print(list3[0:]) #we can print or access an elements in a list using indexes.


# In[2]:


#List Slicing 

amazon = ["books", "sunglasses", "toys", "gadgets", "perfumes", "mens wears", "pulses"]

print(amazon)
print(amazon[0:3])
print(amazon[::2])

#Lists are mutable.

#let us replace the "books" with "laptops"

amazon[0] = "laptops"
print(amazon)          #it will replace books by laptops.

#Creating a new List from an another list.

new_amazon = amazon[:]   
new_amazon[2] = "Avengers Toys"
print(amazon)
print(new_amazon)
new_amazon.insert('toys', 'games')
print(new_amazon)


# In[33]:


#Matrix

matrix1 = [
    [1, 2, 3],
    [3, 5, 9],
    [10, 0, 1]
]

print(matrix1)
print(matrix1[0][2]) #in this [0] index denotes the 1st row ie. [1, 2, 3] and [2 denotes the 2nd element in it ie. 3]


# In[2]:


# Methods in Lists

# append() it is used to add an object into an list or array.

mylist = [1, 24, 23, 4, 26]
print(mylist)

mylist.append(100)
print(mylist)



# insert() it is used to insert a object to any place in a list or array.

mylist.insert(23, 6)  #inserting a new object 6 after 1.
print(mylist)



# extend() it is used to extend a list.

mylist.extend([101, 102]) 
print(mylist)



# remove() and pop()

#for removing an element from a list we use pop().

mylist.pop()   #it will remove the last object from the list (or) we can give the index of the element which to be removed.
print(mylist)

mylist.remove(23) # remove() will remove the object which we want to remove from our list without using the index.
print(mylist)


mylist.insert(4,1999)
print(mylist)

mylist.insert(6,7)
print(mylist)
# Clear() 
# it will remove everything inside a list.

mylist.clear()
print(mylist)




# In[6]:


# List Methods

#list Index - it is used to find the index of an element in a list.

list5 = ['books', 'sunglasses', 'toys', 'gadgets', 'perfumes']
print(list5.index('toys'))

# IN keyword.

print('sunglasses' in list5)  #if the sunglasses is present in list5 it will print TRUE
print('Apple' in list5) 


# In[16]:


# Count()

list6 = [1, 2, 3, 1, 2, 1, 1, 2, 3, 5, 1]

print(list6.count(1))  #it will count how many "1" is present in the list.

# Sort() it helps to sort the list

list6.sort()
print(list6)

# Reversing the lists
print(list6[::-1]) 
#or
list6.reverse()
print(list6)


# In[6]:


# Creating a list with range()   eg... range(start, n-1).


list7 = list(range(0, 20))   
print(list7)


# In[8]:


# Converting a list into a String.

list8 = ['hey', 'how', 'are', 'you', 'doing?']
print( ' '.join(list8))                            # ' '.join(list_name) will help to convert a list into string.


# In[15]:


#List Unpacking    this is used to assign variables for the elements present in the list.

a,b,c,d,e = ['hey', 'how', 'are', 'you', 'doing?']
print(a)
print(b)
print(c)
print(d)
print(e)

#just printing the required variables and keeping others in the list itself
print("<-------------------------------------------------------------------------->")

a,b, *others = ['hey', 'how', 'are', 'you', 'doing?']     #a,b,c,  then giving a space then adding a '*' and giving a variable name will print the other remaining variables as a list itself.
print(a)
print(b)

print(others)

print("<------------------------------------------------------------------------->")

a,b, *others,d  = ['hey', 'how', 'are', 'you', 'doing?'] 
print(a)
print(b)
print(others)
print(d)


# In[5]:


# Dictionaries or dict or {"key" : value}

dictionary = {"a": 1, "b": 2, "c": 3, "d": 4, "e":5 }
print(dictionary)
print(dictionary['d'] )                                 

print("<-------------------------------------------------->")

print("Dictionary is a UnOrdered data collection")

dictionary2 = {"a" : [1,2,3], "b" : "Stringsss", "c" : True}  #Dictionary consists of all types of data types
print(dictionary2)


# In[ ]:




