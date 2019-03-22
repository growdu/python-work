import math

def is_not_prime(n):
    temp=int(math.sqrt(n))
    for num in range(2,temp+1):
        t=n%num
        if t==0:
            return True


def getPrime(n):
    for i in range(1,n):
        if i==1 or i==2 or i==3:
            print(str(i)+',')
        elif not is_not_prime(i):
            print (str(i)+',')

test_num=100
#is_not_prime(27)
getPrime(test_num)


