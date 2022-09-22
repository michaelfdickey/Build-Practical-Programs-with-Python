from pathlib import Path

# how do you rename files in a path 

root_dir = Path('files')            # create a Path object instance with files as a string 
file_paths = root_dir.iterdir()     # this method outputs a file generator 
#print(list(file_paths))             # prints the files in the directory

for path in file_paths:
    new_filename = "new_" + path.stem + path.suffix
    new_filepath = path.with_name(new_filename)         #give me that path with a new name
    print(new_filename)
    path.rename(new_filepath)

"""
we're about to add path.rename(new_filepath) to the for loop
so rename is a class of the path object and takes the argument (new_filepath)
but if we do this, the files actually move up outside the file path
instead we point to path.with_name
"""