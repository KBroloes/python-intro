from setuptools import setup, find_packages

# Layout & format inspired from https://github.com/navdeep-G/samplemod/blob/master/setup.py

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='TicTacPy',
    version='0.1.0',
    description='An implementation of TicTacToe in Python',
    long_description=readme,
    author='Kevin Broløs',
    author_email='kevin.broloes@abzu.ai',
    url='https://github.com/KBroloes/python-intro', #/tictacpy for solution suggestions
    license=license,
    packages=find_packages(exclude=('tests'))
)