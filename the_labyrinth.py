# import time and random modules
import time
import random

# --- Global variables

# player list - to select character
# same character therefore global variable
player_list = ["elf", "fairy",
               "human", "witch", "wizard"]
player = ""  # empty is assigned value in choose_character function

# enemy list - random module to select
# same enemy entire game therefore global variable
enemy_list = ["Goblin King", "Eleven King", "Immortal", "Dark Wizard"]
chosen_enemy = random.choice(enemy_list)

#  riddles
# source: reader's digest - https://www.rd.com/list/what-am-i-riddles/
riddle_one = ("I have eyes but I can't see\n"
              "I live in the dark until you need me.\n\n")  # mirror / a mirror

riddle_two = ("I can fly but I have no wings.\n"
              "I can cry but I have no eyes.\n"
              "Wherever i go darkness "
              "follows me.\n\n")  # cloud / clouds

riddle_three = ("I can be thrown but I can be caught.\n"
                "Ways to lose me are always "
                "being sought.\n\n")  # cold / a cold

riddles = [riddle_one, riddle_two, riddle_three]
riddle_answers = ["mirror", "a mirror", "cloud", "clouds", "cold", "a cold"]

# maze - lions door - random choice of the correct door.
lions_door = ["correct door", "wrong door"]
necklace_door = ""
night_door = ""
left_door = random.choice(lions_door)

if left_door == lions_door[0]:  # randomly selects the right and wrong door
    necklace_door = left_door  # assigns right door to necklace_door variable
    right_door = lions_door[1]
    night_door = right_door

else:
    right_door = lions_door[0]
    necklace_door = right_door
    night_door = left_door


# fight the enemy
weapons = ["sword", "mace", "wand", "staff", "knife", "pistol"]
weapon_choice = random.choice(weapons)
player_health = 100
enemy_health = 100

# --- Functions

# commentary function with time delay (time module)


def commentary(dialogue):
    print(dialogue)
    # delay execution of next code by (x) seconds
    time.sleep(1.5)

# valid input function - string


def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        for option in options:
            return option
        print(f"Sorry, the option {option} is invalid. "
                   "Please try again.")


# valid input function - numeric


def valid_numeric_input(prompt, minimum, maximum):
    while True:
        option = input(prompt).lower()
        if option.isnumeric(): # return True if numeric string
            option = int(option)
            if minimum <= option <= maximum:
                return option
            else:
                print(f"Select number which is => {minimum} "
                       f"and <= {maximum}")
        else: 
            print("Choice must be numeric. Please try again.")


# play again function


def play_again():
    play_again = valid_input("Would you like to play again? (y/n)\n", ["y", "n"])
    if play_again == "y":
        commentary("\nRestarting the game ...\n")
        play_game()
    else:
        commentary("Thanks for playing!")

# start point - player list - user chooses player


def choose_character(inventory):
    commentary("")
    commentary("\nWelcome to The Labyrinth\n")
    commentary(f"Choose your character: \n")
    commentary(f"1. {player_list[0]}\n"
               f"2. {player_list[1]}\n"
               f"3. {player_list[2]}\n"
               f"4. {player_list[3]}\n"
               f"5. {player_list[4]}\n")
    
    player_number = valid_numeric_input("Pick a number between 1 and 5\n",1,5)
    # player_number = valid_input("Pick a number between 1 and 5\n",["1","2","3","4","5"])
    commentary("")
    commentary(
        f"\nYou have selected to be a {player_list[player_number-1]}\n\n")

    # Change the value of the global variable into some function.
    # You must use the global keyword.
    global player
    player = player_list[player_number-1]

    countdown(inventory)

# game countdown


def countdown(inventory):
    commentary("Game loading...")
    n = 3
    while n > 0:
        print(n)
        n -= 1
        time.sleep(1)
    commentary("Good luck!\n")
    intro(inventory)


# intro to the game
def intro(inventory):
    commentary("Your quest is simple..")
    commentary("Find the maze...")
    commentary("Complete the challenges...")
    commentary("Survive...")
    commentary("Defeat the " + chosen_enemy + "!\n\n")
    strange_man(inventory)

# meeting the strange man


def strange_man(inventory):
    commentary("You have been travelling for 6 months,")
    commentary("when you come across a man.")
    commentary("This man seems strange...")
    commentary("ancient face, kind smile but his eyes... "
               "they have an inhuman shine to them.")
    commentary("Is he even human?\n")
    commentary("The man sees you and beckons you to come.")
    commentary("The man smiles...")
    commentary(f"'Greetings, little {player}'")
    commentary("He is leaning against an ancient oak with his arms crossed.")
    commentary("'I know why you are here.'")
    commentary("He looks at you and his eyes suddenly glow purple.")
    commentary("The man leans forward, his purple hair moving with wind")
    commentary("The man speaks:\n")
    commentary("'I have heard the whispers on the wind.'")
    commentary("'You seek the maze.'")
    commentary("'I will show you the path but would you help me first?'\n")

    commentary("What do you say to the purple-eyed man?\n")
    commentary("(1) Show me where the maze is.\n"
               "(2) I will help you.\n")
    help_man = valid_input("Select 1 or 2\n", ["1", "2"])

    if help_man == "1":
        commentary("\nYou ask for him to show you the maze")
        commentary(
            "For a moment he looks disappointed - was that the wrong answer?")
        commentary("His eyes pulse purple and sniffs... he looks at you\n")
        commentary("'Very well...'\n")
        commentary("As soon as you blink the man starts to vanish "
                   "becoming the whisper on the wind")
        commentary("You follow the wind and the mist clears in the distance")
        commentary("There on the hoizon is the maze")
        commentary("You walk towards the maze...\n")

    elif help_man == "2":
        commentary("\nThe man smiles and claps his hands\n")
        commentary("'Excellent! I have heard of your curiosity, "
                   "this will help you on your quest but beware... "
                   "it may also be your downfall.\n")
        commentary("His eyes suddenly begin to glow - warm gold "
                   "like the setting sun")
        commentary("You suddenly step back...\n")
        commentary("'Don\'t be afraid. Answer my riddle...'\n")
        commentary("You nod, the skies darken, the wind picks up...\n")
        commentary(
            "The man eyes still burn gold and his voice echos around you:\n")
        print(random.choice(riddles))
        riddle_entry = input("What am i?\n").lower()

        if riddle_entry in riddle_answers:  # match answer in list of answers
            commentary("\nThe man smiles. \n")
            commentary("'I knew they were right about you "
                       "you indeed have wisdom beyond your years.'\n")
            commentary(
                "With a flick of his hand, you find a "
                "necklace around your neck.")
            commentary("The chain is platinum and the oval crystal sits "
                       "cooly against your skin.")
            commentary("When you touch the crystal it hums"
                       "and suddenly glows red "
                       "and back to clear when you move your hand away.\n")
            commentary("The man speaks to you with a smile on his lips: ")
            commentary("'This is the Crystal of Gaia. It is a fragment of "
                       "mother nature\'s heart.'")
            commentary("'This crystal will change color "
                       "as your emotions "
                       "change and will provide you "
                       "with aid when you "
                       "are in most need.'")
            commentary("'Look after her heart fragment "
                       "and guard it with your own,"
                       " be true to yourself and it will serve you well.'\n")
            commentary("You thank the strange man.")
            commentary("The man suddenly burst into stardust and surges, "
                       "towards your necklance")
            commentary("The necklace glows as bright as a star, "
                       "and your vision darkens...")
            commentary("...")
            commentary("...")
            commentary("You wake in front of the maze...")
            inventory.append("necklace")  # adds necklace to inventory

        else:
            commentary("\nThe man looks at you and fades with the wind.\n")
            commentary("A whisper on the wind says: \n")
            commentary("'You have failed, follow the leaves in the wind "
                       "they will show you the path.'")
            commentary("'Hold your hand out...'\n")
            commentary(
                "You hold you hand out and an "
                "amethyst crystal ball appears.\n")
            commentary(
                "'Take this crystal, it will guide you "
                "in the darkest night'\n")
            commentary("You follow the leaves to the maze...\n")
            inventory.append("crystal")  # adds crystal to inventory

    maze_lions(inventory)

# Maze - challenge 1 - stone lions


def maze_lions(inventory):
    commentary("Your are in front of the maze.")
    commentary("The maze is made of ancient stone, obsidian in color.")
    commentary("As you enter the maze, you walk straight ahead.")
    commentary(
        "You notice that the path is blocked by "
        "two great ancient oak doors.")
    commentary("In front of these doors are two proud 8ft stone lions.")
    commentary("These lions seems to be guarding the doors?\n")

    commentary("Suddenly the stone eyes of the "
               "lions both open at the same time.")
    commentary("There eyes are the same as the maze - obsidian in color.")
    commentary("The lions look down at you...")
    commentary("The lions begin to rumble - no doubt a purr but to your ears "
               "the rumbles are deep and vibrate through your chest.\n")
    commentary("The lions voices suddenly break their rumbles....\n")
    commentary("'Choose a door and see.'")
    commentary("'We cannot tell you what is within.'")
    commentary("'But trust your instincts and you'll be free.'\n")
    commentary("They part to the sides of the maze and watch you intently.\n")

    if "necklace" in inventory:
        commentary("Suddenly your necklace starts to grow hot and "
                   "glow red. As it burns brighter and becomes even hotter, "
                   "you shut your eyes pained.")
        commentary(f"When you open them, the {necklace_door} glows red. "
                   f"You choose that door and walk through.")
        commentary(f"The maze continues in front of you."
                   f"You made the right choice")
        maze_fight(inventory)

    else:
        commentary("Choose a door.\n")
        commentary("(1) Left door.\n"
                   "(2) Right door.\n")
        door = valid_input("Pick 1 or 2\n", ["1", "2"])

        # brackets on if as statement is so long
        # put on two lines
        if (left_door == "correct door" and door == "1" or
                right_door == "correct door" and door == "2"):
            commentary(f"You point to the {necklace_door} and it opens.")
            commentary(f"The maze continues in front of you. "
                       f"You made the right choice\n")
            maze_fight(inventory)

        elif (left_door == "wrong door" and door == "1" or
              right_door == "wrong door" and door == "2"):
            commentary(f"You point to the {night_door}.")
            commentary("You walk through the door and suddenly "
                       "you are plunged into the darkest night.\n")
            # if you have crystal in inventory you can escape
            if "crystal" in inventory:
                commentary("You take the crystal out of your pocket and "
                           "it lights the darkness.")
                commentary("You see the door on the otherside and open it.")
                commentary("The maze continues in front of you.\n")
                maze_fight(inventory)

            else:
                commentary("You feel around the dark....")
                commentary("It\'s hopeless...")
                commentary("In the distance you hear laughing...")
                play_again()


def maze_fight(inventory):
    commentary("\nYou walk further into the maze.")
    commentary("Suddenly a strange mist descends. "
               "A green bolt of lightning cuts through "
               "the fog.")
    if "necklace" in inventory:
        commentary("Your necklace suddenly glows green.")
        commentary("Before the green bolt can hit you, your "
                   "necklace repels the bolt and it hits the "
                   "other side of the maze wall")

    else:
        commentary("You have nothing which can defend "
                   "you from this!")
        commentary("The bolt hits you and you fly across "
                   "the maze, hitting your back on the wall.")
        commentary("You stagger back to your feet.")

    commentary(f"A shadow of a person is within the mist. "
               f"They must have fired the bolt.")
    commentary(f"As they come closer you realise who it is, "
               f"the person you need to defeat... the {chosen_enemy}\n")
    fight_enemy(inventory)

# Fighting enemy


def fight_enemy(inventory):
    commentary("Will you fight or flee?\n")
    fight = valid_input("Enter 1 or 2: \n\n"
                  "1. Fight!\n"
                  "2. Flee for your life!\n\n", ["1", "2"])

    if fight == "1":
        commentary(f"\nThe {chosen_enemy} sneers at you:")
        commentary("'I see you wish to fight...'")
        commentary(f"The {chosen_enemy} clicks their fingers and "
                   f"{weapon_choice} appears in your hand.")

        fight_sequence(inventory)

    elif fight == "2":
        commentary("You move as fast as you can.")
        commentary("You are not ready to do this...")
        commentary("As you run the floor gives way underneath you, "
                   "when you wake you are back where you were 6 months ago")
        commentary("Its like you were never at the maze.")
        commentary("You have to start right from the beginning again.")
        play_again()

    else:
        fight_enemy(inventory)  # repeats until choose

# Below code is based/adapted from:
# https://github.com/darylkevin/Python-Adventure-Game/blob/master/adventure_game.py


def fight_sequence(inventory):
    # random damage between 10 and 50 inclusive
    player_hit = random.randint(10, 50)
    # random damage between 10 and 60 inclusive - necklace not in inventory
    if "necklace" in inventory:
        # random damage between 10 and 60 inclusive
        enemy_hit = random.randint(20, 60)
        enemy_hit = round(enemy_hit / 5)  # necklace increases your defence
        commentary("Your necklace glows blue and you notice a magical "
                   "field which increases you defences\n")
    else:
        commentary(
            f"You hold your {weapon_choice} tightly. And hope for the best\n")
        enemy_hit = random.randint(20, 60)
    commentary(
        f"You use your {weapon_choice} on {chosen_enemy} -- they stagger...")
    commentary(f"You cause {player_hit} of damage")
    global enemy_health  # changing global variable
    enemy_health -= player_hit  # enemy health reduced by player hit
    commentary(f"The {chosen_enemy}'s health is {enemy_health} out of 100.\n")
    global player_health  # changing global variable
    if enemy_health <= 0:
        commentary(f"You have defeated the {chosen_enemy}!")
        commentary("Thanks for playing.")
        play_again()

    elif player_health > 0:
        commentary(
            f"The {chosen_enemy} retaliates. And fires another green bolt.")
        commentary(f"The {chosen_enemy} causes {enemy_hit} damage to you.")

        player_health -= enemy_hit  # player health reduced by enemy hit
        commentary(f"Your health is {player_health} out of 100.\n")
        if player_health <= 0:
            commentary("You are defeated.")
            play_again()

        else:
            fight_sequence(inventory)


# entry point - start game
def play_game():
    # inventory - starts empty list
    inventory = []
    choose_character(inventory)


play_game()
