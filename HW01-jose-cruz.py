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
    score_board = {
        'wins': 0,
        'losses': 0,
        'ties': 0,
    }
    while True:
        if not start_game(player_move, score_board):
            break;
        player_move = get_player_move()
    display_score_board(score_board)


def start_game(player_move: str, score_board: dict) -> bool:
    """Start a new game depending on the player move"""

    # If the move was 'q' exit the game
    if player_move == 'q':
        return False

    computer_move: str = get_computer_move()
    result = get_game_result(player_move, computer_move)

    display_game_result({
        "result": result,
        "computer_move": computer_move,
        "player_move": player_move,
    })
    print()

    # Add the result to the score board
    if result == 0:
        score_board['ties'] += 1
    elif result == 1:
        score_board['wins'] += 1
    else:
        score_board['losses'] += 1

    return True


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


def display_game_result(game_result: dict) -> None:
    """Prints the game result"""
    result = game_result['result']
    player_move = game_result['player_move']
    computer_move = game_result['computer_move']

    if result == 0:
        print('Tie: We both chose {move}'.format(move=get_move_symbol(player_move)))
        return

    message: str = get_message(player_move, computer_move)

    if result == 1:
        print(f'{message} - You Win!')
        return

    print(f'{message} - I Win!')


def display_score_board(score_board: dict) -> None:
    """Receives the score board and prints the result"""
    total_wins = score_board['wins']
    total_losses = score_board['losses']
    total_ties = score_board['ties']

    games_played = total_wins + total_losses + total_ties
    if games_played == 0:
        print(f"You didn't played at all ☹️")
        return

    wins_percentage = round((total_wins * 100) / games_played, 2)
    losses_percentage = round((total_losses * 100) / games_played, 2)
    ties_percentage = round((total_ties * 100) / games_played, 2)

    clear_screen()
    print(f"Games Played: {games_played}\n")
    print('------------------------------------')
    print(f"Wins Percentage: {wins_percentage}%")
    print(f"Losses Percentage: {losses_percentage}%")
    print(f"Ties Percentage: {ties_percentage}%")
    print('------------------------------------')
    print(f'Total of Wins: {total_wins}')
    print(f'Total of Losses: {total_losses}')
    print(f'Total of Ties: {total_ties}')


def get_message(player_move: str, computer_move: str) -> str:
    """Returns the message depending on game moves"""
    first_move = ""
    second_move = ""
    if (player_move == 'r' and computer_move == 's') or (player_move == 's' and computer_move == 'r'):
        first_move = get_move_symbol('r')
        second_move = get_move_symbol('s')
    elif (player_move == 's' and computer_move == 'p') or (player_move == 'p' and computer_move == 's'):
        first_move = get_move_symbol('s')
        second_move = get_move_symbol('p')
    elif (player_move == 'p' and computer_move == 'r') or (player_move == 'r' and computer_move == 'p'):
        first_move = get_move_symbol('p')
        second_move = get_move_symbol('r')

    return f'{first_move} beats {second_move}'


def get_move_symbol(move: str) -> str:
    """It returns the move name and symbol"""
    if move == 'r':
        return 'rock 🪨 '
    if move == 's':
        return 'scissors ✂ ️'
    if move == 'p':
        return 'paper 🧻 '

    return ""


def clear_screen():
    """Cleans the terminal"""
    os.system(shlex_quote('cls' if os.name == 'nt' else 'clear'))
    time.sleep(1)


if __name__ == "__main__":
    main()
