import random
import time

print("🕵️‍♂️ WELCOME TO SECRET NUMBER SPY! 🕵️‍♂️")
print("I am thinking of a number between 1 and 20.")
secret_number = random.randint(1, 20)
attempts = 0

# The loop keeps going until they guess right
while True:
    guess = input("\nEnter your guess: ")

    # Catch empty inputs or typos
    if not guess.isdigit():
        print("🚨 Code Error! Please type a real number.")
        continue

    guess = int(guess)
    attempts += 1

    # Teach comparison conditions
    if guess < secret_number:
        print("📉 Too LOW! Aim higher, spy!")
    elif guess > secret_number:
        print("📈 Too HIGH! Drop down lower!")
    else:
        print(f"\n🎉 BOOM! You cracked the code in {attempts} tries!")
        print("🏆 Secret Agent Status: ACHIEVED! 🏆")
        break
