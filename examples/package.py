# load module (Requires that the module supports it by exposing its functions)
import module

hello = module.Hello("Hello")
hello.say_hello()

# Import class from module
from module import module_class
hey = module_class.Hello("Hey!")
hey.say_hello()

# Import class from file
from classes import Hello
hi = Hello("Hi")
hi.say_hello()
