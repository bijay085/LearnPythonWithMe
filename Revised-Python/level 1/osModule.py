# Write a python program to print the contents of a directory using the os module.
# Search online for the function which does that. 

import os

def print_directory_contents(path):
    try:
        # Get the list of all files and directories in the specified path
        directory_contents = os.listdir(path)
        
        print(f"Contents of the directory '{path}':")
        for item in directory_contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
    except NotADirectoryError:
        print(f"The path '{path}' is not a directory.")
    except PermissionError:
        print(f"Permission denied to access '{path}'.")

# Specify the path to the directory
directory_path = '.'  # '.' refers to the current directory

print_directory_contents(directory_path)
