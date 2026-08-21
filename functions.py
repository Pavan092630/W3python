def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9
def printing (n):
    message = fahrenheit_to_celsius(n)
    return message
print(printing(77))
print(printing(95))
print(printing(50))

def my_function(country = "Norway"):
  print("I am from", country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")

def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)

def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function(my_person)

def my_function(x, y):
    return x + y
result = my_function(10, 50)
print(result)

#Combining Positional-Only and Keyword-Only
#You can combine both argument types in the same function.
#Arguments before / are positional-only, and arguments after * are keyword-only:

def my_function(x, y,/,*,z,a):
    return x + y + z + a
result = my_function(5,10,z =10,a = 15)
print(result)

#What is *args?
#The *args parameter allows a function to accept any number of positional arguments.
#Inside the function, args becomes a tuple containing all the passed arguments:

def my_function(*args):
    print("Type: ", type(args))
    for arg in args:
        print(f"Number {args.index(arg)+1} is {arg}")

my_function("emily","Aarav","Krishna","Surekha")

def my_function(*numbers):
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number
result = my_function(30,50,80,90)
print(result)

#What is **kwargs?
#The **kwargs parameter allows a function to accept any number of keyword arguments.
#Inside the function, kwargs becomes a dictionary containing all the keyword arguments:

def my_function(username, **details):
  print("Username:", username)
  print(type(details))
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)

my_function("emil123", age = 25, city = "Oslo", hobby = "coding")
#unpacking using *args and **kwargs
def my_function(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person) # Same as: my_function(fname="Emil", lname="Refsnes")

def my_function(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers) # Same as: my_function(1, 2, 3)
print(result)
#scope of variables in function
x = "global"

def outer():
  x = "enclosing"
  def inner():
    x = "local"
    print("Inner:", x)
  inner()
  print("Outer:", x)
outer()
print("Global:", x)

#decorators
#Decorators let you add extra behavior to a function, without changing the function's code.
#A decorator is a function that takes another function as input and returns a new function.
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

@changecase
def otherfunction():
  return "I am speed!"

print(myfunction())
print(otherfunction())

#with Arguments
def changecase(func):
  def myinner(x):
    return func(x).upper()
  return myinner

@changecase
def myfunction(nam):
  return "Hello " + nam

print(myfunction("John"))

