# recover-password-lost-in-zip-file

This script recover the password to decompress a zip file by brute force

### Installation
- git clone https://github.com/KevinLiebergen/recover-password-lost-in-zip-file.git


### Running
This default script uses a Spanish dictionary that brings linux, if you want another one you can specify in the second argument (optional).

Linux brings by default dictionaries hosted in /usr/share/dict/

-  cd recover-password-list-in-zip-file

-  ./RecoverPasswordInZip.py <__zip-file-path__> <__dictionary(optional)__>

### Examples
  
-  ./RecoverPasswordInZip.py ~/test.zip /usr/share/dict/american-english
-  ./RecoverPasswordInZip.py ~/test.zip
