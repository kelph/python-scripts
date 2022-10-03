#! /bin/python

from os import listdir
from sys import argv
from pathlib import Path

# files to check if dir_2 contains
dir_1 = listdir(Path(argv[1]))

# files to check against
dir_2 = listdir(Path(argv[2]))

# results arr
results = []

for _, j in enumerate(dir_1):
    if j in dir_2:
        results.append((j, True))
    else:
        results.append((j, False))

# print(results)
for i, j in enumerate(results):
    print('{:<60s}{:>10s}'.format(j[0], str(j[1])))


 # (| select-string -Pattern False) powershell grep ://