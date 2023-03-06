# suppose you want to sell your computer but you want to destroy all your files
# this script will destroy all files in a directory
# it will first change the contents then delete them

from pathlib import Path 

root_dir = Path('destination')      # defines the local root directory

for path in root_dir.glob("*.cvv"):        # careful, don't use rglob, it will go through subfolders.   
    with open(path, 'wb') as file:      # wb mode is write mode for binary files 
        file.write(b'0')                # write a zero to the file  
    path.unlink()                       # delete the file


