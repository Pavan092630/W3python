#lists and their properties
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["apple", "banana", "cherry",45 , 68, True]
print(list1)
print(list2)
print(list3)
print(list4)
print(len(list1))
print(type(list4))
thislist = list(("apple", "Banana", "cherry")) # note the double round-brackets using list constructor
print(thislist)
thislist1 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist1[2])
print(thislist1[2:5])
print(thislist1[:2])
print(thislist1[2:])
if "apple" in thislist1:
  print("Yes, 'apple' is in the fruits list")

thislist1[1:3] = ["apple", "banana", "cherry"]
print(thislist1)

thislist1.insert(3,"watermelon") # insert () method
print(thislist1)



thislist1.append("Raspberry")#append adds at the last
print(thislist1)

tropical = ["mango", "pineapple", "papaya"]
thislist1.extend(tropical) #extend can add the other list at the end of the list it appended to
print(thislist1) #The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
thistuple = ("apple", "banana", "cherry")
thislist1.extend(thistuple)
print(thislist1)
thislist1.remove("banana")
#The remove() method removes the specified item.
print(thislist1)
thislist1.pop(1)
thislist1.pop()# removes last item
print(thislist1)
del thislist1[3]
print(thislist1)
#thislist1.clear() will clear all list
print(thislist1)
#del thislist1 will delete whole list
for x in thislist1:
 print(x)
for i in range(len(thislist1)):
 print(i)
i=0
while i<len(thislist1):
  print(thislist1[i])
  i=i+1
[print(x) for x in thislist1]
#comprehension in lists
newlist = []
for x in thislist1:
  if "a" in x:
    newlist.append(x)
print(newlist)
# different apprehending
newlist1 = [x for x in thislist1 if "a" in x]
print(newlist1)

newlist2 = [x for x in range(10)]
print(newlist2)

newlist3 = [x.upper() for x in thislist1]
print(newlist3)

newlist4 = ["Aarav" for x in thislist1]
print(newlist4)

newlist5 = [x if x!= "apple" else "Aarav" for x in thislist1]
print(newlist5)

def aarav(thislist1):
  for x in thislist1:
    print(x)
aarav(thislist1)
aarav(newlist5)
thislist1.sort()
print(thislist1)
thislist1.sort(reverse=True)
print(thislist1)

def myfunc(n):
  return abs(n - 50)

thislist2 = [100, 50, 65, 82, 23]
thislist2.sort(key = myfunc)
print(thislist2)
thislist.sort()
print(thislist)
thislist.sort(key = str.lower)
print(thislist)
#copy of list
mylist1 = thislist1.copy()
print(mylist1)
mylist2 = list(thislist1)
print(mylist1)
mylist3 = list(thislist1[0:4])
print(mylist3)

#joining of list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

for x in list1:
    list2.append(x)
print(list2)

list1.extend(list2)
print(list1)
""" append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list """

#tulips
#A tuple is a collection which is ordered and unchangeable and allow duplicate values.
#Tuples can also be created without the parentheses.
#Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
myTuple = ("apple", "banana", "cherry")
print(myTuple)
print(type(myTuple))
print(len(myTuple))

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple it will be considered string
thistuple = ("apple")
print(type(thistuple))
#CONSTRUCTOR OF TUPLE
tuple1 = tuple(("abc", 34, True, 40, "male"))
print(tuple1)
# Adding to tuple
x = list(myTuple)
x.append("orange")
myTuple = tuple(x)
print(myTuple)

#adding two tuples
#myTuple +=tuple1
#print(myTuple)
# you can change tuple to list and delete item or delete it entirely
del tuple1
#unpacking the tuple with variable names
(red, green, *blue) = myTuple
print(red)
print(green)
print(blue)
#loops in tuples
for x in myTuple:
    print(x)

for i in range(len(myTuple)):
    print(i)
    print(myTuple[i])

i=0
while i<len(myTuple):
    print(myTuple[i])
    i=i+1
 #adding the tuples
tuple2 = myTuple*3
print(tuple2)
#count()	Returns the number of times a specified value occurs in a tuple
#index()	Searches the tuple for a specified value and returns the position of where it was found

# sets in python
#A set is a collection which is unordered, unchangeable*, and unindexed.
#Set items are unordered, unchangeable, and do not allow duplicate values.
#Unordered means that the items in a set do not have a defined order.
#Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
#et items are unchangeable, meaning that we cannot change the items after the set has been created.

mySet = set(("apple", "banana", "cherry",True,1, 5, 0, False))
print(mySet)
print(type(mySet))
print(len(mySet))
print("banana" in mySet)
print("banana" not in mySet)
for x in mySet:
    print(x)
# Adding to set
mySet.add("orange")
print(mySet)
tropical = {"pineapple", "mango", "papaya"}
# update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
mySet.update(tropical)
print(mySet)
#removing items from set
mySet.remove("pineapple")
print(mySet)
mySet.discard("mango")
print(mySet)
#pop() delete random member in the set
x = mySet.pop()
print(x)
print(mySet)
#mySet.clear() will clear the set and make it empty
#del mySet will delete the whole set
"""Method	Shortcut	Description
add()	 	Adds an element to the set
clear()	 	Removes all the elements from the set
copy()	 	Returns a copy of the set
difference()	-	Returns a set containing the difference between two or more sets
difference_update()	-=	Removes the items in this set that are also included in another, specified set
discard()	 	Remove the specified item
intersection()	&	Returns a set, that is the intersection of two other sets
intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	 	Returns True if NO items of this set is present in another set
issubset()	<=	Returns True if all items of this set is present in another set
 	<	Returns True if all items of this set is present in another, larger set
issuperset()	>=	Returns True if all items of another set is present in this set
 	>	Returns True if all items of another, smaller set is present in this set
pop()	 	Removes an element from the set
remove()	 	Removes the specified element
symmetric_difference()	^	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
union()	|	Return a set containing the union of sets
update()	|=	Update the set with the union of this set and others """
#The union() method allows you to join a set with other data types, like lists or tuples.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
#myset = set1 | set2 | set3 |set4 can also be done through this
myset1 = set1.union(set2, set3, set4)
print(myset1)
#The update() method inserts all items from one set into another.
#The update() changes the original set, and does not return a new set.
set1.update(set2, set3, set4)
print(set1)
#The intersection() method will return a new set, that only contains the items that are present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
#set3 = set1 & set2 this can also be used for the intersection.
set5 = set1.intersection(set2)
print(set5)
set1.intersection_update(set2)
print(set1)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
#The difference() method will return a new set that will contain only
# the items from the first set that are not present in the other set.
set3 = set1.difference(set2)
#set3 = set1 - set2 also can be used
print(set3)
set1.difference_update(set2)
print(set1)
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
#set3 = set1 ^ set2 can also be used
print(set3)
set1.symmetric_difference_update(set2)
print(set1)

#frozenset is an immutable version of a set.
#Like sets, it contains unique, unordered, unchangeable elements.
#Unlike sets, elements cannot be added or removed from a frozenset.
froze = frozenset({"apple", "banana", "cherry"})
print(froze)
print(type(froze))
froze1 = froze.copy()
print(froze1)
#methods of frozen set
"""copy()	 	Returns a shallow copy	
difference()	-	Returns a new frozenset with the difference	
intersection()	&	Returns a new frozenset with the intersection	
isdisjoint()	 	Returns True if there is NO intersection between two frozensets	
issubset()	<= / <	Returns True if this frozenset is a (proper) subset of another	
issuperset()	>= / >	Returns True if this frozenset is a (proper) superset of another	
symmetric_difference()	^	Returns a new frozenset with the symmetric differences	
union()	|	Returns a new frozenset containing the union"""

#Python Dictionaries
#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
mydict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year":2020,
  "colors": ["red", "white", "blue"]
}
print(mydict)
print(type(mydict))
print(mydict["brand"])
print(len(mydict))
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
"""There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members."""
x = mydict.get("model")
print(x)
x = mydict.keys()
print(x)
x = mydict.values()
print(x)
x = mydict.items()
print(x)
mydict["year"] = 2021
print(mydict)
if "model" in mydict:
  print("Yes, model is in dict")
#The update() method will update the dictionary with the items from the given argument.
#The argument must be a dictionary, or an iterable object with key:value pairs.
mydict.update({"year": 2022})
print(mydict)
mydict["name"] = "explorer"
print(mydict)
mydict.pop("model")
print(mydict)
mydict.popitem()
print(mydict)
mydict.update({"model": "ford"})
print(mydict)
del mydict["model"]
print(mydict)
# del mydict can delete the whole thing
# mydict.clear() clear the whole dict
# loop through the dict
for x in mydict:
    print(x)
for x in mydict.values():
    print(x)
for x,y in mydict.items():
    print(x,y)
for x in mydict.keys():
    print(x)
"""You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1,
 and changes made in dict1 will automatically also be made in dict2.
There are ways to make a copy, one way is to use the built-in Dictionary method copy()."""
mydict1 = mydict.copy()
print(mydict1)

#Another way to make a copy is to use the built-in function dict()
mydict2 = dict(mydict1)
print(mydict2)

#Nested Dictionaries
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)
print(myfamily["child2"]["name"])
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])
"""clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary"""