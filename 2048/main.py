import os
import random


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board):
    clear_console()
    for row in board:
        print('+----' * len(row) + '+')
        print('|'.join(f'{num:^5}' for num in row))
    print('+----' * len(board[0]) + '+')

def initialize_board():
    board = [[0] * 4 for _ in range(4)]
    add_random_tile(board)
    add_random_tile(board)
    return board

def add_random_tile(board):
    empty_cells = [(r, c) for r in range(4) for c in range(4) if board[r][c] == 0]
    if not empty_cells:
        return False
    row, col = random.choice(empty_cells)
    board[row][col] = 2 if random.random() < 0.9 else 4
    return True

def rotate_board(board):
    return [list(row) for row in zip(*board[::-1])]

def move_left(board):
    def merge(row):
        new_row = [i for i in row if i != 0]
        for i in range(len(new_row) - 1):
            if new_row[i] == new_row[i + 1]:
                new_row[i] *= 2
                new_row[i + 1] = 0
        new_row = [i for i in new_row if i != 0]
        new_row += [0] * (len(row) - len(new_row))
        return new_row

    return [merge(row) for row in board]

def move_right(board):
    return [row[::-1] for row in move_left([row[::-1] for row in board])]

def move_up(board):
    return rotate_board(move_left(rotate_board(rotate_board(rotate_board(board)))))

def move_down(board):
    return rotate_board(rotate_board(rotate_board(move_left(rotate_board(board)))))

def check_game_over(board):
    for row in board:
        if 0 in row:
            return False
    for row in board + rotate_board(board):
        for i in range(len(row) - 1):
            if row[i] == row[i + 1]:
                return False
    return True

def main():
    board = initialize_board()
    while True:
        print_board(board)
        move = input("Move (w/a/s/d): ").strip().lower()
        if move not in ['w', 'a', 's', 'd']:
            print("Invalid move. Use w, a, s, or d.")
            continue

        if move == 'w':
            new_board = move_up(board)
        elif move == 'a':
            new_board = move_left(board)
        elif move == 's':
            new_board = move_down(board)
        elif move == 'd':
            new_board = move_right(board)

        if new_board != board:
            board = new_board
            if not add_random_tile(board):
                print_board(board)
                print("Game Over!")
                break
        else:
            if check_game_over(board):
                print_board(board)
                print("Game Over!")
                break

if __name__ == "__main__":
    main()
