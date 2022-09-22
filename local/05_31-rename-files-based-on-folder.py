from pathlib import Path 
root_dir = Path('files')
file_paths = root_dir.glob("**/*")

for path in file_paths:
    if path.is_file():          # checks if it's a file returns true 
        # print(path)
        # get the name of the folder the file is in:
        parent_folder = path.parts[-2]
        #print(parent_folder)
        
        new_filename = parent_folder + '-' + path.name
        print(new_filename)

        new_filepath = path.with_name(new_filename)     # creaeting a new path object here 
        path.rename(new_filepath)                                   # apply rename to the path object
