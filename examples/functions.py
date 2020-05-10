# Functions
def hello(message):
    print(message)

hello("Hello")
# > “Hello”

def hello_default(message="Hello world"):
    print(message)

hello_default()
# > “Hello world”

def add(a, b):
    return a + b

def multi_return(a, b):
    return b, a

b, a = multi_return(1, 2)


# Lambdas
adder = lambda x: x + 2
multiply = lambda x, y: x * y

# Call lambda
adder(10)
# > 12

# Call lambda with two parameters
multiply(4, 5)
# > 20

## Pass lambda as parameter
def run(a, fn):
    return fn(a)

run(2, adder)
# > 4