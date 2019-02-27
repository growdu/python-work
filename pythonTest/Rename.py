import os
import sys


path=sys.argv[1]
for file in os.listdir(path):
    if file[-3: ]!='xml':
        continue
    name=file.replace(' ','')
    newName=name[: -3]+'.html'
    os.rename(os.path.join(path,file),os.path.join(path,newName))