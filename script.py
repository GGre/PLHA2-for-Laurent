# Here is the script for PLHA2 for Laurent

import os
import shutil

os.chdir("/home/ladmin/Téléchargements/PLHA") # Path to the superdirectory where
                                              # files and directories to manage
                                              # take place.

# (1) Making the list of files in the superdirectory (1)
filelist = []
for (dirpath, dirnames, filenames) in os.walk(os.getcwd()):
    filelist.append(filenames)
    break
try:
    test = filelist[1]
    print('An error occured : Please verify the path')
except:
    filelist = filelist[0]
# (1) End of (1)


# (2) Moving the files (2)
for element in filelist:
    box = element[0:9] + '/' + element
    shutil.move(element, box)
# (2) End of (2)
