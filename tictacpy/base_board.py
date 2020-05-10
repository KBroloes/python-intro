import abc

# The Board class you will be implementing
class BaseBoard(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def pass_turn(self):
        """ Passes the turn by setting the 'current_move' attribute to the other player """
        raise NotImplementedError("pass_turn not yet implemented")

    @abc.abstractmethod
    def available_locations(self):
        """ lists the locations on the board not yet occupied by a piece """
        raise NotImplementedError("available_locations not yet implemented")

    @abc.abstractmethod
    def set_piece(self, location):
        """ Sets a piece on the board for the current player.
            Parameters:
                location - the location on the board to set the piece
            Exceptions:
                Raises an exception if the location is invalid (already taken)
        """
        raise NotImplementedError("set_piece not yet implemented")

    @abc.abstractmethod
    def reset(self):
        """ Resets the board so all locations are unoccupied and sets the current player to player 1 (X) """
        # Create the board state as a dictionary with values from 0-8 (positions of the board)
        # All initialized with None values
        raise NotImplementedError("reset not yet implemented")

    @abc.abstractmethod
    def display(self):
        """ Displays (prints) the current board state """
        raise NotImplementedError("display not yet implemented")

    @abc.abstractmethod
    def check_win_condition(self):
        """ Returns True if the win condition is met anywhere on the board.
            Note we only have to check the current player's token for each turn,
            as the other player will be checked on subsequent or previous turns. """

        raise NotImplementedError("check_win_condition not yet implemented")

    @abc.abstractmethod
    def all_filled(self):
        """ Simply returns True if all spots are taken.
            Expects win condition to be checked elsewhere. """
        raise NotImplementedError("all_filled not yet implemented")

    @abc.abstractmethod
    def save(self, filename):
        """ Saves the board as a file """
        raise NotImplementedError("save not yet implemented")


    @classmethod
    @abc.abstractmethod
    def load(filename):
        """ Loads the board from file
            Returns:
                Board instance
        """
        raise NotImplementedError("load not yet implemented")