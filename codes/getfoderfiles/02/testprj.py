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

relative_path1 = os.path.relpath(parent_dir, current_dir)
relative_path2 = os.path.relpath(grandparent_dir, current_dir)

print("relative_path 1 directory:", relative_path1)
print("relative_path 2 directory:", relative_path2)