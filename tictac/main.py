import random


def main():
    structure = [' ' for i in range(9)]
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
    print("You will go first.")
    print("Good luck!")
    print()
    print("The game board is as follows:")
    print(" " + structure[0] + " | " + structure[1] + " | " + structure[2] + " ")
    print("-----------")
    print(" " + structure[3] + " | " + structure[4] + " | " + structure[5] + " ")
    print("-----------")
    print(" " + structure[6] + " | " + structure[7] + " | " + structure[8] + " ")
    print()
    while True:
        player_move = 10
        while not player_move < 8:
            player_move = int(input("Enter a number between 0 and 8: "))
        if structure[player_move] == ' ':
            structure[player_move] = 'X'
        else:
            print("That position is already taken. Try again.")
            continue
        if check_win(structure, 'X'):
            print("You win!")
            break
        if check_tie(structure):
            print("It's a tie!")
            break
        computer_move = computer_turn(structure)
        structure[computer_move] = 'O'
        if check_win(structure, 'O'):
            print("The computer wins!")
            break
        if check_tie(structure):
            print("It's a tie!")
            break
        print("The game board is as follows:")
        print(" " + structure[0] + " | " + structure[1] + " | " + structure[2] + " ")
        print("-----------")
        print(" " + structure[3] + " | " + structure[4] + " | " + structure[5] + " ")
        print("-----------")
        print(" " + structure[6] + " | " + structure[7] + " | " + structure[8] + " ")
        print()
    play_again = input("Would you like to play again? (y/n): ")
    if play_again == 'y':
        main()
    else:
        print("Thanks for playing!")
        return

def check_win(structure, player):
    if (structure[0] == player and structure[1] == player and structure[2] == player) or \
       (structure[3] == player and structure[4] == player and structure[5] == player) or \
       (structure[6] == player and structure[7] == player and structure[8] == player) or \
       (structure[0] == player and structure[3] == player and structure[6] == player) or \
       (structure[1] == player and structure[4] == player and structure[7] == player) or \
       (structure[2] == player and structure[5] == player and structure[8] == player) or \
       (structure[0] == player and structure[4] == player and structure[8] == player) or \
       (structure[2] == player and structure[4] == player and structure[6] == player):
        return True
    return False

def check_tie(structure):
    if ' ' not in structure:
        return True
    return False

def computer_turn(structure):
    for i in range(9):
        if structure[i] == ' ':
            structure[i] = 'O'
            if check_win(structure, 'O'):
                return i
            structure[i] = ' '
    for i in range(9):
        if structure[i] == ' ':
            structure[i] = 'X'
            if check_win(structure, 'X'):
                structure[i] = 'O'
                return i
            structure[i] = ' '
    if structure[4] == ' ':
        return 4
    while True:
        move = random.randint(0, 8)
        if structure[move] == ' ':
            return move

if __name__ == '__main__':
    main() 
    
