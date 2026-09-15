"""
Candy Realm

A command-line board game where players move through a candy-themed board
by drawing cards that match the colors on the board.
"""

import random


BOARD = [
    "START!", "B", "R", "V", "X", "O", "S", "P", "Y",
    "B", "R", "V", "X", "O", "P", "E", "Y", "B",
    "R", "V", "X", "O", "P", "Y", "GOAL!"
]

CARD_COLORS = ["B", "R", "V", "O", "P", "Y", "X", "S"]


def show_rules():
    """Display the rules for Candy Realm."""
    print()
    print("The Rules to Candy Realm!")
    print("1. Move through the board by matching drawn cards to board spaces.")
    print("2. Four total players participate. You can choose 1-4 human players;")
    print("   any remaining players are controlled by the computer.")
    print("3. Players begin at START and move forward to matching colors.")
    print("4. Before each game, choose how many copies of each card to include.")
    print("   You can choose between 1 and 5 copies per card.")
    print("5. Special spaces:")
    print("   X = Unlucky Rubber Ducky: skip your next turn.")
    print("   S = Quick Slide: move immediately to the E space.")
    print("6. The first player to reach GOAL wins!")
    print()


def create_deck():
    """Create, shuffle, and return a new deck of cards."""
    while True:
        copies = input(
            "How many copies of each card would you like? (1-5): "
        ).strip()

        try:
            copies = int(copies)
        except ValueError:
            print("Please enter a number between 1 and 5.")
            continue

        if not 1 <= copies <= 5:
            print("Please choose a number between 1 and 5.")
            continue

        deck = []
        for color in CARD_COLORS:
            deck.extend([color] * copies)

        random.shuffle(deck)
        return deck


def create_players():
    """Create four players based on the selected number of human players."""
    while True:
        human_count = input(
            "How many HUMAN players are going to play (1-4)? "
        ).strip()

        try:
            human_count = int(human_count)
        except ValueError:
            print("Please enter a number between 1 and 4.")
            continue

        if not 1 <= human_count <= 4:
            print("Please choose a number between 1 and 4.")
            continue

        break

    players = []

    for number in range(1, human_count + 1):
        players.append(
            {
                "player": f"Player {number}",
                "position": 0,
                "unlucky": False,
                "type": "human",
            }
        )

    for number in range(1, 5 - human_count):
        players.append(
            {
                "player": f"AI {number}",
                "position": 0,
                "unlucky": False,
                "type": "ai",
            }
        )

    return players


def display_board(board, players):
    """Display the board and the current position of each player."""
    print("=" * 67)

    for player_number, player in enumerate(players, start=1):
        row = ""
        for position in range(len(board)):
            if player["position"] == position:
                row += f"{player_number} "
            else:
                row += "  "
        print(row)

    print("-" * (len(board) * 2))
    print(" ".join(space[0] for space in board))
    print("=" * 67)


def find_next_color(board, position, card_color):
    """Return the next board position matching the drawn card."""
    for next_position in range(position + 1, len(board)):
        if board[next_position] == card_color:
            return next_position

    return -1


def get_human_action():
    """Ask a human player whether to draw or shuffle the deck."""
    while True:
        choice = input(
            "Do you want to [D]raw a card or [S]huffle the deck? "
        ).strip().upper()

        if choice in {"D", "S"}:
            return choice

        print("Please enter D to draw or S to shuffle.")


def play_game():
    """Run a complete game of Candy Realm."""
    board = BOARD.copy()
    players = create_players()
    deck = create_deck()
    winner = None

    while winner is None:
        for player in players:
            display_board(board, players)
            print(f"It is {player['player']}'s turn!")

            if player["unlucky"]:
                print(
                    "Unlucky Rubber Ducky! "
                    "This player must skip this turn."
                )
                player["unlucky"] = False
                input("Press Enter to continue...")
                continue

            if not deck:
                print("The deck is empty. Creating a new deck!")
                deck = create_deck()

            if player["type"] == "human":
                while True:
                    action = get_human_action()

                    if action == "S":
                        print("Shuffling the deck!")
                        random.shuffle(deck)
                        input("Press Enter to continue...")
                        break

                    current_position = player["position"]
                    card = deck.pop(0)
                    print(f"{player['player']} drew a {card} card!")

                    next_position = find_next_color(
                        board, current_position, card
                    )

                    if next_position == -1:
                        if current_position == len(board) - 2:
                            print(
                                "You're right in front of the GOAL! "
                                "Moving to the goal!"
                            )
                            player["position"] = len(board) - 1
                        else:
                            print(
                                "No matching space remains ahead. "
                                "Drawing another card..."
                            )
                            continue
                    else:
                        player["position"] = next_position

                    break

                # Shuffling ends the player's turn.
                if action == "S":
                    continue

            else:
                print(f"{player['player']} (AI) is drawing a card...")
                current_position = player["position"]

                while True:
                    if not deck:
                        print("The deck is empty. Creating a new deck!")
                        deck = create_deck()

                    card = deck.pop(0)
                    print(f"{player['player']} drew a {card} card!")

                    next_position = find_next_color(
                        board, current_position, card
                    )

                    if next_position == -1:
                        if current_position == len(board) - 2:
                            player["position"] = len(board) - 1
                            break

                        print(
                            "No matching space remains ahead. "
                            "Drawing another card..."
                        )
                        continue

                    player["position"] = next_position
                    break

            landed_on = board[player["position"]]

            if landed_on == "X":
                print(
                    "Unlucky Rubber Ducky! "
                    "This player will skip their next turn."
                )
                player["unlucky"] = True

            elif landed_on == "S":
                print("Quick Slide! Moving to the E space!")
                player["position"] = board.index("E")

            if player["position"] == len(board) - 1:
                winner = player
                break

            input("Press Enter to continue to the next turn...")

    print("*" * 67)
    print(f"CONGRATULATIONS, {winner['player']}! YOU WIN CANDY REALM!")
    print("*" * 67)


def main():
    """Run the Candy Realm main menu."""
    while True:
        print("=" * 51)
        choice = input(
            "What would you like to do? "
            "[P]lay, [L]earn the rules, or [Q]uit: "
        ).strip().upper()

        if choice == "P":
            play_game()
        elif choice == "L":
            show_rules()
        elif choice == "Q":
            print("Thanks for playing Candy Realm!")
            break
        else:
            print("Please enter P, L, or Q.")


if __name__ == "__main__":
    main()
