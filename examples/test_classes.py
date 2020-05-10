import unittest
from .classes import Hello

class TestClasses(unittest.TestCase):
    """Test cases for the Hello class"""

    def test_greet(self):
        hello = Hello("Hey!")
        greeting = hello.greet("Bob")

        assert greeting is not None, "Greeting should be set"
        assert greeting == "Hey! Bob", "Greeting should be 'Hey! Bob'"
