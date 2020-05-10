is_true = True
number = 42
hello_string = "Hello world!"

format_string = f"Answer: {number}"
# > “Answer: 42”

print(format_string)

format_2= "Answer: {:.1f}".format(number)
# > “Answer: 42.0”

print(format_2)
