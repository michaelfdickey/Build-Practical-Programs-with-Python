from pathlib import Path
import zipfile

root_dir = Path('files_39')                     # defines the local root directory

#archive_path = Path('archive.zip')              # defines the archive file name and creates a Path object
                                                # add 'root_dir /' to make it files/archives.zip
                                                # add 'root_dir / archive_path' to make it files/files_39/archive.zip

archive_path = root_dir / Path('archive.zip')   # defines the archive file name and creates a Path object

with zipfile.ZipFile(archive_path, 'w') as zip_object:         # creates a ZipFile object, 'w' is the mode for write. 
                                                               # ok what do we want to do with this object? probably iterate through it
    for path in root_dir.rglob("*.txt"):                       # iterate through all the files in the root_dir
        zip_object.write(path)
        path.unlink()                                         # delete the file after it's been added to the archive

    


#

