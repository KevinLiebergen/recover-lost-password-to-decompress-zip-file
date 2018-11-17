#!/usr/bin/env python3

import zipfile
import zlib
import sys


found = False
path_file = sys.argv[1]

if len(sys.argv)==2: 
    dictionary = "/usr/share/dict/spanish"
else:
    dictionary = sys.argv[2]

with zipfile.ZipFile(path_file, "r") as archive:
    first = archive.infolist()[0]   #Infolist to extract information from each member, [0] take the first element
    print("Reading ", first.filename)
    with open(dictionary) as corpus:
        for line in corpus:
            word = line.encode("utf8").strip()
            try:
                with archive.open(first, 'r', pwd=word) as member:
                    text = member.read()
                print("Password",word)
                print(text)
                found=True
                break
            except (RuntimeError, zlib.error, zipfile.BadZipfile):
                pass
                    
if found is False: print("Password not found")
