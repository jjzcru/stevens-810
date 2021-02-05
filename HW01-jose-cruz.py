"""HW01: Rock, Paper, Scissors

   Both players simultaneously choose one of "rock", "paper", or "scissors" 
   and share their choice with their opponent using hand signals.    
   
   The outcome of a game is determined by:
   - Rock beats scissors (rock smashes scissors)
   - Scissors beats paper (scissors cut paper)
   - Paper beats rock (paper covers rock)
   - A tie occurs if both players choose the same option

   Author: Jose J. Cruz
"""
import os
import time
from shlex import quote as shlex_quote
from random import choice


def main():
    """Main program function"""
    clear_screen()
    player_move = get_player_move()
    start_game(player_move)
    print("END!!!!!")


def start_game(player_move: str) -> None:
    """Start a new game depending on the player move"""

    # If the move was 'q' exit the game
    if player_move == 'q':
        return

    computer_move: str = get_computer_move()
    result = get_game_result(player_move, computer_move)

    display_game_result({
        "result": result,
        "computer_move": computer_move,
        "player_move": player_move,
    })

    return start_game(get_player_move())


def get_player_move() -> str:
    """Loops until it get a valid player input"""
    move: str = input("Please choose 'R', 'P', 'S' or 'Q' to quit: ")
    move = move.lower()

    if move != 'r' and move != 'p' and move != 's' and move != 'q':
        print(f'"{move}" is not a valid option, please try again ⛔️ ')
        return get_player_move()

    return move


def get_computer_move() -> str:
    """ randomly choose and return one of 'rock', 'paper', 'scissors' """
    move: str = choice(['r', 'p', 's'])
    return move


def get_game_result(player_move: str, computer_move: str) -> int:
    """Get the result from the player and the computer move:
        - 0 (Tie)
        - 1 Player Win
        - -1 Computer Win
    """

    # Checks for tie
    if player_move == computer_move:
        return 0

    # Only search for combinations when the player wins
    if player_move == 'r' and computer_move == 's':
        return 1

    if player_move == 's' and computer_move == 'p':
        return 1

    if player_move == 'p' and computer_move == 'r':
        return 1

    # Everything else, the player loses

    return -1


def display_game_result(result: dict) -> None:
    """Prints the game result"""
    player_move = result['player_move']
    computer_move = result['computer_move']
    message: str = get_message(player_move, computer_move)

    print(result)


def get_message(player_move: str, computer_move: str) -> str:
    """Returns the message depending on game moves"""
    if (player_move == 'r' and computer_move == 's') or (player_move == 's' and computer_move == 'r'):
        return "rock beats scissors"

    if (player_move == 's' and computer_move == 'p') or (player_move == 'p' and computer_move == 's'):
        return "scissors beats paper"

    if (player_move == 'p' and computer_move == 'r') or (player_move == 'r' and computer_move == 'p'):
        return "paper beats rock"

    return ""


def get_move_symbol(move: str) -> str:
    if move == 'r':
        return 'rock 🪨'
    if move == 's':
        return 'scissors '
    if move == 'r':
        return 'rock 🪨'


def clear_screen():
    """Cleans the terminal"""
    os.system(shlex_quote('cls' if os.name == 'nt' else 'clear'))
    time.sleep(1)


if __name__ == "__main__":
    main()
