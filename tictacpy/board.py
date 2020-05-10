# This helps us save/load the class as a file (and thus our state)
import pickle
from .base_board import BaseBoard


# By far the easiest way to check the win conditions is to just map them out
win_conditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontals
                  [0, 3, 6], [1, 4, 7], [2, 5, 8], # Verticals
                  [0, 4, 8], [2, 4, 6] # Diagonals
                 ]

# A list of the pretty names for valid locations
# Note: The tests use this list for testing various functions. You can change the names, but need to expose the variable.
valid_locations = ['TopLeft', 'Top', 'TopRight',
                    'Left', 'Center', 'Right',
                    'BottomLeft', 'Bottom', 'BottomRight']

# The Board class you will be implementing
class Board(BaseBoard):
    def __init__(self):
        self.reset()



    def _get_display_value(self, value):
        if value is None:
            return ' '
        else:
            return value


    def pass_turn(self):
        """ Passes the turn by setting the 'current_move' attribute to the other player """
        if self.current_move == 'X':
            self.current_move = 'O'
        else:
            self.current_move = 'X'


    def _valid_location(self, location):
        return self.state[location] is None


    def available_locations(self):
        """ lists the locations on the board not yet occupied by a piece """
        # Filter by value == None, return the key.
        return list(map(lambda x: x[0], filter(lambda x: x[1] is None, self.state.items())))


    def set_piece(self, location):
        """ Sets a piece on the board for the current player.
            Parameters:
                location - the location on the board to set the piece
            Exceptions:
                Raises an exception if the location is invalid (already taken)
        """
        if self._valid_location(location):
            self.state[location] = self.current_move
        else:
            raise Exception(f"Bad location {location} for player {self.current_move}")


    def reset(self):
        """ Resets the board so all locations are unoccupied and sets the current player to player 1 (X) """
        # Create the board state as a dictionary with values from 0-8 (positions of the board)
        # All initialized with None values
        self.state = dict([(i, None) for i in valid_locations])

        # Whose turn is it?
        self.current_move = 'X'


    def display(self):
        """ Displays (prints) the current board state """
        # Convert dict values to list
        values = list(self.state.values())
        for i in range(3):
            # Let's learn about slices:
            current_position = i*3
            next_three = current_position+3

            # Create a slice of three elements (one row) using [a:b]
            row = values[current_position:next_three]
            # Use a list comprehension to convert None to ' '
            row = [self._get_display_value(value) for value in row]

            print(row)


    def _all_met(self, condition):
        """ This is a reduce function as a loop.
            Returns true if all locations in a win condition are occupied by the current player
        """
        all_set = True
        for location in condition:
            # Translate to the pretty locations
            loc = valid_locations[location]

            # Figure out if the current player symbol is set
            all_set = all_set and (self.state[loc] == self.current_move)

        return all_set


    def check_win_condition(self):
        """ Returns True if the win condition is met anywhere on the board.
            Note we only have to check the current player's token for each turn,
            as the other player will be checked on subsequent or previous turns. """

        for condition in win_conditions:
            if self._all_met(condition):
                return True

        return False


    def all_filled(self):
        """ Simply returns True if all spots are taken.
            Expects win condition to be checked elsewhere. """
        for item in self.state.values():
            if item is None:
                return False

        return True


    def save(self, filename):
        """ Saves the board as a file """
        with open(filename, 'wb') as f:
            pickle.dump(self, f)


    @staticmethod
    def load(filename):
        """ Loads the board from file
            Returns:
                Board instance
        """
        with open(filename, 'rb') as f:
            return pickle.load(f)