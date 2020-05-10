import sys
import os

from tictacpy import board

def setup_board():
    # Load from file if a file is passed from commandline
    file = parse_filename()
    if file is not None:
        return board.Board.load(file)

    print("File not found, starting new game...")
    return board.Board()


def parse_filename():
    """ Parses the commandline arguments for whether a filename was supplied """
    # You can do this better by using getopt for more advanced commandline parsing.
    # But this is fine for our purposes
    if len(sys.argv) == 2 and os.path.isfile(sys.argv[1]):
        return sys.argv[1]

    return None


def handle_save_and_exit():
        print("\nSaving game. Please choose a filename (or ctrl+c to skip):")
        try:
            file = input()
            game.save(file)
        except Exception as err:
            print(err)
        finally:
            sys.exit(0)

# We've executed this file from the commandline
if __name__ == "__main__":
    game = setup_board()

    # The game loop
    while True:
        try:
            print("\n===========================")
            print("To save & exit type: exit\n")

            game.display()

            print(f"The current player is: {game.current_move}")
            print(f"available locations: {game.available_locations()}")

            print("\nMake a move:")
            # Read input
            move = input()

            # If the selected move is invalid, try again (unless exit command)
            while move not in game.available_locations():
                if move == "exit":
                    handle_save_and_exit()
                print("Sorry, move invalid. Please try again:")
                move = input()

            # The move is valid, set it.
            game.set_piece(move)


            # If the game is over, display and exit
            if game.check_win_condition() == True:
                print(f"Congratulations player {game.current_move}!")
                game.display()
                break

            if game.all_filled() == True:
                print("What a shame. Noone won. Try again?")
                break

            # Otherwise, pass turn
            game.pass_turn()

        except KeyboardInterrupt:
            # Exit the game if we ctrl+c
            handle_save_and_exit()
