print("""Welcome to Treasure Island.
Your mission is to find the treasure.""")
first_option = input("You're at a cross road. Where do you want to go? type 'left' or 'right'.\n").lower()
if first_option == 'left':
    second_option = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
    if second_option == 'wait':
        third_option = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()
        if third_option == 'yellow':
            print("You won!")
        elif third_option == 'blue':
            print("You've been eaten by beasts. Game Over!")
        elif third_option == 'red':
            print("You've been burned by fire. Game Over!")
        else:
            print("Game Over!")
    else:
        print("You've been attacked by trout. Game Over!")
else:
    print("You're have fallen into a hole. Game Over!")