from pathlib import Path
import zipfile

root_dir = Path('files_40')                     # defines the local root directory
#root_dir = Path('.') # if the files are in the same working directory as the script

#lets also define destination dir/path 
destination_path = Path('destination')

for path in root_dir.glob("*.zip"):                         #rglob will go inside each of the folders, rglob is recursive glob
    with zipfile.ZipFile(path, 'r') as zf:                  #zf is the zip file object, 'r' is the mode for read, 'w' is the mode for write
        final_path = root_dir / destination_path / Path(path.stem)     # path.stem is the name of the file without the extension                                               
        zf.extractall(path=final_path)                      #this is the method that extracts the files            
