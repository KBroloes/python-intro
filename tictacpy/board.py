# This helps us save/load the class as a file (and thus our state)
import pickle
from .base_board import BaseBoard


# By far the easiest way to check the win conditions is to just map them out
win_conditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontals
                  [0, 3, 6], [1, 4, 7], [2, 5, 8], # Verticals
                  [0, 4, 8], [2, 4, 6] # Diagonals
                 ]

# A list of the pretty names for valid locations
# Note: The tests use this list for testing various functions. You can change the names, but need to expose the variable like this.
valid_locations = ['TopLeft', 'Top', 'TopRight',
                    'Left', 'Center', 'Right',
                    'BottomLeft', 'Bottom', 'BottomRight']

# The Board class you will be implementing
class Board(BaseBoard):
    # Initial state is None for each of the valid locations
    state = dict({'TopLeft': None, 'Top': None, 'TopRight': None,
                    'Left': None, 'Center': None, 'Right': None,
                    'BottomLeft': None, 'Bottom': None, 'BottomRight':None
                })
    current_move = 'X'

    def __init__(self):
        self.reset()


    def pass_turn(self):
        """ Passes the turn by setting the 'current_move' attribute to the other player

            Hint: Remember self. in front of class variables. """
        # Implement me!
        pass


    def available_locations(self):
        """ lists the locations on the board not yet occupied by a piece

            Hint: you can check if a value is taken by example:
                    self.state['Top'] is None
        """
        # Implement me!
        pass


    def set_piece(self, location):
        """ Sets a piece on the board for the current player.
            Parameters:
                location - the location on the board to set the piece
            Exceptions:
                Raises an exception if the location is invalid (already taken)

            Hint: Remember to validate if the location is taken in the state dict.
                  Dicts can be assigned using ie. self.state['Top'] = <value>
        """
        # Implement me!
        pass


    def reset(self):
        """ Resets the board so all locations are unoccupied and sets the current player to player 1 (X) """
        # Implement me!
        pass


    def display(self):
        """ Displays (prints) the current board state

            Hint: Remember it should be displayed as a 3x3 grid.
                You can loop over the items 3 by 3 in the state dict to accomplish this using the print function.

                Maybe replace "None" values with a blank string for the display?
                Example (but you can display how you want):
                X |   |
                    | O |
                    |   | X
        """
        # Implement me!
        pass


    def check_win_condition(self):
        """ Returns True if the win condition is met anywhere on the board.
            Note we only have to check the current player's token for each turn,
            as the other player will be checked on subsequent or previous turns.

            Hint: You need to check each of the win conditions.
                This is typically easiest just looping over the configurations in the start of this file:
                win_conditions.
                These are from values 0-8 from top left to bottom right in the 3x3 grid,
                so you need to translate to the pretty names we have in the state.
                You can use the valid_locations list for that.
            """
        # Implement me!
        pass


    def all_filled(self):
        """ Simply returns True if all spots are taken.
            Expects win condition to be checked elsewhere.

            Hint: Just check if all the spots are not None """
        # Implement me!
        pass


    def save(self, filename):
        """ Saves the board as a file

            Hint: Check the examples folder in the file_system.py for examples on how to save
        """
        # Implement me!
        pass


    @staticmethod
    def load(filename):
        """ Loads the board from file
            Returns:
                Board instance


            Hint: Check the examples folder in the file_system.py for examples on how to load
        """
        # Implement me!
        pass