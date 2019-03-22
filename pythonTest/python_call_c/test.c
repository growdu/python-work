#include<stdio.h>
#include<stdlib.h>
#include<string.h>
 
 
//求阶乘
int fac(int n) {
    if(n < 2)
        return 1;
 
    return n*fac(n-1);
}


 //字符串逆序
 char *reverse(char *s) {
     //比如输入abcdefg,则返回gfedcba
     char t,*p = s ,*q = (s+strlen(s)-1);
 
     while(s && (p<q)) {
         t = *p;
         *p++ = *q;
         *q-- = t;
     }
 
     return s;
 }

int test(void)  //测试main方法，改成普通的test方法
//  int main(void)
{
     char s[1024];
 
     printf("5! = %d\n",fac(5));  //5的阶乘
 
     printf("10! = %d\n",fac(10)); // 10的阶乘
 
 
    strcpy(s,"hello world");
     printf("reversing 'hello world',we get '%s'\n",reverse(s));
 
     return 0;
}