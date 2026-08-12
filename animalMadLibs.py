import time

# --- STEP 1: Game Introduction ---
print("====================================")
print(" 🐾 WELCOME TO ANIMAL MAD LIBS! 🐾")
print("====================================")
print("Give me some words, and I will write a silly story!\n")

# --- STEP 2: The Kid's Input Zone (Variables) ---
# Teach Variables: Explain that these boxes hold onto words like a treasure chest.
animal = input("1. Enter any ANIMAL (e.g., penguin, hamster): ")
adjective1 = input("2. Enter a DESCRIBING word (e.g., smelly, giant, slimy): ")
clothing = input("3. Enter an item of CLOTHING (e.g., socks, spacesuit): ")
food = input("4. Enter a FOOD (e.g., pizza, broccoli, tacos): ")
verb = input("5. Enter an ACTION word (e.g., dance, explode, sneeze): ")
place = input("6. Enter a PLACE (e.g., the moon, McDonald's, a sandbox): ")

# --- STEP 3: Dramatic Pause ---
print("\n🔮 Shaking the magic story maker... 🔮")
time.sleep(2)  # Pauses for 2 seconds for dramatic effect!
print("\nHere is your story:\n")

# --- STEP 4: The Story Generator (String Concatenation) ---
# Teach String Building: Mixing text with variables using standard f-strings.
story = (
    f"Once upon a time, a {adjective1} {animal} decided to go on an adventure. "
    f"It put on its favorite pair of {clothing} and grabbed a bag of {food} for the road. "
    f"Suddenly, it felt a huge urge to {verb}! "
    f"It got so dizzy that it accidentally tripped and landed right in {place}. "
    f"Everyone looked and cheered, 'Wow, that is one legendary {animal}!'"
)

print(story)
print("\n====================================")
print("         THE END! 🎭                 ")
print("====================================")
