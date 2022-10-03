#! /bin/python
## Modified 'compare_dirs' code

from os import listdir, mkdir
from sys import argv
from pathlib import Path
from shutil import copy

# files to check if dir_2 contains
dir_1 = Path(argv[1])

# files to check against
dir_2 = Path(argv[2])

# outputfile lol
output = Path(argv[3])

# results arr
results = []
if not output.is_dir():
    mkdir(output)

# gen diffs
for _, j in enumerate(listdir(dir_1)):
    if j in listdir(dir_2):
        results.append((j, True))
    else:
        results.append((j, False))

# move files
for _, tup in enumerate(results):
    if not tup[1]:
        print(tup[0])
        copy(Path(dir_1, tup[0]), output)


 # (| select-string -Pattern False) powershell grep ://