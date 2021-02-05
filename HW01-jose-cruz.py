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


def main() -> None:
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
            break
        player_move = get_player_move()
    display_score_board(score_board)
    display_random_quote()


def start_game(player_move: str, score_board: dict) -> bool:
    """Start a new game depending on the player move"""

    # The player find the easter egg 😲
    if player_move == 'quote':
        random_quote: dict = get_random_quote()
        quote: str = random_quote['quote']
        game: str = random_quote['game']
        print(f'\nQUOTE 🗣:\n{quote}')
        print(f' - {game}\n')
        return True

    # If the move was 'q' exit the game
    if player_move == 'q':
        return False

    computer_move: str = get_computer_move()
    result: int = get_game_result(player_move, computer_move)

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

    if move == 'quote':
        return move

    if move != 'r' and move != 'p' and move != 's' and move != 'q':
        print(f'"{move}" is not a valid option, please try again ⛔️ \n')
        return get_player_move()

    return move


def get_computer_move() -> str:
    """ randomly choose and return one of 'rock', 'paper', 'scissors'
        r = rock
        p = paper
        s = scissors
    """
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
    result: int = game_result['result']
    player_move: str = game_result['player_move']
    computer_move: str = game_result['computer_move']

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
    total_wins: int = score_board['wins']
    total_losses: int = score_board['losses']
    total_ties: int = score_board['ties']

    games_played = total_wins + total_losses + total_ties
    if games_played == 0:
        clear_screen()
        print(f"You didn't played at all ☹️")
        return

    wins_percentage: float = round((total_wins * 100) / games_played, 2)
    losses_percentage: float = round((total_losses * 100) / games_played, 2)
    ties_percentage: float = round((total_ties * 100) / games_played, 2)

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
    first_move: str = ""
    second_move: str = ""

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
    symbols: dict = {
        'r': 'rock 🪨 ',
        's': 'scissors ✂️',
        'p': 'paper 🧻 '
    }

    return symbols[move]


def clear_screen() -> None:
    """Cleans the terminal"""
    os.system(shlex_quote('cls' if os.name == 'nt' else 'clear'))
    time.sleep(1)


def display_random_quote():
    random_quote = get_random_quote()
    quote = random_quote['quote']
    game = random_quote['game']
    print('\n--------------------')
    print('Quote of the game 📝\n')
    print(quote)
    print(f' - {game}\n')


def get_random_quote() -> dict:
    """Returns a random quote from a game
    
    To add a little flavor to the game, when looking at the 
    score the program is going to display a random quote
    so players has something to look for everytime they play.

    And who doesn't like a good quote 😌
    """
    quotes = [
        {
            'quote': 'I’m Commander Shepard, and this is my favorite store on the Citadel!',
            'game': 'Mass Effect 2'
        },
        {
            'quote': 'What is a man? A Miserable little pile of secrets!',
            'game': 'Castlevania: Symphony of the Night'
        },
        {
            'quote': 'We’re not tools of the government or anyone else. Fighting was the only thing I was good at, but at least I always fought for what I believed in.',
            'game': 'Metal Gear Solid'
        },
        {
            'quote': 'The right man in the wrong place can make all the difference in the world.',
            'game': 'Half-Life 2'
        },
        {
            'quote': 'The healthy human mind doesn’t wake up in the morning thinking this is its last day on Earth. But I think that’s a luxury, not a curse. To know you’re close to the end is a kind of freedom. Good time to take… inventory.',
            'game': 'Call of Duty: Modern Warfare'
        },
        {
            'quote': 'You can’t break a man the way you break a dog or a horse. The harder you beat a man, the taller he stands.',
            'game': 'Far Cry 2'
        },
        {
            'quote': 'Nothing is true, everything is permitted.',
            'game': 'Assassin’s Creed franchise'
        },
        {
            'quote': 'It’s dangerous to go alone, take this!',
            'game': 'The Legend of Zelda'
        },
        {
            'quote': 'Endure and survive.',
            'game': 'The Last of Us'
        },
        {
            'quote': 'War is where the young and stupid are tricked by the old and bitter into killing each other.',
            'game': 'Grand Theft Auto IV'
        },
        {
            'quote': 'A man chooses; a slave obeys.',
            'game': 'Bioshock'
        },
        {
            'quote': 'Good men mean well. We just don’t always end up doing well.',
            'game': 'Dead Space 3'
        },
        {
            'quote': 'Men are but flesh and blood. They know their doom, but not the hour.',
            'game': 'The Elder Scrolls: Oblivion'
        },
        {
            'quote': 'Time passes, people move. Like a river’s flow, it never ends. A childish mind will turn to noble ambition.',
            'game': 'The Legend of Zelda: Ocarina of Time'
        },
        {
            'quote': 'At the end of the day, as long as there are two people left on the planet, someone is gonna want someone dead.',
            'game': 'Team Fortress 2'
        },
        {
            'quote': 'Don’t make a girl a promise if you know you can’t keep it.',
            'game': 'Halo 3'
        },
        {
            'quote': 'The thing about happiness is that you only know you had it when it’s gone. I mean, you may think to yourself that you’re happy. But you don’t believe it. You focus on the petty bull ****, or the next job, or whatever. It’s only looking back by comparison with what comes after that you understand, that’s what happiness felt like.',
            'game': 'Fallout 4'
        },
        {
            'quote': 'Reliance upon others is a weakness for the strong but strength for the weak. Wisdom and balance lie in knowing your nature over time.',
            'game': 'Thief II'
        },
        {
            'quote': 'What is a man but the sum of his memories? We are the stories we live, the tales we tell ourselves.',
            'game': 'Assassin’s Creed: Revelations'
        }
    ]
    return choice(quotes)


if __name__ == "__main__":
    main()
