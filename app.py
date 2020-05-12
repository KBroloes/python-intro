import os
from flask import Flask, session, jsonify, redirect
from tictacpy.board import Board
import sys

app = Flask(__name__, static_url_path='')

# We can't really have a game loop, but we can have the session state instead!
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') or \
    'python_intro_2020_not_so_secret_key'


def save_state(game, end_condition=None):
    web_friendly_state = game.get_dict()
    web_friendly_state['end_condition'] = end_condition

    session['game_state'] = web_friendly_state

    # Let's just return the state again here since we use it a lot
    return web_friendly_state


@app.route('/')
def index():
    return redirect('/index.html')


@app.route('/create')
def create():
    # Let's just assume if you hit new game you wanna quit the old one
    # You could add a check for whether or not a game is in progress here.
    game = Board()

    # Get it ready to transfer over the wire (dict that jsonifies easily)
    web_friendly_state = save_state(game)
    return jsonify(web_friendly_state)


@app.route('/set_piece/<location>')
def set_piece(location):
    # Check if you have a game in session
    if "game_state" not in session:
        return "Game not found", 404

    game_state = session["game_state"]

    end_condition = game_state["end_condition"]

    # Check that the game hasn't already ended
    if end_condition is not None:
        return "Game has already ended", 400

    # Added an extra cool function to load from our session dict.
    game = Board.load_from_dict(game_state)

    try:
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

    # Pass in the end_condition in case it has changed
    web_friendly_state = save_state(game, end_condition)

    # If we just always return the state on success, the client doesn't need to make a new request
    return jsonify(web_friendly_state)


if __name__ == '__main__':
    app.run()