"""
PSEUDOCODE:

Import random library

define a function that rolls a dice

define a function with actual game:

- ask user for a name

- give an introduction of the game and provide user with options to choose

- write conditional statements depending on user choice

- wrap everything around in the loop so the user can decide when to stop the game.

- add a basic requirements to finish the game and solve the case

- add hidden easter egg to make it more fun

"""


from random import randint

def roll_dice():
    return randint(1, 6)

def game():
    print("Welcome to the Sparta-global Mystery Game!")

    player_name = input("Enter your name: ")

    print(f"Hello, {player_name}! You find yourself in an empty room. You have no idea what are you doing here. There is only laptop, Luke and Ramon")

    clues = 0
    trainers_help = 0


    play = True
    while play:
        print("\n What are you going to do? \n"
              "1. Investigate the room\n"
              "2. Ask Luke what is going on\n"
              "3. Use laptop\n"
              "4. Search your pockets\n"
              "5. Try to connect the dots\n"
              "6. Ask Ramon for help\n"
              "8. Quit the game")

        choice = int(input("Enter your choice (1-8): "))

        if choice == 1:
            print("You start to looking around the room hoping to find something that helps you to figure out what is going on...")
            dice_roll = roll_dice()
            print("You rolled: ", dice_roll)
            if dice_roll >= 4:
                print("You see the Deliveroo bag in the garbage bin. It has receipt inside it that says it was from 'Curry Paradise' restaurant in London. Nice one! Now you know at least the city where You are.")
                clues += 1
            else:
                print("Sorry, you don't see anything relevant.")

        elif choice == 2:
            print("You ask Luke to explain why are you here...")
            dice_roll = roll_dice()
            print("You rolled: ", dice_roll)

            if dice_roll >= 4:
                print("Nice one. Luke is a good guy. He explains you briefly what you are doing here")
                trainers_help += 1
            else:
                print("Too bad. Luke does not want to talk to you.")

        elif choice == 3:
            print("You access the laptop...")
            dice_roll = roll_dice()
            print("You rolled: ", dice_roll)
            if dice_roll >= 4:
                print("Wow! New lesson is starting in 20 minutes. Could it be the reason why are you here?")
                clues += 1
            else:
                print("Oh boy. It is a Windows computer. Too bad you can only use Mac.")

        elif choice == 4:
            print("You check your pockets...")
            dice_roll = roll_dice()
            print("You rolled: ", dice_roll)
            if dice_roll >= 4:
                print("Bingo! You find sparta-global access card in your pocket. Another piece to solve the case. ")
                clues += 1
            else:
                print("You can't find anything important, but mate...why are you not wearing an underwear?.")

        elif choice == 5:
            print("You are trying to connect the dots...")
            if clues >= 3 or trainers_help >= 2:
                print("You got it. It was super simple. You are in Sparta-global head office with your trainers, lesson starts in 20 minutes. You are here to give a guest-speech for the next cohort.")
            else:
                print("You cannot figure it out. Maybe you are not that smart after all. Are you sure you want to be a tech guy?.")

        elif choice == 6:
            print("You ask Ramon for help...")
            dice_roll = roll_dice()
            print("You rolled: ", dice_roll)
            if dice_roll >= 4:
                print("Ramon gives you more insight about the situation. You should've asked him sooner")
                trainers_help += 1
            else:
                print("Ramon looks at you judgmental. He says nothing and goes back to running on his treadmill")

        elif choice == 7:
            print("You woke up in your bed. Palms are sweaty, knees weak, arms are heavy. It was just a bad dream. Your mom calls you from the kitchen. She made spaghetti.")
            break

        elif choice == 8:
            print("Thank you for playing! Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 8.")

        play_again = input("Do you want to keep playing? (yes/no): ")
        if play_again.lower() == "no":
            print("Thank you for playing! Goodbye!")
            play = False


    print("\nGame summary")
    print(f"Clues found: {clues}")
    print(f"How many trainers you asked for help: {trainers_help}")




# Start the game
game()

