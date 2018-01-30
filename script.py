# Here is the script

import os

chdir("/home/ladmin/Téléchargements/PLHA")    # Path to the superdirectory where files and directories to manage take place.

filelist = []
filelist = os.lsisfile?????????,()

for k in filelist:
    move ??????????????????

while i:
    if i > 9999:
        suf = str(i)
    elif i > 999 and i < 10000:
        suf = '0' + str(i)
    elif i > 99 and i < 1000:
        suf = '00' + str(i)
    elif i > 9 and i < 100:
        suf = '000' + str(i)
    elif i < 10:
        suf = '0000' + str(i)
    path = way + suf
    os.mkdir(path)
    i -=1

print(j, ' directories created')
