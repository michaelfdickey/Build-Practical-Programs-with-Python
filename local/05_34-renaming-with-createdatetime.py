from pathlib import Path
from datetime import datetime

path = Path('files/December/a.txt')

# if you have a path object you can get data about that object with the path.stat() method

stats = path.stat()

print(stats)
"""
result of print(stats):
$ python main.py
os.stat_result(st_mode=33188, st_ino=264, st_dev=19923088, st_nlink=1, st_uid=1000, st_gid=1000, st_size=2, st_atime=1635878203, st_mtime=1635878203, st_ctime=1665005893)

st_mode some info about permissions
st_uid user identifier
st_gid user group identifier
st_size = file size

what we want is time:

st_atime - last access time stamp, seconds from jan1 1970
st_mtime - when file was last modified
st_ctime - when the file was created
"""

# to get that ctime:
seconds_when_created = stats.st_ctime
print(seconds_when_created)
"""
output:
$ python main.py
os.stat_result(st_mode=33188, st_ino=264, st_dev=19923088, st_nlink=1, st_uid=1000, st_gid=1000, st_size=2, st_atime=1635878203, st_mtime=1635878203, st_ctime=1665005893)
1665005893.6959639
"""

# to convert epoch time to normal time in python:
date_created = datetime.fromtimestamp(seconds_when_created)
print(date_created)
"""
$ python main.py
os.stat_result(st_mode=33188, st_ino=264, st_dev=19923088, st_nlink=1, st_uid=1000, st_gid=1000, st_size=2, st_atime=1635878203, st_mtime=1635878203, st_ctime=1665005893)
1665005893.6959639
2022-10-05 21:38:13.695964
"""

# date_created is not a string though, need to convert it
date_created_str = date_created.strftime(
    "%Y-%m-%d_%H:%M:%S")  # creates a string from time

print(date_created_str)
print(type(date_created_str))
"""
1665005893.6959639
2022-10-05 21:38:13.695964
2022-10-05_21:38:13
<class 'str'>
"""
