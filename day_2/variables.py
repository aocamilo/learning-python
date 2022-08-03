# In Python we have lots of built-in functions. Built-in functions are globally available 
# for your use that mean you can make use of the built-in functions without importing or 
# configuring. Some of the most commonly used Python built-in functions are the following: 
# print(), len(), type(), int(), float(), str(), input(), list(), dict(), min(), max(), sum(),
#  sorted(), open(), file(), help(), and dir()

# help('keywords')
# help(str)
print(min(20, 30, 40, 50, 60, 1))
print(max(20, 30, 40, 50, 60, 1))
print(min([20, 30, 40, 50, 60, 1, 0]))
print(max([20, 30, 40, 50, 60, 1, 100]))
print(sum([20, 30, 40, 50, 60, 1, 100]))


# Python Variable Name Rules

# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (firstname, Firstname, FirstName and FIRSTNAME) are different variables)

name = 'Camilo'
last_name = 'Arango'
city = 'Envigado, Ant'
country = 'Colombia'
age = 27
married = False
nationalities = ['Colombian', 'American'] #Arrays (lists)
skills = {
  'JS': True,
  "React": True,
  False: True,
  27: 'Yes',
  "TS": True,
} # Hash maps (Dictionaries)

print(name, len(name))

first_name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)
print(age)

# Printing out types
print(type('Camilo'))     # str
print(type(first_name))     # str
print(type(10))             # int
print(type(3.14))           # float
print(type(1 + 1j))         # complex
print(type(True))           # bool
print(type([1, 2, 3, 4]))     # list
print(type({'name':'Asabeneh','age':250, 'is_married':250}))    # dict
print(type((1,2)))                                              # tuple
print(type(zip([1,2],[3,4])))                                   # set

#Casting to other data types
number = 10
print(str(number), type(str(number))) # 10 str

# int to float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int
gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int or float
num_str = '10.6'
print('num_int', int(float(num_str)))      # 10
print('num_float', float(num_str))  # 10.6

# str to list
first_name = 'Camilo'
print(first_name)               # 'Camilo'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']


# Exercises

first_name = 'Camilo'
last_name = 'Arango'
full_name = first_name + last_name
country = 'Colombia'
city = 'Envigado'
age = 27
year = 2022
is_married = False
is_true = True
is_light_on = False

sons_name, sons_age = 'Alejandro', 6

print(sons_name, sons_age)

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_light_on))

print(len(first_name))
print(len(last_name))
print(len(first_name) > len(last_name))
print(len(first_name) >= len(last_name))
print(len(first_name) == len(last_name))


num_one = 5 
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

print(total)
print(diff)
print(product)
print(division)
print(remainder)
print(exp)
print(floor_division)





