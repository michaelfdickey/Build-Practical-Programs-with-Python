from pathlib import Path

# reading files:
#p1 = Path('files/abc.txt')
#print(type(p1))
#print(p1)

# you can also write files if the file doesn't exist
p1 = Path('new_file2.txt')

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


