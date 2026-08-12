import turtle
import random

# --- STEP 1: Set up the playground ---
screen = turtle.Screen()
screen.title("The Magic Art Adventure!")
screen.bgcolor("black")  # Teach the kid they can change this color!

# Create our drawing artist
painter = turtle.Turtle()
painter.shape("turtle")
painter.speed(3)

# --- STEP 2: The Kid's Customizing Zone ---
# Teach variables: Let the child change these values
PEN_COLOR = "cyan"  # Try "red", "yellow", "lime"
PEN_SIZE = 5  # Try making it thicker or thinner

painter.color(PEN_COLOR)
painter.pensize(PEN_SIZE)

# --- STEP 3: The Secret Loop ---
# Teach loops: This draws a glowing star burst automatically
for i in range(15):
    painter.forward(100)
    painter.left(135)

# --- STEP 4: Interactive Story Decisions ---
# Teach conditionals: The child makes a choice via a popup box
choice = screen.textinput("Your Choice", "Pick a magic path: 'square' or 'circle'?")

if choice == "square":
    painter.color("magenta")
    for _ in range(4):
        painter.forward(80)
        painter.left(90)

elif choice == "circle":
    painter.color("yellow")
    painter.circle(50)

else:
    # If they type something silly, the turtle does a random dance
    painter.color("orange")
    painter.write("Magic chaos!", font=("Arial", 16, "bold"))
    for _ in range(8):
        painter.forward(30)
        painter.left(45)

# Keep the window open until clicked
screen.exitonclick()
