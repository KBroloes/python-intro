import os
from flask import Flask, session, jsonify, redirect
from tictacpy.board import Board
import sys

app = Flask(__name__, static_url_path='')

# We can't really have a game loop, but we can have the session state instead!
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') or \
    'python_intro_2020_not_so_secret_key'

@app.route('/')
def index():
    return redirect('/index.html')

def save_state(game, end_condition=None):
    """ Saves the game state in the session and return it again """
    ## Your code goes here:


    # Let's just return the state again here since we use it a lot
    return session['game_state']

@app.route('/create')
def create():
    """ Create a new game, save the state in the session and return it as json to the client """
    # Let's just assume if you hit new game you wanna quit the old one
    # You could add a check for whether or not a game is in progress here.
    game = Board()

    # Get it ready to transfer over the wire (dict that jsonifies easily)
    web_friendly_state = save_state(game)
    return jsonify(web_friendly_state)

def has_ended(game):
    """ Returns True if ended, False otherwise """
    # Your code goes here
    return True


def game_exists(session):
    """ Returns True if exists, False otherwise """
    # Your code goes here
    return False

def get_board_from_state(game_state):
    """ Returns a board instance with the state initialized from the saved
        session dict. """
    # Your code goes here
    return Board()


@app.route('/set_piece/<location>')
def set_piece(location):
    # First, check if you have a game in the session storage

    # Check if you have a game in session
    if game_exists(session):
        return "Game not found", 404

    game_state = session['game_state']

    # Then recreate the game board class from the dict state
    game = get_board_from_state(game_state)

    # Make sure the game isn't already over and return a 400
    if has_ended(game):
        return "Game has already ended", 400

    end_condition = None

    # Check that the game hasn't already ended
    if end_condition is not None:
        return "Game has already ended", 400

    try:
        # We already know this stuff
        game.set_piece(location)

        # Let's just check the state here, and add an attribute constant
        if game.check_win_condition():
            end_condition = "PLAYER_WIN"
        elif game.all_filled():
            end_condition = "DRAW"
        else:
            game.pass_turn()
    except Exception:
        # Normally, you'd like a custom exception specifically for invalid locations.
        return "Invalid location, or location already taken", 400

    # Pass in the end_condition in case it has changed so we can save it on the session
    # instead of doing the above check all the time
    web_friendly_state = save_state(game, end_condition)

    # If we just always return the state on success, the client doesn't need to make a new request to get the board
    return jsonify(web_friendly_state)


if __name__ == '__main__':
    app.run()