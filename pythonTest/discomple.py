# encoding=utf8
import os
import uncompyle6


def main():
    for root, dirs, files in os.walk("."):
        for filename in files:
            if filename.endswith('pyc'):
                source = os.path.join(root, filename)
                print(os.path.join(root, filename))
                os.system("uncompyle6 -o "+source.replace('.pyc', '.py')+" "+source)
                os.remove(source)



if __name__ == '__main__':
    main()