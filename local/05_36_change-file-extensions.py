from pathlib import Path
from datetime import datetime

# change file extension from .txt to .csv

root_dir = Path('files_36')  # defines the local root directory
file_paths = root_dir.glob("**/*")

for file in file_paths:
    if file.is_file():
        #print filename
        print(file)

        #get filename without extension
        filename_without_extension = file.stem
        
        #create new filename
        new_filename = filename_without_extension + ".csv"
        print("new filename is: ", new_filename)

        #create new file path
        new_filepath = file.with_name(new_filename)
        print("new_filepath is: ", new_filepath)

        #rename the file
        file.rename(new_filepath)
      


