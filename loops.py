#if loop
age = 20
if age >= 18:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")
is_logged_in = True
if is_logged_in:
    print("You are logged in")

score = 75
if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")

temperature = 22
if temperature > 30:
  print("It's hot outside!")
elif temperature > 20:
  print("It's warm outside")
elif temperature > 10:
  print("It's cool outside")
else:
  print("It's cold outside!")

username = "Emil"

if len(username) > 0:
  print(f"Welcome, {username}!")
else:
  print("Error: Username cannot be empty")
# short hand If
a = 5
b = 2
if a > b: print("a is greater than b")
print("a is greater than b") if a>b else print("a is greater than b")
bigger = a if a > b else b
print("Bigger is", bigger)
print("A") if a > b else print("=") if a == b else print("B")

username = "Tobias"
password = "secret123"
is_verified = True
if username and password and is_verified:
  print("Login successful")
else:
  print("Login failed")
#nested loops
age = 25
has_license = True
if age >= 18:
    if has_license:
      print("You can drive")
    else:
      print("You need a license")
else:
    print("You are too young to drive")

score = 62
attendance = 90
submitted = True
if score >= 60:
  if attendance >= 80:
    if submitted:
      print("Pass with good standing")
    else:
      print("Pass but missing assignment")
  else:
    print("Pass but low attendance")
else:
  print("Fail")
#pass usage can build code and logic later
value = 50

if value < 0:
  print("Negative value")
elif value == 0:
  pass # Zero case - no action needed
else:
  print("Positive value")

#match loop
month = 5
day = 5
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print(f"weekend in {month}")

#while loop

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
#for loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)

for x in range(6):
  print(x)
else:
  print("Finally finished!")

for x in range(6):
  print(x)
  if x == 3: break
else:
  print("Finally finished!")

for x in range(2,50,3):# 3 will be added to 2 and so on until 50
  print(x)