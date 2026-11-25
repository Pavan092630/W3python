current_choice = "-"
choice = ["Computer",
          "Mouse",
          "Mouse Mat",
          "Keyboard",
          "HDMI Cable",
          "Monitor",
          "Computer Table",
          "Finish The List"
          ]
valid_choices = [str(i) for i in range(1,len(choice)+1)]
computer_parts = []
while current_choice != str(choice.index("Finish The List")+1):
    if current_choice in valid_choices:
        print("adding {} ".format(choice[int(current_choice)-1]))
        computer_parts.append(choice[int(current_choice)-1])
    else:
         print("Please enter a valid choice.")
         for x in choice:
           print("{}: {}".format(choice.index(x) +1, x))
    current_choice = input("Please enter your choice: ")
print(computer_parts)
