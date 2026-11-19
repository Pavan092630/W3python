low = int(input("Enter a number of the low range: "))
high = int(input("Enter a number of the high range: "))
print("guessing your  number between {} and {}".format(low, high))
input("Think of your number Press Enter to continue...")
guesses = 0
while True:
    guesses += 1
    guess = low + (high - low) // 2
    if high == low:
        print("I am sure {} is your number and i guessed in {} guesses".format(low, guesses))
        break
    #print("Guess between {} and {}".format(low, high))
    print("My guess is  {}".format(guess))
    answer = input("Enter h for higher, l for lower, c for correct").casefold()
    if answer == "c":
      print("I guessed in {} guesses".format(guesses))
      break
    elif answer == "h":
      low = guess+1
    elif answer == "l":
        high = guess-1
    else:
        print("Please enter a h, l or c")