from pathlib import Path
from datetime import datetime
# update file names with datetime created:

root_dir = Path('files')  # defines the local root directory
file_paths = root_dir.glob("**/*")

for path in file_paths:
    #print(path)
    if path.is_file():  # only if it's a file print on it or act on it
        print(path)
        #print(type(path))
        file_stats = path.stat()
        #print(file_stats)

        # get time stampe when created
        seconds_when_created = file_stats.st_ctime
        #print(seconds_when_created)

        #convert epoch timestamp
        date_created = datetime.fromtimestamp(seconds_when_created)
        #print(date_created)

        #format date created string
        date_created_str = date_created.strftime(
            "%Y-%m-%d_%H:%M:%S")  # creates a string from time
        print(date_created_str)

        #create new filename
        new_filename = date_created_str + "-" + path.name
        print("new filename is: ", new_filename)

        #create new file path
        new_filepath = path.with_name(new_filename)
        print("new_filepath is: ", new_filepath)

        #rename the file
        path.rename(new_filepath)
