import sys
import hashlib
import os.path
#filename = sys.argv[1]
filename="c:\\1.txt"
if os.path.isfile(filename):
    fp=open(filename,'rb')
    contents=fp.read()
    fp.close()
    print(hashlib.md5(contents).hexdigest())
else:
    print(filename)