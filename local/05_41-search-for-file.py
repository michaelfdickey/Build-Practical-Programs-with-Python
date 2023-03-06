# search a destination folder for a specific file

from pathlib import Path

# how do you get the abolute path of a file?
#path = Path('destination/items1/10.csv')
#print(path.absolute())

# output example:
###
#$ python 05_41-search-for-file.py
#C:\Files\MFD Personal\Programming\python\Udemy\Build-Practical-Programs-with-Python\local\destination\items1
#10.csv
###

# prompt for string to search for in files
search_string = input('Enter a string to search for: ')
print(" search string is: ", search_string)

#root_dir = Path('destination')      # defines the local root directory
#file_paths = root_dir.glob("**/*")

# get a list of all files in the directory
#for file in file_paths:
#    if file.is_file():
#        print(file)
                          
# find only the files that contain the search string

root_dir = Path('destination')      # defines the local root directory
file_paths = root_dir.glob("**/*")

for file in file_paths:
    if file.is_file():
        #print(" path is: ", file, " file name is: ", file.name)
        if search_string in file.name:
            print(" found: ", file.name)
            print(file.absolute())


