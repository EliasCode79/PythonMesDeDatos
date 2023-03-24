# When you start a program using python3, you assign it the name of the file to be started. You can also assign it a set of arguments: data that the program will have access to when it executes. This is what it can look like:

# python3 backup.py 2023-01-01

# Command line arguments
#How are these commands captured from a coding perspective? Using the sys module, you can retrieve command line arguments and use them in the program. Note the code below:

import sys

print(sys.argv)
print(sys.argv[0]) # program name
print(sys.argv[1]) # first argument

# python3 05_command_line_input 2022-05-11