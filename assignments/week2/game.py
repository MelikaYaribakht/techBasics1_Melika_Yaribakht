import time

# Title
print("""
   _________
  |         |
  | UNKNOWN |
  |  CALL   |
  |_________|
      📞
""")

time.sleep(1)

print("Your phone suddenly rings at 2:13 AM... 📞")
time.sleep(1)

# Input 1
name = input("What is your name? ")
print("Hello", name)
time.sleep(1)

# Input 2
answer = input("Do you answer the call? (yes/no): ")

# First condition
if answer == "no":
    print("You ignore the call.")
    time.sleep(1)
    print("At 2:23 AM... *knock* *knock* *knock*... 🚪")
    print("Game Over. 💀")

else:
    print("You answer the call...")
    time.sleep(1)
    print("Voice: Don't panic... I am you from tomorrow. 😨")
    time.sleep(1)

    # Input 3 (number with while)
    choice = 0
    while choice < 1 or choice > 3:
        choice = int(input("""
Choose one:
1 - Who are you?
2 - What happens tonight?
3 - Is this a joke?
> """))
        if choice < 1 or choice > 3:
            print("Enter a number between 1 and 3.")

    # Second condition + nested
    if choice == 1:
        print("Voice: I survived.")
        believe = input("Do you believe it? (yes/no): ")  # Input 4

        if believe == "yes":
            print("You trust the voice.")
        else:
            print("You are not sure.")

    elif choice == 2:
        print("Voice: At 2:23 AM, do NOT open the door.")

    else:
        print("Voice: This is not a joke...")

    time.sleep(1)

    # Input 5 (number with while)
    action = 0
    while action < 1 or action > 3:
        action = int(input("""
*knock* *knock* *knock*... 🚪

What do you do?
1 - Open the door
2 - Stay silent
3 - Call back
> """))
        if action < 1 or action > 3:
            print("Enter a number between 1 and 3.")

    time.sleep(1)

    # Final conditions
    if action == 1:
        print("You open the door...")
        time.sleep(1)
        print("No one is there...")
        print("Game Over. 💀")

    elif action == 2:
        if choice == 2:  # nested
            print("You stay silent...")
            time.sleep(1)
            print("Everything becomes quiet.")
            print("You survived. ✅")
        else:
            print("Nothing happens...")
            print("You wait until morning.")

    else:
        print("You call back...")
        time.sleep(1)
        print("Voice: Too late.")
        print("Game Over. 💀")

print("End.")
