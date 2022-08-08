# There are four collection data types in Python :

# List: is a collection which is ordered and changeable(modifiable). Allows duplicate members.
# Tuple: is a collection which is ordered and unchangeable or unmodifiable(immutable). Allows duplicate members.
# Set: is a collection which is unordered, un-indexed and unmodifiable, but we can add new items to the set. Duplicate members are not allowed.
# Dictionary: is a collection which is unordered, changeable(modifiable) and indexed. No duplicate members.
# A list is collection of different data types which is ordered and modifiable(mutable). A list can be empty or it may have different data type items.


#Creating a List

from ntpath import join


lst = list()
empty_list = list()
list_with_values = list([1, 3 ,4 ,5, 'asd', True])

print(len(empty_list)) # 0
print(len(list_with_values)) # 6

lst = []
lst_with_values =  [1, 3, 5, True, 'asd']

fruits = ['banana', 'orange', 'mango', 'lemon']                     # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

# Print the lists and its length
print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal products:',animal_products)
print('Number of animal products:', len(animal_products))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
print('Countries:', countries)
print('Number of countries:', len(countries))

lst = ['Asabeneh', 250, True, {'country':'Finland', 'city':'Helsinki'}] # list containing different data types

#can be accessed with negative indexing
# Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item.
first_fruit = fruits[-4]
last_fruit = fruits[-1]
second_last = fruits[-2]
print(first_fruit)      # banana
print(last_fruit)       # lemon
print(second_last)      # mango

# unpacking
lst = ['item','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst # Destructuring!
print(first_item)     # item1
print(second_item)    # item2
print(third_item)     # item3
print(rest)           # ['item4', 'item5']

#Slicing items
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4] # it returns all the fruits
# this will also give the same result as the one above
all_fruits = fruits[0:] # if we don't set where to stop it takes all the rest
orange_and_mango = fruits[1:3] # it does not include the first index
orange_mango_lemon = fruits[1:]
orange_and_lemon = fruits[::2] # here we used a 3rd argument, step. It will take every 2cnd item - ['banana', 'mango']

#Negative indexing
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:] # it returns all the fruits
orange_and_mango = fruits[-3:-1] # it does not include the last index,['orange', 'mango']
orange_mango_lemon = fruits[-3:] # this will give starting from -3 to the end,['orange', 'mango', 'lemon']
reverse_fruits = fruits[::-1] # a negative step will take the list in reverse order,['lemon', 'mango', 'orange', 'banana']

#Lists are mutable!
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado'
print(fruits)       #  ['avocado', 'orange', 'mango', 'lemon']
fruits[1] = 'apple'
print(fruits)       #  ['avocado', 'apple', 'mango', 'lemon']
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits)        #  ['avocado', 'apple', 'mango', 'lime']

#checking if an item exists in list
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # True
does_exist = 'lime' in fruits
print(does_exist)  # False

#Adding items
# syntax
lst = list()
lst.append('hola')

#Inserting Items into a List
#We can use insert() method to insert a single item at a specified index in a list. Note that other items are shifted to the right. The insert() methods takes two arguments:index and an item to insert.

# syntax
lst = ['item1', 'item2']
lst.insert(1, 'item3')

print(lst)

#Removing items
# syntax
lst = ['item1', 'item2']
lst.remove('item2')

# The pop() method removes the specified index, (or the last item if index is not specified):
# syntax
lst = ['item1', 'item2']
lst.pop()       # last item
# lst.pop(index)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)       # ['banana', 'orange', 'mango']

fruits.pop(0)
print(fruits)       # ['orange', 'mango']

#The del keyword removes the specified index and it can also be used to delete items within index range. It can also delete the list completely
# syntax
lst = ['item1', 'item2']
# del lst[index] # only a single item
del lst        # to delete the list completely

#The clear() method empties the list:

# It is possible to copy a list by reassigning it to a new variable in the following way: 
# list2 = list1. Now, list2 is a reference of list1, any changes we make in list2 will also modify the original, list2. 
# But there are lots of case in which we do not like to modify the original instead we like to have a different copy. 
# One of way of avoiding the problem above is using copy().

# syntax
lst = ['item1', 'item2']
lst_copy = lst.copy()

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)       # ['banana', 'orange', 'mango', 'lemon']

# list3 = list1 + list2 Joins lists

#Counting items in a List
# The count() method returns the number of times an item appears in a list:
# syntax
# lst.count(item)

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))           # 3

#The index() method returns the index of an item in the list:
# syntax
# lst.index(item)
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))    

#The reverse() method reverses the order of a list.
# To sort lists we can use sort() method or sorted() built-in functions. 
# The sort() method reorders the list items in ascending order and modifies the original list. 
# If an argument of sort() method reverse is equal to true, it will arrange the list in descending order.
# syntax
lst = ['item1', 'item2']
lst.sort()                # ascending
lst.sort(reverse=True)    # descending

#Exercises
print('exercises')
#1
empty_list = list()
#2
list_with_more_than_five_items = [1, 2 ,3 ,4 ,5, 6, 7]
#3
print(len(list_with_more_than_five_items))
#4
middle = round(len(list_with_more_than_five_items) / 2)
print(list_with_more_than_five_items[0])
print(list_with_more_than_five_items[middle - 1])
print(list_with_more_than_five_items[-1])

#5
mixed_data_types = ['Camilo', 27, 1.83, 'Single', 'Envigado, Ant']

#6
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

#7
print(it_companies)

#8
print(len(it_companies))

#9
print(it_companies[0])
middle = round(len(it_companies) / 2)
print(it_companies[middle - 1])
print(it_companies[-1])

#10
it_companies[4] = 'Uber'
print(it_companies)

#11
it_companies.append('IBM')

#12
it_companies.insert(middle - 1, 'AirBnB')


#13
it_companies[0]= it_companies[0].upper()

#14
print('#;  '.join(it_companies))

#15
print('Apple' in it_companies)

#16
print(it_companies)
it_companies.sort()
print('=>', it_companies)

#17
it_companies.reverse()
print(it_companies)

#18
first, second, third, *rest = it_companies
print(it_companies[0:3])

#19
#Last 3 companies
print(it_companies[-3:])

#20
middle = len(it_companies) // 2
print(it_companies[middle])

#21
it_companies.pop(0)

#22
it_companies.pop(middle)

#23
del it_companies[-1]
print(it_companies)

#24
it_companies.clear()
print(it_companies)

#25
del it_companies

#26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

print(front_end + back_end)

#27
# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. 
# Then insert Python and SQL after Redux.

full_stack = front_end + back_end
index = full_stack.index('Redux') + 1
full_stack[index:index] = ['Python', 'SQL']

print(full_stack)


#Level2

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()

print(ages)

min, max = ages[0], ages[-1]
print(min, max)

middle = len(ages) // 2
print(ages[middle])

print(sum(ages) / len(ages))
print(max - min)

