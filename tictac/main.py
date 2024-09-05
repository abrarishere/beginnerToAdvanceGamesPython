import random


def display_board(structure):
    """Displays the current state of the game board."""
    print("\nThe game board is as follows:")
    print(" " + structure[0] + " | " + structure[1] + " | " + structure[2] + " ")
    print("-----------")
    print(" " + structure[3] + " | " + structure[4] + " | " + structure[5] + " ")
    print("-----------")
    print(" " + structure[6] + " | " + structure[7] + " | " + structure[8] + " ")
    print()


def main():
    structure = [" " for i in range(9)]
    print("Welcome to the Tic-Tac-Toe Game")
    print("The structure of the game is as follows:")
    print(" 0 | 1 | 2 ")
    print("-----------")
    print(" 3 | 4 | 5 ")
    print("-----------")
    print(" 6 | 7 | 8 ")
    print("You will be playing against the computer.")
    print("You are X and the computer is O.")
    print("You will be prompted to enter a number between 0 and 8.")
    print("This number corresponds to the position on the board.")
    print("You will go first. Good luck!\n")

    display_board(structure)

    while True:
        player_move = -1
        while player_move not in range(9):
            try:
                player_move = int(input("Enter a number between 0 and 8: "))
            except ValueError:
                print("Invalid input. Please enter a valid number between 0 and 8.")

        if structure[player_move] == " ":
            structure[player_move] = "X"
        else:
            print("That position is already taken. Try again.")
            continue

        display_board(structure)

        if check_win(structure, "X"):
            print("You win!")
            break
        if check_tie(structure):
            print("It's a tie!")
            break

        computer_move = computer_turn(structure)
        structure[computer_move] = "O"

        display_board(structure)

        if check_win(structure, "O"):
            print("The computer wins!")
            break
        if check_tie(structure):
            print("It's a tie!")
            break

    play_again = input("Would you like to play again? (y/n): ").lower()
    if play_again == "y":
        main()
    else:
        print("Thanks for playing!")


def check_win(structure, player):
    win_conditions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),  # Rows
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),  # Columns
        (0, 4, 8),
        (2, 4, 6),  # Diagonals
    ]
    return any(
        structure[a] == structure[b] == structure[c] == player
        for a, b, c in win_conditions
    )


def check_tie(structure):
    return " " not in structure


def computer_turn(structure):
    # Try to win
    for i in range(9):
        if structure[i] == " ":
            structure[i] = "O"
            if check_win(structure, "O"):
                return i
            structure[i] = " "

    # Block player's win
    for i in range(9):
        if structure[i] == " ":
            structure[i] = "X"
            if check_win(structure, "X"):
                structure[i] = "O"
                return i
            structure[i] = " "

    # Take center if available
    if structure[4] == " ":
        return 4

    # Pick a random empty spot
    while True:
        move = random.randint(0, 8)
        if structure[move] == " ":
            return move


if __name__ == "__main__":
    main()
