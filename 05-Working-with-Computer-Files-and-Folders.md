# 5 Working with Computer Files and Folders





## 29. intro to python pathlib library

using the pathlib library

standard of python - installed by default

first showed up in v 3.4 substitute of the os library

both os and pathlib are useful for file and directory operations

os treats filepaths as strings but pathlib use a path object type

- paths used to be treated as strings

first you need to think of the path:

```
p1 = 'files/abc.txt'
with open(p1, 'r') as file:
 print(file.read())
```

- now pathlib recognizes paths as object types

```
from pathlib import Path

p1 = Path('files/abc.txt')
print(type(p1))
print(p1)
```

```
$ python local/04-29_python_pathlib_library.py
<class 'pathlib.WindowsPath'>
files\abc.txt

```

benefits not visible in this example but if your code expands 

it has many methods you can check methods with Dir(Path):

![image-20220905182704363](images/image-20220905182704363.png)

```
# you can also write files if the file doesn't exist
p1 = Path('new_file.txt')

if not p1.exists():
    with open(p1, 'w') as file:
        file.write('file_contents')
```

you can print just the filename:

`print(p1.name)`

get filename without extension

`print(p1.stem)`

or just extension

`print(p1.suffix)`

it's much more work to do this with os.path, these are all methods of the Path class

```
from pathlib import Path

# reading files:
#p1 = Path('files/abc.txt')
#print(type(p1))
#print(p1)

# you can also write files if the file doesn't exist
p1 = Path('new_file.txt')

if not p1.exists():
    with open(p1, 'w') as file:
        file.write('file_contents')

#you can print just the filename:
print(p1.name)

# get filename without extension
print(p1.stem)

# or just extension
print(p1.suffix)

#it's much more work to do this with os.path, these are all methods of the Path class

# let's print the filename of files in a directory
p2 = Path('files')
print(p2.iterdir())
for item in p2.iterdir():
    print(item)
```



## 30. Add prefix to all filenames in a folder

first, determine where / in what folders these files are, what is the root directory holding the files

need to run it from the right folder (not local/*.py)

![image-20220911175135181](images/image-20220911175135181.png)

lets start with:

```
from pathlib import Path

# how do you rename files in a path 

root_dir = Path('files')            # create a Path object instance with files as a string 
file_paths = root_dir.iterdir()     # this method outputs a file generator 
print(list(file_paths))             # prints the files in the directory
```

outputs:

![image-20220911175135181](images/image-20220911175135181.png)



let's list all the files:

```
from pathlib import Path

# how do you rename files in a path 

root_dir = Path('files')            # create a Path object instance with files as a string 
file_paths = root_dir.iterdir()     # this method outputs a file generator 
#print(list(file_paths))             # prints the files in the directory

for path in file_paths:
    new_filename = "new_" + path.stem + path.suffix  
    print(new_filename)
```

result:

```
Matus1976@DESKTOP-98E2DP4 MINGW64 /d/Files - Google Drive/Files - New Merged/MFD Personal/Programming/python/Udemy/Build-Practical-Programs-with-Python/local (main)
$ python 04_30-add-prefix.py
new_abc.txt
new_def.txt
new_mark.item
```



this is just printing to the screen with the new name, they are not renamed. 

you need to use class path.with_name(new_filename)

```
from pathlib import Path

# how do you rename files in a path 

root_dir = Path('files')            # create a Path object instance with files as a string 
file_paths = root_dir.iterdir()     # this method outputs a file generator 
#print(list(file_paths))             # prints the files in the directory

for path in file_paths:
    new_filename = "new_" + path.stem + path.suffix
    new_filepath = path.with_name(new_filename)
    print(new_filename)
    path.rename(new_filepath)

"""
we're about to add path.rename(new_filepath) to the for loop
so rename is a class of the path object and takes the argument (new_filepath)
but if we do this, the files actually move up outside the file path
instead we point to path.with_name
"""
```





# 31 - Rename All Files Based on Folder

going to rename all files in a folder to the prefix of the folder

e.g. a bunch of files in \November and a bunch in \December and then adding the name of the folder to each file, so \November\abc.txt will be renamed to \November\November-abc.txt

start with the Path module, defining the root dir and instantiating the file_paths class:

```
from pathlib import Path 

root_dir = Path('files')

file_paths = root_dir.iterdir()

for path in file_paths:
    print(path)
```

![image-20220921173726668](images/image-20220921173726668.png)

get the list of files inside each folder:

```
from pathlib import Path 
root_dir = Path('files')
file_paths = root_dir.iterdir()

for path in file_paths:
    for filepath in path.iterdir():     # gives list of files inside current folder
        print(path)
```

![image-20220921174106235](images/image-20220921174106235.png)



There's a more elegant way though you can use `glob(pattern)` instead

```
from pathlib import Path 

root_dir = Path('files')

file_paths = root_dir.glob("**/*")

for path in file_paths:
    print(path)

```

includes everything including first level files

![image-20220921174412983](images/image-20220921174412983.png)



you can use `path.is_file():` to check if it is a file and only then print it or act on it:

```
from pathlib import Path 
root_dir = Path('files')
file_paths = root_dir.glob("**/*")

for path in file_paths:
    if path.is_file():          # checks if it's a file returns true 
        print(path)
```

seperate the parts of the path/filename out using `path.parts`:

```
from pathlib import Path 
root_dir = Path('files')
file_paths = root_dir.glob("**/*")

for path in file_paths:
    if path.is_file():          # checks if it's a file returns true 
        # print(path)
        # get the name of the folder the file is in:
        parent_folder = path.parts
        print(parent_folder)
        #new_filename = path.
```

![image-20220921174833618](images/image-20220921174833618.png)

but it's split into different items in a tuple

since it's a tuple use [-2], counting from right to left it's -1, -2, -3 etc

```
parent_folder = path.parts[-2]
```

```
from pathlib import Path 
root_dir = Path('files')
file_paths = root_dir.glob("**/*")

for path in file_paths:
    if path.is_file():          # checks if it's a file returns true 
        # print(path)
        # get the name of the folder the file is in:
        parent_folder = path.parts[-2]
        print(parent_folder)

```

![image-20220921175129509](images/image-20220921175129509.png)

construct the new filename with

```
        new_filename = parent_folder + '-' + path.name
```

and you use path.with_name and path.rename:

```
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
        path.rename(new_filepath)                       # apply rename to the path object
```

![image-20220921175503089](images/image-20220921175503089.png)

and the files get renamed:

![image-20220921175517941](images/image-20220921175517941.png)

## 32 - Renaming Files based on a sub-sub folder