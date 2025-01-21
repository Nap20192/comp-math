from scipy.misc import derivative

def  newton(a,b,e,f,m):
    i=0
    d = derivative(f,a)
    while abs(d)>=1:
        a+=0.001
        d=derivative(f,a)
    x = f(a)
    while i < m:
        x1 = x - f(x)/derivative(f,x)
        if abs(x1-x) < e:
            return x1 ,i, True
        x=x1
        i+=1
    return x1,i, False