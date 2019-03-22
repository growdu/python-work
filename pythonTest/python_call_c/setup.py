#incoding:utf-8
from distutils.core import setup,Extension
#模块名
MOD = 'test'
#资源（要编译和链接的代码文件）
source = ['test.c','wrapper.c'] 
#调用setup函数,编译和链接
setup(name=MOD,ext_modules=[Extension(MOD,sources=source)])