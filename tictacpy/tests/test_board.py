from ..board import Board, win_conditions, valid_locations

import unittest
import os


class TestBoard():
    """Test cases for the board"""

    # We'll use this location whenever testing setting a piece. This way is chosen to give freedom to change the names in the board
    test_location = valid_locations[0]

    def test_initializes_correctly(self):
        board = Board()

        # Use a python list comprehension to build the expected state from the valid locations.
        expected_state = dict([(location, None) for location in valid_locations])

        assert board.state == expected_state, f"Expected {board.state} to equal {expected_state}"

    stalemate = {'X': [0, 1, 3, 4, 8], 'O':[2, 5, 6, 7]}
    def test_stalemate(self):
        board = Board()

        fill_board(board, self.stalemate['X'], 'X')
        fill_board(board, self.stalemate['O'], 'O')

        assert board.all_filled() == True, "expected stalemate"

    def test_not_stalemate(self):
        board = Board()

        fill_board(board, self.stalemate['X'], 'X')
        fill_board(board, self.stalemate['O'], 'O')
        # clear one field
        board.state[self.test_location] = None

        assert board.all_filled() == False, "expected not stalemate"

    def test_available_locations(self):
        board = Board()

        assert board.available_locations() == valid_locations

    def test_available_locations_with_some_set(self):
        board = Board()

        board.state[self.test_location] = 'X'

        assert board.available_locations() == valid_locations[1:] # Slice away the first element we set

    def test_set_piece(self):
        board = Board()

        board.set_piece(self.test_location)

        assert board.state[self.test_location] == board.current_move, "Expected location to be set to current player"

    def test_set_piece_fails_if_already_set(self):
        board = Board()

        board.state[self.test_location] = 'X'


        # Note, the good way would be to use self.assertRaised
        # But since we're not inheriting from unittest.TestCase (because we're using generators)
        # We have to implement this behaviour ourselves.
        raised = False
        try:
            board.set_piece(self.test_location)
        except Exception:
            raised = True
        finally:
            if not raised:
                assert False, "Expected exception to be raised"


    def test_pass_turn(self):
        board = Board()

        assert board.current_move == 'X', "Expected current player to be X"

        board.pass_turn()

        assert board.current_move == 'O', "Expected current player to be O"

        board.pass_turn()

        assert board.current_move == 'X', "Expected current player to be X"


    def test_display(self):
        board = Board()

        # fake a state:
        for location in win_conditions[0]:
            board.state[valid_locations[location]] = 'X'

        for location in win_conditions[5]:
            board.state[valid_locations[location]] = 'O'

        board.display()

        # Note this doesn't actually test that it prints correctly, just that the code runs
        # You can comment out the below line to make it fail and print:
        #assert False

    def test_save_and_load(self):
        """ This depends on other features working, like setting pieces and passing the turn """
        board = Board()
        filename = 'test_save_and_load.tst'

        try:
            board.set_piece(self.test_location)
            board.pass_turn()
            board.save(filename)

            loaded_board = Board.load(filename)

            assert board.current_move == loaded_board.current_move, "Board current move (player) not equal after saving and loading"
            assert board.state == loaded_board.state, "Board states not equal after saving and loading"

        finally:
            if os.path.exists(filename):
                os.remove(filename)

    # An example of testing using python generators:
    # test generators must yield tuples,
    # the first element of which must be a callable and
    # the remaining elements the arguments to be passed to the callable.
    def test_win_conditions(self):
        for condition in win_conditions:
            # This generates a test case for each condition
            yield assert_win_condition, condition, True


    non_win_conditions = [[], [1, 3, 4], [0, 5, 6], [5, 7, 8], [0, 2, 4]]
    def test_non_win_conditions(self):
        for condition in self.non_win_conditions:
            # This generates a test case for each condition
            yield assert_win_condition, condition, False



# helper functions for the tests

def fill_board(board, locations, player):
    # fake a state:
    for location in locations:
        board.state[valid_locations[location]] = player


def assert_win_condition(win_condition, expectation):
        board = Board()
        fill_board(board, win_condition, 'X')

        actual, expected = board.check_win_condition(), expectation

        assert actual == expected, f"Expected {actual} to be {expected}"

if __name__ == '__main__':
    unittest.main()