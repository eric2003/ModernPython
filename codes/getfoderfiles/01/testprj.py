import os

# Get the current working directory
current_dir = os.getcwd()
print("Current working directory:", current_dir)

# Get the parent directory
parent_dir = os.path.dirname(current_dir)
print("Parent directory:", parent_dir)

# Get the grandparent directory
grandparent_dir = os.path.dirname(parent_dir)
print("Grandparent directory:", grandparent_dir)