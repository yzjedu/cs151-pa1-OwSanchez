# Class: CS151
# Professor Z.
# Programmer: Owen Sanchez
# Prompt: This program will run you through a small turn based combat game.

# Woken up
print("WAKE UP!")
name = input("What is your name, prisoner?: ")
print("You are woken up.")
print(f"Guard: {name}, you will sit in this cell for life!")

while True:
    answer = input("Do you wish to pick up the sword? (Yes or No): ").lower()

    if answer == "yes":
        print("Congratulations, you have the sword!")
        sword = 2.5  # Swords value
        break

    elif answer == "no":
        print("You sit and wait in the cell...")

    else:
        print("Invalid response, please answer with 'Yes' or 'No'.")

print(f"Guard: Put down the sword!\n*The guard enters the cell*")
print("*You attack the guard with your sword! More guards come to detain you.*")

# Fight sequence
while True:
    battle = input("Choose to attack guard 1 or 2: ")

    if battle == "1":
        print("You attack guard 1 and he dropped a shield.\nCongratulations, you have the shield!")
        shield = 1.5  # Shield Resistance
        break

    elif battle == "2":
        print("You attack guard 2 and guard 1 flees.")
        shield = 0  # No shield
        break

    else:
        print("Please input 1 or 2.")

print("You continue down the hall of the prison.")

# Decides where the story will go. Items for different choices
key = 0
dark_wand = 0

while True:
    room = input("Enter The Armory, The Kitchen, or The Garbage Room? Please input (1, 2, or 3): ")

    # The Armory
    if room == "1":
        print("The blacksmith attacks as soon as you enter!")
        attack_sequence = input("Attack or Shield: ").lower()

        if attack_sequence == "attack":
            print("The blacksmith is faster! The Blacksmith kills you in one hit!")
            exit("GAME OVER!")  # End the game after the player dies

        elif attack_sequence == "shield":
            if shield == 1.5:  # The user has the shield
                print("You block his attack and counter with your sword!")
                print("The blacksmith dropped the prison key!")
                key = 1  # The player picks up the key
            elif shield == 0:  # The user does not have a shield
                print("You don't have a shield! The blacksmith attacks you!")
                exit("GAME OVER!")  # End the game

        else:
            print("Invalid input. You need to choose either 'Attack' or 'Shield'.")

    # The Kitchen or The Garbage Room
    elif room == "2" or room == "3":
        if room == "2":
            print("You have entered the Kitchen.")
        elif room == "3":
            print("You have entered the Garbage Room.")

        print("You see a magic staff in the corner and pick it up.\nCongratulations, you now have the Dark Wand!")
        dark_wand = 1  # Player has dark wand
        break


    else:
        print("Invalid input. Please enter 1, 2, or 3.")

# Decision to leave based on prior choices
while True:
    leave = input("Do you wish to leave the prison? (Yes or No): ").lower()

    if leave == "yes":
        key_option = input("Do you wish to use the key? (Yes or No): ").lower()

        if key_option == "yes":
            if key == 1:
                exit("YOU USED THE KEY AND ESCAPED THE PRISON! CONGRATULATIONS")
            else:
                print("You don't have the key!")
        else:
            print("You decided not to use the key.")
            break

    elif leave == "no":
        print("You live a happy life in the prison! \n...For about 2 minutes until more guards come and put you back in the cell.\nGAME OVER!")
        exit("GAME OVER!")
    else:
        print("Invalid input. Please enter 'Yes' or 'No'.")

#Intro to last battle
print("Warden: Prisoner return to your cell!")
print("Warden (8hp/4 atk. damage)")

# Set Users health and Weapons
user_health = 8
warden_health = 8
flail = 5
bow_arrow = 4
dark_wand = 6
# Final Boss Battle
while True:
    boss = input("Use: Sword, Shield, Dark Wand: ")
    if boss == "Sword":
        user_health = 8 - bow_arrow
        print(f"Warden out of range.\nWarden uses bow.\n{name} Health: {user_health}/8HP")
        break
    elif boss == "Shield":
        if shield == 1.5:
            print("Warden uses bow and arrow. Your Shield blocks the arrow.")
            break
        elif shield == 0:  # No shield
            print("You do not have the shield.")
    elif boss == "Dark Wand":
        warden_health = 8 - dark_wand
        print(f"You use the Dark Wand on the Warden. \n Warden Health: {warden_health}/8HP")
        break
    else:
        print("Invalid input. Please enter Sword, Shield, Dark Wand.")
print("Warden steps closer and pulls out Flail (5 atk. dmg.")

# Next fight sequence
while True:
    second_boss = input("Use: Sword, Shield, Dark Wand: ")
    if second_boss == "Sword":
        warden_health -= sword
        print(f"You stabbed the warden. \n Warden Health: {warden_health}/8HP")
    elif second_boss == "Shield":
        if shield == 1.5:
            user_health -= 4
            print("Warden hits your shield with flail.\n But your shield resistance wasn't strong enough!")
            print(f"{name} Health: {user_health}/8HP")
        elif shield == 0:  # No shield
            print("You do not have the shield.")
    elif second_boss == "Dark Wand":
        user_health -= 5
        print(f"Dark Wand takes too long to work!\n {name} Health: {user_health}/8HP")
    if user_health <= 0:
        exit("GAME OVER!")
    if warden_health <= 0:
        exit("YOU HAVE DEFEATED THE WARDEN CONGRATULATIONS PRISONER!")
    if user_health or warden_health > 0:
        break
    else:
        print("Invalid input. Please enter Sword, Shield, Dark Wand.")

# Ending Scene if user doesn't input Dark Wand then Sword but has more than 0 health.
print("Warden hits you with flail again.\n You are too weak to get up!")
print("Warden: You're pitiful! Go back to your cell!")
print("You sit in your cell...broken")
exit("GAME OVER!")
