# Introduction to Python

Welcome to the course. Together, we'll go through a small and fun project to learn more about how to build python modules. Finally, we'll expose what we've built in this python module as a web server to bring to the world wide interwebs.

# TL;DR

**`board.py` is where you'll be implementing all your code.**

`pip3 install -r requirements.txt` to install requirements

`nosetests` to run the tests

`python3 game.py` to run the game using your current implementation from `board.py`

# Description

The course is in two segments: The module. and the web server.

During the course of this project, we'll explore how to setup a python project, how to write pythonic code, and all the usual suspects like data structures, control flows, error handling, file system access, etc.

The project itself will be to implement a playable version of Tic-Tac-Toe in Python.

For this to be fun to play, we have some general concepts we need to fulfill:

# Tic-Tac-Py features

- We need to be able to print the game board
- We need to be able to show whose turn it is
- We can receive player input
- We can place a piece according to player input on the 3x3 Tic-Tac-Toe grid
- We can validate that the position is valid
    - And ask for new input if not valid
- We can check the win condition (Either three in a row vertically, horizontally or diagonally)
    - We can end the game if the win condition is met
    - We can show a "Congratulations" notification on win to the right player
    - We print the final game board and show the winning combination
- We can detect a stalemate
- We can reset the game state
- We can show available locations
- We can save the game state for later
- We can pass the turn
- We can exit/resume the game

Phew, what a list! Fortunately, it's entirely up to us how we solve this.

# Project structure

When you check out this project, a template structure will already have been made ready for you to get started. This is compiled from a few best-practice advice on how to build python projects. You can structure projects in many ways, but this is chosen to be useful for modular code.

The structure is like this:

    Tic-Tac-Py
        |
        |.. game.py (the game runner)
        |-- README.md (you are here!)
        |-- setup.py
        |-- requirements.txt
        |-- LICENSE
        |-- examples (this folder has all the example code for learning)
        |-- tictacpy
            |-- __init__.py
            |-- board.py
            |-- tests
                |-- __init__.py
                |-- test_board.py


## The Module

Tictacpy contains a `board.py` and `base_board.py`. The Board class is used by `game.py` (top level), and inherits the abstract class `BaseBoard.py`. This is honestly not something you'll be doing a lot in Python except for specific use-cases. We're doing it to print nice errors if the functions aren't implemented, since we have a hard contract between `game.py`, our tests and the implementation of `board.py`.

**`board.py` is where you'll be implementing all your code. So take some time to familiarize yourself with it, and the tests**

## The Web Server

The web server consists of two parts, the `app.py` and a folder called `static` with some simple javascript and html. The `app.py` has the basic game flow implemented using flask, and just requires you to implement the functions to get it working.

# Testing

We're using the builtin unittest framework of python, as well as the package `nose` to help us find and execute tests. After installing requirements, you can run `nosetests` to execute all the tests

To execute all tests, run:

`nosetests` in the main directory, and it'll give you a status of which tests pass and fail so you know when you're done implementing the board functionality.

# Examples

This folder has a bunch of python example files exemplifying how different features of the language works. I definitely recommend taking a look in here while implementing your own board.py logic.

Recommended reading order:

* package.py
* variable.py
* classes.py
* lists.py
* dictionaries.py
* if.py
* loops.py
* functions.py
    *  map_filter.py
* file_system.py
* exceptions.py
* command.py
* test_classes.py

All of the examples can be executed by typing `python3 examples/example_name.py`

None of these are mandatory and you should be able to complete the exercises fine without using all of these features if you get stuck on one or more of them.

# Further information about the project files

Note the root level has this README file, a setup.py, requirements.txt and a LICENSE file.

__setup.py__ is the standard file for installing python packages. When you run it, it will install your package using the Python distribution system so you can run them with a system command. We're using a simplified version, but this is also the file that you'll use to configure how to publish your package on the public repositories (using what's called wheels). We won't go through that in this course, but [here's](https://github.com/navdeep-G/setup.py) some recommended reading for when you're interested in how you could go about it.

For now, know that you can install this package in your local python environment using `pip install .`, which will allow you to `from tictacpy import board`. This is not necessary to just work with this module within this package, but for larger software projects with multiple modules, you might want to distribute it like this to be used in a separate context.

__requirements.txt__ is your list of package dependencies, and using pythons package manager `pip` (or `pip3` if you have multiple versions of python) will use this list to install the necessary requirements to run your module. Our file includes only dependencies on the `flask` web server and `nose` (for running tests).

The LICENSE file is self-explanatory, and is all the legalese about the software license you're operating under. This field is big enough to warrant an entire course on its own. I've chosen the MIT license, which is popular for many projects on `Github`, due to its leniency in how it's both being used commercially and privately, and also regards to compatibility with other licenses.

Then we have the module itself: __tictacpy__.

You'll notice it's just a folder with a special kind of file inside, the *\_\_init\_\_.py*. This file is responsible for telling the python package loader that this folder is a package that exposes the files/classes found inside.

This allows you to say `from tictacpy import core` and you'll have it all loaded.

Code put inside the `__init__.py` files will be executed every time parts of the module is loaded. The recommended default is that these files are empty and exist for structural purposes only unless you have a specific need for initialization logic (such as exposing internals so you can import the whole package with `import module`).

There's also a __tests__ folder inside, containing any and all tests that you may have for ensuring the robustness of your code. It has the same structure as above with an *\_\_init\_\_.py* file, as well as a file called test_<file_under_test>.py by convention. This allows automatic test frameworks to find the tests you have for your project and automatically run them - as well as helps you figure out exactly what is under test.
