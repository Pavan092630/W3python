import sys
current_choice = "-"
choice = ["Computer",
          "Mouse",
          "Mouse Mat",
          "Keyboard",
          "HDMI Cable",
          "Monitor",
          "Finish The List"
          ]
valid_choices = [str(i) for i in range(1,len(choice)+1)]
computer_parts = []
while current_choice != str(choice.index("Finish The List")+1):
    if current_choice in valid_choices:
        print("adding {} ".format(choice[int(current_choice)-1]))
        if current_choice == str(choice.index("Computer")+1):
            computer_parts.append(choice[choice.index("Computer")])
        elif current_choice == str(choice.index("Mouse")+1):
            computer_parts.append(choice[choice.index("Mouse")])
        elif current_choice == str(choice.index("Mouse Mat")+1):
            computer_parts.append(choice[choice.index("Mouse Mat")])
        elif current_choice == str(choice.index("Keyboard")+1):
            computer_parts.append(choice[choice.index("Keyboard")])
        elif current_choice == str(choice.index("HDMI Cable")+11):
            computer_parts.append(choice[choice.index("HDMI Cable")])
        elif current_choice == str(choice.index("Monitor")):
            computer_parts.append(choice[choice.index("Monitor")])
    else:
         print("Please enter a valid choice.")
         for x in choice:
           print("{}: {}".format(choice.index(x) +1, x))
    current_choice = input("Please enter your choice: ")
print(computer_parts)
