import os

# Using the with keyword ensures file is properly closed after access
with open('tempfile', 'w') as f:
    f.writelines("Hello World")

# Check file exists
if os.path.isfile('tempfile'):
    with open('tempfile', 'r') as f:
        # Reads lines as array
        message = f.readlines()

    print(message)
    # > "Hello World"

    # Cleaning up
    os.remove('tempfile')


# Python class serialization
import pickle

class Person():
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def save(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @staticmethod
    def load(filename):
        """ Loads the class from file"""
        with open(filename, 'rb') as f:
            return pickle.load(f)

person = Person(32, "Kevin")
person.save("person")

loaded_person = Person.load("person")
print(loaded_person.age, loaded_person.name)
# > 32, Kevin

# Cleaning up
if os.path.isfile("person"):
    os.remove("person")