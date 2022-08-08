# Set is a collection of items. Let me take you back to your elementary or high 
# school Mathematics lesson. The Mathematics definition of a set can be applied 
# also in Python. Set is a collection of unordered and un-indexed distinct elements. 
# In Python set is used to store unique items, and it is possible to find the union, \
# intersection, difference, symmetric difference, subset, super set and disjoint 
# set among sets.

# syntax
st = {} #Can be a dictionary too so its better to use Set()
# or
st = set()

#Creating a set with initial items
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
fruits = {'banana', 'orange', 'mango', 'lemon'}

#length
print(len(fruits))

#To access items inside a set we have to loop over them

#checking items
print('item1' in st)
print('banana' in fruits)

#Adding items (only a single item)
fruits.add('watermelon')
print(fruits)

#Adding multiple items
fruits.update(['papaya', 'berry'])
print(fruits)

#Can pass a list of elements list or tuple
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)

print(fruits)

#removing items
fruits.remove('tomato')

#clearing set
fruits.clear()

#deleting set
del fruits

#We can remove an item from a set using remove() method. 
# If the item is not found remove() method will raise errors, 
# so it is good to check if the item exist in the given set. 
# However, discard() method doesn't raise any errors.

#Converting List to Set
# syntax
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)  # {'item2', 'item4', 'item1', 'item3'} - the order is random, because sets in general are unordered

print(st)

#Joining sets
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)

#Intersection
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2) # {'item3', 'item2'}

#Difference
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1) # set()
st1.difference(st2) # {'item1', 'item4'} => st1\st2

#Symmetric Difference
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# it means (A\B)∪(B\A)
st2.symmetric_difference(st1) # {'item1', 'item4'}

#Exercises
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))

it_companies.add('Twitter')

it_companies.update(['AirBnB', 'Uber'])

it_companies.remove('IBM')

#Discard doesn't raise any error if the element does not exist inside the set

print(A.union(B))
print(A.intersection(B))

word_set = set('I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.'.split())

print(word_set)