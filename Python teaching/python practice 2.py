#!/usr/bin/env python
# coding: utf-8

# In[24]:


Dictionary = {"hello": [1, 2, 3], "hi": "1,2,3"}
print(Dictionary["hello"])
print(Dictionary.get('age'))   # get.[] it is used to avoid error when we search a key which is not present in a dictionary.

print("hello" in Dictionary.keys())
print('1,2,3' in Dictionary.values())
print(Dictionary.items())
print("hello" in Dictionary.items())

Dictionary1 = {"hello": [1, 2, 3], "hi": "1,2,3"}
Dictionary1.clear()    #to make a dictionary empty.
print(Dictionary1)   

print(len(Dictionary))

print(Dictionary.update({'hiii': '55'}))   #used to modify a Dictionary
print(Dictionary)


# In[34]:


my_list = [1, 2, 3, 4, 5]
my_list[3] = 6
print(my_list)

my_list2 = [3, 5, 1, 99, 10, 100, 1, 2, 5, 20, 90]
my_list2.sort()
print(my_list2)
length = len(my_list2)
print(length)
mid = length//2
print(mid)


# In[39]:


my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

new_tuple = my_tuple[:]
print(new_tuple)

print(new_tuple.count(3))
print(new_tuple.index(3))


# In[14]:


#SETS           importand part

my_set = {1, 2, 3, 4}
my_set.add(5)
print(my_set)


# In[23]:


#removing the repeating elements present in a list using SETs method.

list1 = [1, 1, 3, 2, 5, 1, 9, 8, 7, 6, 5, 1, 9]

list1.sort()
print(list1)

my_set1 = set(list1[:])
print(my_set1)

print(list(my_set1))


# In[31]:


my_set3 = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}

print(my_set.union(your_set))          # .union() is used to join two sets

print(my_set.difference(your_set))     # .differenece() prints the difference between set1 and set2.

print(my_set.intersection(your_set))   # .intersection()  or "&" is used to find the intersection elements.
print(my_set & your_set)

print(my_set.isdisjoint(your_set))     # used to find whether there the both sets are joint or not

print(my_set | your_set)               # | or .union() is used to union the set

print(my_set.difference_update(your_set))
print(my_set)                                    #it is used to remove the common elements present in set1 or in set2.


# In[30]:


set1 = {4, 5}
set2 = {4, 5, 6, 7}

print(set1.issubset(set2))            # .issubset() is used to check whether the set1 is a subset of set2.
print(set2.superset(set1)             # set2 contains all the elements of set1, so ,superset() is used to check whether the set2 is a superset.


# In[ ]:




