import random


def how_to_play():
    print("Here's how to play:")
    sample_board = ([0, 1, 2], [3, 4, 5,], [6, 7, 8])
    print(sample_board)

def invalid_input():
    print("Sorry, that's not one of the options. Try again.")
    return starting()


def starting():
    user_start_choice = input("How would you like to start? Either you can go first (input 'me first'), "
                              "I can go first (input 'you first'), or the first turn can be picked randomly"
                              " (input 'random'). ")
    if user_start_choice.isalpha:
        user_start_choice = str(user_start_choice)

        if user_start_choice == "me first":
            print("Okay, you will go first!")
            return user_first()

        if user_start_choice == "you first":
            print("Okay, I will go first!")
            return npc_first()

        if user_start_choice == "random":
            print("Okay, the first player will be randomly picked.")
            return random_choice()

        else:
            return invalid_input()

    else:
        return invalid_input()


def user_first():
    print("You will be [X].")
    return how_to_play()


def npc_first():
    print("I will be [X]")
    return how_to_play()


def random_choice():
    players = [1, 2]
    result = random.choice(players)
    if result == 1:
        print("You have been chosen!")
        return user_first()

    if result == 2:
        print("I have been chosen!")
        return npc_first()

    else:
        print("Sorry, there was an error choosing the first player. Let's try again.")
        return starting()


def main():
    user_name = input("Hello User! What is your name?")
    print("Hello", user_name, ", welcome to Tic-Tac-Toe!")
    return starting()


main()

# invalid_input()
