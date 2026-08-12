import sys
import random

print(sys.version)
print("Hello World")
#Semicolons are optional in Python.
#You can write multiple statements on one line by separating them with ; but this is rarely used because it makes it hard to read


#variables
x = 5
y = "John"
z = True
a = 3.5

# Casting variables
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
a = bool(True)
print(a)
print(x)
print(y)
print(z)

#You can get the data type of a variable with the type() function
print(type(a))
print(type(z))
print(type(x))
print(type(y))

#String variables can be declared either by using single or double quotes:
#Variable names are case-sensitive.

#Types of casing in variable names
myVariableName = "John"  #camelCase
MyVariableName = "John"  #PascalCase
my_variable_name = "John"#snakeCase

#Assigning multiple variables
x, y, z = "Orange", "Banana", "Cherry"
x = y = z = "Orange" #one value to all variables
fruits = ["apple", "banana", "cherry"]# we can unpack list using this assign methods
x, y, z = fruits
print(x, y, z) #output the variables

#global variables
# that are created outside a function are known as global variables.
#Global variables can be used by everyone, both inside of functions and outside.
x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc()

#If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function.
# The global variable with the same name will remain as it was, global and with the original value.
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)

# Using global keyword to create global variable inside the function
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)

#Datatypes
x = "Hello World"	#str
print(type(x))

x = 20	#int
print(type(x))

x = 20.5	#float
print(type(x))

x = 1j	#complex
print(type(x))

x = ["apple", "banana", "cherry"]	#list
print(type(x))

x = ("apple", "banana", "cherry")	#tuple
print(type(x))

x = range(6)	#range
print(type(x))

x = {"name" : "John", "age" : 36}	#dict
print(type(x))

x = {"apple", "banana", "cherry"}	#set
print(type(x))

x = frozenset({"apple", "banana", "cherry"})	#frozenset
print(type(x))

x = True	#bool
print(type(x))

x = b"Hello"	#bytes
print(type(x))

x = bytearray(5)	#bytearray
print(type(x))

x = memoryview(bytes(5))	#memoryview
print(type(x))

x = None	#NoneType
print(type(x))

# Using random function
print(random.randrange(1, 10))

#Strings and its functions
#it is ok to use quotes as long as they dont match with surroundings
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

#multiline string allocation
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.""" # can also use single three qoutes
print(a)

#Strings are arrays
print(a[1])

#loop through a string
b = "Banana"
for x in b:
  print(x)

  print(len(b)) # finding length of string
  print( "ipsum" in a)# Return if true or false and can also use print( "ipsum" not in a)
  print("ipsum" not in a)

  #Using if else statement using string
  if "ipsum" in a:
      print("Yes , ipsum present in a ")
  else:
      print("Yes , ipsum not present in a ")

  if "ipsum" not in a:
      print("yes , ipsum present not in a ")
  else:
      print("yes , ipsum present in a ")

      #Slicing of Strings
      b = "Hello, World!"
      print(b[2:5])# 5 not included
      print(b[:5]) # start to 5
      print(b[2:]) # 2 until last
      print(b[-5:-2]) # -5 not included
      print(b[-8:-5]) # -8 not included

      #Modify Strings

      print(b.upper())
      print(b.lower())
      a = " Hello, World! "
      print(a.strip())  # returns "Hello, World!"
      print(a.replace("H", "J"))
