# -*-coding:Latin-1 -*

# Here is the script for PLHA2 for Laurent
# Here are handled files PLHA#####.* which must be
# moved to their directory PLHA#####
# Files PLHA#####.* and directories PLHA##### take
# place at the same level # (i.e. superdirectory)
# before being handled.

import os
import shutil

os.chdir("/home/ladmin/Téléchargements/PLHA")
# Path to the superdirectory where files and
# directories to handle take place.

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
j, k = 0, len(filelist)
for element in filelist:
    box = element[0:9] + '/' + element
    try:
        shutil.move(element, box)
    except:
        j += 1
        continue
# (2) End of (2)

# Final report :
print('Final report (3 lines follow) :')
print(k, ' file(s) examined.')
print(k-j, ' file(s) relocated.')
print(j, ' file(s) remained in place.')


#input("Press 'Entry key' to close this program...")
# For linux use, cancel the eventual # at the beginning of the upper line
# and put a # (if not yet) at the beginning of the following one.

os.system("pause")

# For Windows use, cancel the eventual # at the beginning of the just upper
# line and put a # (if not yet) at the beginning of the upper line beginning
# with : input("Press 'Entry key' to ...")
