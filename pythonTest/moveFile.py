import os,shutil
import sys

def travel(filepath,targetPath):
    files = os.listdir(filepath)
    for fi in files:
        fi_d = os.path.join(filepath,fi)            
        if os.path.isdir(fi_d):
            travel(fi_d,targetPath)                 
        else:
            shutil.move(fi_d,os.path.join(targetPath,fi))

'''
处理命令行参数
'''
def __main__():
    if len(sys.argv)==3 and sys.argv[1]=='-i':
        sourcePath=sys.argv[2]
        targetPath=os.path.join(sys.argv[2],'test')
    elif len(sys.argv)==5 and sys.argv[1]=='-i' and sys.argv[3]=='-o':
        sourcePath=sys.argv[2]
        targetPath=sys.argv[4]
    elif len(sys.argv)<0:
        print("no argument.")
    else:
        ss=[]
        ss=sys.argv
        print(ss[0])
        for s in ss:
            print(s)
        return 0
    '''
    sourcePath='C:\\Users\\duanys\\Desktop\\20190125\\基金公告\\2019\\1\\25'
    targetPath=os.path.join(sourcePath,'test')
    '''
    if not os.path.exists(targetPath):
        os.makedirs(targetPath)
    for path in os.listdir(sourcePath):
        if path=='test':
            continue
        child=os.path.join(sourcePath,path)
        if os.path.isdir(child):
            travel(child,targetPath)
        else:
            shutil.move(child,os.path.join(targetPath,path))


