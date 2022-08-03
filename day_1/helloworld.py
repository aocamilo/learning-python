# Introduction
# Day 1 - 30DaysOfPython Challenge

import math

print(2 + 3)   # addition(+)
print(3 - 1)   # substraction(-)
print(2 * 3)   # multiplication(*)
print(3 / 2)   # division(/)
print(3 ** 2)  # exponential(**)
print(3 % 2)   # modulus(%)
print(3 // 2)  # Floor division operator(//)

# Checking data types

print(type(10))                  # Int
print(type(3.14))                # Float
print(type(1 + 3j))              # Complex
print(type('Camilo'))          # String
print(type([1, 2, 3]))           # List
print(type({'name':'Camilo'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple

def euclidianDistance(p, q):
  return abs(p-q)

def euclidianDistance2D(p1, p2, q1, q2):
  return math.sqrt(pow(q1 - p1, 2) + pow(q2 - p2, 2))


print(euclidianDistance(6, 10))
print(euclidianDistance2D(2, 3, 10, 8))