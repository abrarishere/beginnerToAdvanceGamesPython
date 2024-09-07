import argparse
import os
from typing import List

from rich.console import Console
from rich.table import Table

console = Console()


def clear_console() -> None:
    """
    Clear the console screen.
    """
    os.system("cls" if os.name == "nt" else "clear")


def create_structure() -> List[str]:
    """
    Initialize the game board with numbered positions.

    Returns:
        List[str]: A list representing the game board with positions from 1 to 9.
    """
    return [str(i) for i in range(1, 10)]


console = Console()


def print_structure(board: List[str], verbose: bool) -> None:
    """
    Print the current state of the game board using a rich Table.

    Args:
        board (List[str]): The current game board state.
    """
    if not verbose:
        clear_console()  # Clear the console before printing the board

    # Creating a Rich table for the game board
    table = Table(show_header=False, show_edge=False, box=None)

    # Define the board row colors based on the player
    def format_cell(cell: str) -> str:
        if cell == "X":
            return f"[bold green]{cell}[/]"  # User's move
        elif cell == "O":
            return f"[bold red]{cell}[/]"  # Computer's move
        else:
            return f"[bold yellow]{cell}[/]"  # Available spot

    # Split the board into rows and format each cell
    table.add_row(format_cell(board[0]), format_cell(board[1]), format_cell(board[2]))
    table.add_row("---", "---", "---")
    table.add_row(format_cell(board[3]), format_cell(board[4]), format_cell(board[5]))
    table.add_row("---", "---", "---")
    table.add_row(format_cell(board[6]), format_cell(board[7]), format_cell(board[8]))

    console.print(table)


def perform_move(move: int, board: List[str], player: str, verbose: bool) -> List[str]:
    """
    Update the board with the player's move.

    Args:
        move (int): The position on the board where the move is made (1-9).
        board (List[str]): The current game board state.
        player (str): The player making the move ("user" or "computer").
        verbose (bool): Whether to print detailed move information.

    Returns:
        List[str]: The updated game board state.
    """
    index = move - 1
    if board[index] in {"X", "O"}:
        if verbose:
            console.print(
                f"[yellow]Position {move} is already taken. Try a different position.[/]"
            )
    else:
        symbol = "X" if player == "user" else "O"
        board[index] = symbol
        if verbose:
            color = "green" if player == "user" else "red"
            console.print(
                f"[{color}]{player.capitalize()} places '{symbol}' at position {move}.[/]"
            )
    return board


def get_user_input() -> int:
    """
    Prompt the user for input and ensure it's a valid integer between 1 and 9.

    Returns:
        int: A valid user input between 1 and 9.
    """
    while True:
        try:
            user_input = int(input("Enter a digit (1-9): "))
            if 1 <= user_input <= 9:
                return user_input
            else:
                console.print(
                    "[red]Input must be between 1 and 9. Please try again.[/]"
                )
        except ValueError:
            console.print("[red]Input must be an integer. Please try again.[/]")


def check_win(board: List[str], player: str) -> bool:
    """
    Check if the specified player has won the game.

    Args:
        board (List[str]): The current game board state.
        player (str): The player to check for a win ("user" or "computer").

    Returns:
        bool: True if the player has won, False otherwise.
    """
    symbol = "X" if player == "user" else "O"
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
    return any(board[a] == board[b] == board[c] == symbol for a, b, c in win_conditions)


def check_tie(board: List[str]) -> bool:
    """
    Determine if the game is a tie (i.e., the board is full).

    Args:
        board (List[str]): The current game board state.

    Returns:
        bool: True if the game is a tie, False otherwise.
    """
    return all(cell in {"X", "O"} for cell in board)


def computer_turn(board: List[str], verbose: bool) -> int:
    """
    Decide and perform the computer's move.

    Args:
        board (List[str]): The current game board state.
        verbose (bool): Whether to print detailed move information.

    Returns:
        int: The position where the computer made its move (1-9).
    """
    # Try to win
    for i in range(9):
        if board[i] not in {"X", "O"}:
            board[i] = "O"
            if check_win(board, "computer"):
                if verbose:
                    console.print(
                        f"[green]Computer places 'O' at position {i + 1} to win.[/]"
                    )
                return i + 1
            board[i] = str(i + 1)  # Revert move if it doesn't win

    # Block user win
    for i in range(9):
        if board[i] not in {"X", "O"}:
            board[i] = "X"
            if check_win(board, "user"):
                board[i] = "O"
                if verbose:
                    console.print(
                        f"[yellow]Computer places 'O' at position {i + 1} to block your win.[/]"
                    )
                return i + 1
            board[i] = str(i + 1)  # Revert move if it’s not blocking a win

    # Choose a preferred position (center, then corners, then edges)
    for i in [4, 0, 2, 6, 8, 1, 3, 5, 7]:
        if board[i] not in {"X", "O"}:
            board[i] = "O"
            if verbose:
                console.print(f"[green]Computer places 'O' at position {i + 1}.[/]")
            return i + 1


def main(verbose: bool = False) -> None:
    """
    Run the main game loop for Tic-Tac-Toe.

    Args:
        verbose (bool): Whether to print detailed game information.
    """
    console.print("[bold blue]You are X.[/]")
    board = create_structure()
    print_structure(board, verbose)

    while True:
        # User's Turn
        user_move = get_user_input()
        board = perform_move(user_move, board, "user", verbose)
        print_structure(board, verbose)

        if check_win(board, "user"):
            console.print("[bold green]Congratulations! You win![/]")
            break
        if check_tie(board):
            console.print("[yellow]The game is a tie![/]")
            break

        # Computer's Turn
        console.print("[bold blue]Computer's turn...[/]")
        computer_move = computer_turn(board, verbose)
        board = perform_move(computer_move, board, "computer", verbose)
        print_structure(board, verbose)

        if check_win(board, "computer"):
            console.print("[bold red]Computer wins! Better luck next time.[/]")
            break
        if check_tie(board):
            console.print("[yellow]The game is a tie![/]")
            break


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Play a game of Tic-Tac-Toe with a verbose option."
    )
    parser.add_argument(
        "--verbose", action="store_true", help="Enable detailed game output."
    )
    args = parser.parse_args()

    main(verbose=args.verbose)
