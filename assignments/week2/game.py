import time

# Title
print("\nSomeone Is Already Inside\n")

time.sleep(1)

print("It is 2:13 AM.")
time.sleep(1)
print("You are alone in your apartment.")
time.sleep(1)
print("Your phone vibrates.")
time.sleep(1)

# Input 1
name = input("What is your name? ")
print("Hello", name)
time.sleep(1)

print("Unknown message: Don't make any noise.")
time.sleep(1)
print("Unknown message: He is already inside your apartment.")
time.sleep(1)

# Input 2
reaction = 0
while reaction < 1 or reaction > 3:
    reaction = int(input("""
What do you do?
1 - Text back
2 - Ignore
3 - Stay silent and listen
> """))
    if reaction < 1 or reaction > 3:
        print("Enter 1 to 3.")

# First decisions
if reaction == 1:
    print("You text back.")
    time.sleep(1)
    print("New message: He heard that.")

elif reaction == 2:
    print("You ignore the message.")
    time.sleep(1)
    print("The apartment feels too quiet.")

else:
    print("You stay silent.")
    time.sleep(1)
    print("You hear a small noise from the kitchen.")

time.sleep(1)

# Input 3
action = 0
while action < 1 or action > 3:
    action = int(input("""
What do you do now?
1 - Check the kitchen
2 - Run to the door
3 - Lock your room and hide
> """))
    if action < 1 or action > 3:
        print("Enter 1 to 3.")

time.sleep(1)

# Final decisions
if action == 1:
    print("You walk to the kitchen...")
    time.sleep(1)
    print("Nothing is there.")
    time.sleep(1)
    print("Then you hear breathing behind you.")
    print("Game Over.")

elif action == 2:
    print("You run to the front door...")
    time.sleep(1)
    print("The hallway is empty.")
    time.sleep(1)
    print("Your phone vibrates again.")
    print("New message: Wrong move.")
    print("Game Over.")

else:
    if reaction == 3:
        print("You lock your room and hide.")
        time.sleep(1)
        print("You hear slow footsteps outside your door.")
        time.sleep(1)
        print("Then the front door opens and closes.")
        time.sleep(1)
        print("New message: You did nothing. That is why you survived.")
        print("You survived.")
    else:
        print("You lock your room and hide.")
        time.sleep(1)
        print("You hear someone stop outside your door.")
        time.sleep(1)
        print("The handle moves once.")
        print("Then everything becomes silent.")
        print("You survived, but he heard you.")

print("End.")
