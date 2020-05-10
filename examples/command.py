import sys

print(sys.argv)
# > filename.py arg1, arg2, arg3

if len(sys.argv) == 4:
    first_arg = sys.argv[1] # Skipping the filename
    second_arg = sys.argv[2]
    third_arg = sys.argv[3]
    print(first_arg, second_arg, third_arg)
else:
    print("You need to supply three arguments when running this file")

# Usage: foo@bar:~$ python3 filename.py first_arg second_arg 42