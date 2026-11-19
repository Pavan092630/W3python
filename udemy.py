import random

high = int(input("Enter a number of the range: "))
guess = 0
answer = random.randint(1, high)
print("enter a number between 1 and {}".format(high))
while guess != answer:
    guess = int(input("Enter a number of the range: "))
    if guess == 0:
        break
    if guess == answer:
        print("Correct")
        break
    else:
        if guess < answer:
            print("Your guess is too low")
        if guess > answer:
            print("Your guess is too high")