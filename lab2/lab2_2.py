﻿import os
import hashlib

import codecs

tree = os.walk(os.getcwd())
RtFsHash = []
hashes = []
for r,d,fs in tree:
    for f in fs:
        try:
            root = r+'\\'
            with codecs.open(root+f, 'r', 'utf-8-sig') as file:
                fileread = file.read()
                md5Hash = hashlib.md5(fileread.encode())
                RtFsHash.append((r,f,md5Hash.hexdigest()))
                hashes.append(md5Hash.hexdigest())
        except IOError as err:
            print(err)
        except UnicodeDecodeError:
            print('PROBLEM WITH THE {}'.format(f))

for r,f,h in RtFsHash:    
    print('Root: ',r,'\nFilename: ',f,'\nHash MD5: ',h,'\n')

print('Одинаковые контрольные суммы MD5:')
ravni = []

for i,h in enumerate(hashes):
    if hashes.count(h) > 1:
        print(RtFsHash[i][1], RtFsHash[i][2])

        
            

    






