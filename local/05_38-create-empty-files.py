from pathlib import Path 

# set root directory
root_dir = Path('files_38')                     # defines the local root directory

for i in range(20,31):                          # creates 10 files with numbers from 10 - 21
    filename = str(i) + '.txt'                  # construct a filename as a string
    filepath = root_dir / Path(filename)        # construct a filepath as a Path object
    filepath.touch()                            # create an empty file

    


