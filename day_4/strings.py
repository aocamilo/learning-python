letter = 'P'                # A string could be a single character or a bunch of texts
print(letter)               # P
print(len(letter))          # 1
greeting = 'Hello, World!'  # String could be made using a single or double quote,"Hello, World!"
print(greeting)             # Hello, World!
print(len(greeting))        # 13
sentence = "I hope you are enjoying 30 days of Python Challenge"
print(sentence)

multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)

# Another way of doing the same thing
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)

# In Python and other programming languages \ followed by a character is an escape sequence.\
# Let us see the most common escape characters:

# \n: new line
# \t: Tab means(8 spaces)
# \\: Back slash
# \': Single quote (')
# \": Double quote (")

print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # line break
print('Days\tTopics\tExercises') # adding tab space or 4 spaces 
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')
print('This is a backslash  symbol (\\)') # To write a backslash
print('In every programming language it starts with \"Hello, World!\"') # to write a double quote inside a single quote

# String formatting
# Old Style String Formatting (% Operator)
# In Python there are many ways of formatting strings. In this section, we will cover some of them. 
# The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list), 
# together with a format string, which contains normal text together with "argument specifiers", 
# special symbols like "%s", "%d", "%f", "%.number of digitsf".

# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# "%.number of digitsf" - Floating point numbers with fixed precision

# Strings only
first_name = 'Camilo'
last_name = 'Arango'
language = 'Python'
formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print(formated_string)

# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area) # 2 refers the 2 significant digits after the point

python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
formated_string = 'The following are python libraries:%s' % (python_libraries)
print(formated_string) # "The following are python libraries:['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']"

# New Style String Formatting (str.format)
# This formatting is introduced in Python version 3.

first_name = 'Camilo'
last_name = 'Arango'
language = 'Python'
formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
print(formated_string)
a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area) # 2 digits after decimal
print(formated_string)

# String Interpolation / f-Strings (Python 3.6+)
# Another new string formatting is string interpolation, f-strings. Strings start with f and we can inject 
# the data in their corresponding positions.

a = 4
b = 3
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

# Unpacking characters
language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n

# Accessing Characters in Strings by Index
# In programming counting starts from zero. Therefore the first letter of a string is at zero 
# index and the last letter of a string is the length of a string minus one.

language = 'Python'
first_letter = language[0]
print(first_letter) # P
second_letter = language[1]
print(second_letter) # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) # n

#Reversing a string
greeting = 'Hello, World!'
print(greeting[::-1]) # !dlroW ,olleH

# Skipping Characters While Slicing
# It is possible to skip characters while slicing by passing step argument to slice method.

language = 'Python'
pto = language[0:6:2] #
print(pto) # Pto

#String methods
# capitalize(): Converts the first character of the string to capital letter
# count(): returns occurrences of substring in string, count(substring, start=.., end=..). The start is a starting 
# indexing for counting and end is the last index to count.

challenge = 'thirty days of python'
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1, 
print(challenge.count('th')) # 2`

# endswith(): Checks if a string ends with a specified ending
challenge = 'thirty days of python'
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion')) # False

# expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(10)) # 'thirty    days      of        python'

#find(): Returns the index of the first occurrence of a substring, if not found returns -1
challenge = 'thirty days of python'
print(challenge.find('y'))  # 16
print(challenge.find('th')) # 17

#rfind(): Returns the index of the last occurrence of a substring, if not found returns -1
challenge = 'thirty days of python'
print(challenge.rfind('y'))  # 5
print(challenge.rfind('th')) # 1

#index(): Returns the lowest index of a substring, additional arguments indicate starting and ending index
#  (default 0 and string length - 1). If the substring is not found it raises a valueError.

# rindex(): Returns the highest index of a substring, additional arguments
#  indicate starting and ending index (default 0 and string length - 1)

# isalnum(): Checks alphanumeric character
# isalpha(): Checks if all string elements are alphabet characters (a-z and A-Z)
# isdecimal(): Checks if all characters in a string are decimal (0-9)
# isdigit(): Checks if all characters in a string are numbers (0-9 and some other unicode characters for numbers)
# isnumeric(): Checks if all characters in a string are numbers or number related (just like isdigit(), just accepts more symbols, like ½)

# isidentifier(): Checks for a valid identifier - it checks if a string is a valid variable name
challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True

# islower(): Checks if all alphabet characters in the string are lowercase
# isupper(): Checks if all alphabet characters in the string are uppercase

# join(): Returns a concatenated string
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'

# strip(): Removes all given characters starting from the beginning and end of the string
challenge = 'thirty days of pythoonnn'
print(challenge.strip('noth')) # 'irty days of py'

# replace(): Replaces substring with a given string
challenge = 'thirty days of python'
print(challenge.replace('python', 'coding')) # 'thirty days of coding'

# split(): Splits the string, using given string or space as a separator
challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']
challenge = 'thirty, days, of, python'
print(challenge.split(', ')) # ['thirty', 'days', 'of', 'python']

# startswith(): Checks if String Starts with the specified String

# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

print('Thirty' + 'Days' + 'Of' + 'Python')

# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.

print('Coding' + 'For' + 'All')

# Declare a variable named company and assign it to an initial value "Coding For All".

company = 'Coding For All'

# Print the variable company using print().

print(company)

# Print the length of the company string using len() method and print().

print(len(company))

# Change all the characters to uppercase letters using upper() method.

print(company.upper())

# Change all the characters to lowercase letters using lower() method.

print(company.lower())

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.

print(company.capitalize())

# Cut(slice) out the first word of Coding For All string.

print(company.split(" ")[0])
print(company[0:6])


# Check if Coding For All string contains a word Coding using the method index, find or other methods.

print(company.index('Coding') is 0)

# Replace the word coding in the string 'Coding For All' to Python.

print(company.replace("Coding", "Python"))

# Change Python for Everyone to Python for All using the replace method or other methods.

print(company.replace('All', 'Everyone'))

# Split the string 'Coding For All' using space as the separator (split()) .

print('Coding For All'.split(' '))

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.

print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(','))

# What is the character at index 0 in the string Coding For All.

print('Coding For All'[0] is 'C')

# What is the last index of the string Coding For All.

print('Coding For All'[-1] is 'l')

# What character is at index 10 in "Coding For All" string.

print('Coding For All'[10] is ' ')

# Create an acronym or an abbreviation for the name 'Python For Everyone'.

for val in 'Python For Everyone'.split(' '):
  print(val[0])

# Create an acronym or an abbreviation for the name 'Coding For All'.
print('\n')
for val in 'Coding For All'.split(' '):
  print(val[0])

# Use index to determine the position of the first occurrence of C in Coding For All.
print('\n')
print('Coding For All'.index('C') is 0)

# Use index to determine the position of the first occurrence of F in Coding For All.

print('Coding For All'.index('F') is 7 )

# Use rfind to determine the position of the last occurrence of l in Coding For All People.

print('Coding For All People'.rfind('l') is 19)

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

print('You cannot end a sentence with because because because is a conjunction'.index('because'))
print('You cannot end a sentence with because because because is a conjunction'.find('because'))

# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

print('You cannot end a sentence with because because because is a conjunction'.rindex('because'))

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

print('You cannot end a sentence with because because because is a conjunction'[0:31])

# Does ''Coding For All' start with a substring Coding?

print('Coding For All'.startswith('Coding'))

# Does 'Coding For All' end with a substring coding?

print('Coding For All'.endswith('coding'))

# '   Coding For All      '  , remove the left and right trailing spaces in the given string.

print('   Coding For All      ')
print('   Coding For All      '.strip())

# Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython -> Cant be a number at the start
# thirty_days_of_python = True

# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.

print('# '.join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))