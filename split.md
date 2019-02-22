'''python

import numpy as np


def fun(a, b, c):
    return b**2-4*a*c


def check(x):

    if x>0:
        val = (b*-1+np.sqrt(x))/2*a
        val2 = (b * -1 - np.sqrt(x)) / 2 * a
        print(val,val2)

    elif x==0:
        val = b*-1/2*a
        print(val)
    else:
        print('It is not possible !')



abc = input("abc: ")

a, b, c = abc.split(',')
a, b, c = int(a),int(b),int(c)
temp = fun(a,b,c)
check(temp)

'''
