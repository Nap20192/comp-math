from scipy.misc import derivative
import math
def g(x):
    return  math.cbrt(2*x-5)

def iteration_method(a,b,e,g,m):
    i=0
    d = derivative(g,a)
    while abs(d)>=1:
        a+=0.001
        d=derivative(g,a)
    x = a
    while i < m:
        x1 = g(x)
        if abs(x1-x) < e:
            return x1 ,i, True
        x=x1
        i+=1
    return x1,i, False