#include "Python.h"
#include <stdlib.h>
#include <string.h>
#include "test.h"
 /**
 
  **包裹文件
 
 **/
 
 //为fac函数设置包裹函数(函数名、参数都有一定的规则，要注意)
static PyObject *test_fac(PyObject *self,PyObject *args)
 {
 
     int num ;
     //将python的数据类型int args通过i的方式转换成能被c识别的类型int num
     //i:表示将python的整型转成c的整型 ，其它类型可百度
     if (!PyArg_ParseTuple(args,"i",&num)) 
         return NULL;
 
 
     //调用c的对应函数并得到返回值，
     //然后将返回值c的数据类型int通过i的方式转换成能被python识别的类型int
     //最后强转成PyObject类型
     return (PyObject *)Py_BuildValue("i",fac(num));
 
 }
 
 
 //为reverse函数设置包裹函数（由于python中有reverse函数，不能使用）
 static PyObject *test_doppel(PyObject *self,PyObject *args)
 {
     char *src;
    char *mstr;
    PyObject *retval;
 
     //s:python中str ----->C中char * 
     if (!PyArg_ParseTuple(args,"s",&src))
         return NULL;

     //申请存储空间
     mstr = malloc(strlen(src) +1);
     //拷贝src到mstr
     strcpy(mstr,src);
     //调用reverse方法，逆序字符串
     reverse(mstr);
     //这里把原字符串和转换后的字符串返回
     retval = (PyObject *) Py_BuildValue("ss",src,mstr);
    //释放空间
     free(mstr);
 
     return retval;
 }
 
 
 //为test函数设置包裹函数
 static PyObject *test_test(PyObject *self,PyObject *args)
 {
     //直接调用c函数
     test();
 
    return (PyObject *)Py_BuildValue("");
 }
 

 //添加模块数组(注意是PyMethodDef,不要错写成PyMethondDef)
 //定义对应的方法名，后面Python调用的时候就用这里面的方法名调用
 static PyMethodDef testMethods[] = {
     {"fac",test_fac,METH_VARARGS},
     {"doppel",test_doppel,METH_VARARGS},
     {"test",test_test,METH_VARARGS},
     {NULL,NULL},
 };
 
 
 //模块初始化函数
 void init_test(void)
 {
    Py_InitModule("test",testMethods);
}