
import re

from os import listdir, sep
from os.path import abspath, commonpath
import os.path
from sys import argv, path
from pathlib import Path


# is file:
# path.is_file()
# is dir
# path.is_dir()

# recur_grep.py [pattern] dir

dir = Path(abspath(argv[2]))

ptrn = argv[1]
paths = []
results = []


def check_ln(pattern, txt, spacer='|'):  
    x = re.search(pattern, txt)
    if x:
        # returns tuple
        parts = [txt[0:x.span()[0]]]
        parts += [txt[x.span()[0]:x.span()[1]]]
        parts += [txt[x.span()[1]:len(txt)]]
        return f'{parts[0]} {spacer}{parts[1]}{spacer} {parts[2]}'
    return None

def recur_dir(_obj: Path):
    if _obj.is_dir():
        dirs = listdir(_obj)
        for i in dirs:
            recur_dir(Path(_obj, i))
    else:
        # do file things
        with open(_obj, 'r') as f:
            try:
                for ln, line in enumerate(f):
                    x = check_ln(ptrn, line)
                    if x:
                        paths.append(abspath(_obj))
                        results.append((ln, x))
            except UnicodeDecodeError as e:
                pass
recur_dir(dir)
common_path_parts = str(commonpath(paths)).split(sep)

final_arr = []
for path in paths:
    s_path = str(path).split(sep)
    a = sep.join(s_path[len(common_path_parts)-1:len(common_path_parts)])
    final_arr.append(a)
 
print(len(final_arr))
print(len(results))

for idx, path in enumerate(final_arr):
    print('{:<75s} {:^2} {:^2}'.format(path, results[idx][0], results[idx][1]))