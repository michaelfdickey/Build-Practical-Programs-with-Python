# file names should contain folder and parent / grandparent folders

from pathlib import Path

root_dir = Path('files')  # defines the local root directory

#print(root_dir)
#print(type(root_dir))
#print("file_paths is: ", file_paths)
#print("printing list(file_paths)")
#print(list(file_paths))

#file_paths = root_dir.iterdir()
file_paths = root_dir.glob("**/*")

for path in file_paths:
    if path.is_file():  # only if it's a file print on it or act on it
        print(path)
        parent_folder = path.parts[-3:-1]
        print("parent folder is: ", parent_folder)

        #construct new filename
        new_filename = parent_folder[0] + "-" + parent_folder[1] + "-" + path.name
        print("new_filename is: ", new_filename)

        #construct new filepath
        new_filepath = path.with_name(new_filename)  # creating a new path object here
        print("new_filepath is: ", new_filepath)

        path.rename(new_filepath)
