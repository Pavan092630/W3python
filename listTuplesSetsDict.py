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

