print("Please choose one of the following options:")
options = ["1. Learn python", "2. Learn Java", "3. Watch Movie", "4. Play With Son", "0. Exit"]

while True:
    for option in options:
        print(option)
    choice = input("Enter your choice: ")
    if choice == "1":
     print("You chose to learn python glad you are interested in python")
     break
    elif choice == "2":
      print("You chose to learn Java glad you are interested in java")
      break
    elif choice == "3":
      print("You choose to watch movie glad you are interested in watch movie")
      break
    elif choice == "4":
      print("You choose to play with son glad you are interested in soccer with son")
      break
    elif choice == "0":
      print("You choose to exit")
      break
    else:
     print("Please choose one of the following options:")

