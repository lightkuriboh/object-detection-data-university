import os
from os import walk

my_path = 'racing motor bike'

f = []
for (dirpath, dirnames, filenames) in walk(my_path):
    f.extend(filenames)

for to_rename in f:
    if len(to_rename) > 8 and to_rename[-8:] == '.xml.txt':
        print(to_rename)
        new_name = to_rename[:-8] + to_rename[-4:]
        command = 'mv \"{}/{}\" \"{}/{}\"'.format(my_path, to_rename, my_path, new_name)
        print(command)
        os.system(command)

