# A tuple is a collection of different data types which is ordered and unchangeable (immutable). 
# Tuples are written with round brackets, (). Once a tuple is created, we cannot change its values. 
# We cannot use add, insert, remove methods in a tuple because it is not modifiable (mutable). Unlike list, 
# tuple has few methods. Methods related to tuples:

# tuple(): to create an empty tuple
# count(): to count the number of a specified item in a tuple
# index(): to find the index of a specified item in a tuple
# operator: to join two or more tuples and to create a new tuple

#Creating a tuple
# syntax
empty_tuple = ()
# or using the tuple constructor
empty_tuple = tuple()

#With initial values
# syntax
tpl = ('Camilo', 27, True)

#length
len(tpl)

#accesing
#positive indexing
tpl[0] #Camilo
tpl[2] #True

#Negative indexing
tpl[-1] #True
tpl[-2] #27
tpl[-3] #Camilo

#Slicing
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[0:4]         # all items
all_items = tpl[0:]         # all items
middle_two_items = tpl[1:3]  # middle two items

print(middle_two_items)

#Chaning tuples to lists
lst = list(tpl)

#Checking items in tuple
print('Camilo' in tpl)

fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits) # True
print('apple' in fruits) # False
# fruits[0] = 'apple' # TypeError: 'tuple' object does not support item assignment

#Joining tuples
# syntax
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5','item6')
tpl3 = tpl1 + tpl2

#Deleting tuples
# syntax
tpl1 = ('item1', 'item2', 'item3')
del tpl1

#Exercises lvl 1
empty_tuple = ()

siblings = ('Alejandro', 'Macarena')

family_tuple = ('Camilo', 'Manuela')

full_family = family_tuple + siblings

print(full_family, len(full_family))

