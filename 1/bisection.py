import math
import numpy as np
import matplotlib.pyplot as plt
from false_position import false_postion
from iteration_method import iteration_method,g
from newton import newton
def f(x):
    return x-math.cos(x)

def draw(m1,a,b,e,f,m,c,l):
    q=False
    x = []
    y = []
    while not q:
        m+=1
        t,i,q = m1(a,b,e,f,m)
        if t is not None:
            x.append(i)
            y.append(t)
    print(y[-1],'=>',f(y[-1]))
    plt.plot(x, y,color=c,linestyle = l)




def bisection(a,b,e,f,m):
    if(f(a)*f(b) >= 0):
        return None
    i=0
    while (abs(a-b)>e) and i<=5:
        x = (a+b)/2
        if(f(x)==0):
            return x ,i, True
        elif(f(x)*f(a)<0):
            b=x
        else:
            a=x
        i+=1
    print(x)
    if(abs(a-b)<e):
        return x,i, True
    else:
        return x,i, False


if __name__ == "__main__":
    a=-5
    b=10
    if f(a)*f(b)<0:
        print("correct")
    else:
        print('not correct:')
        print(f(a))
        print(f(b))
        exit()

    x = []
    y = []
    m=0
    e=10**(-5)

    draw(bisection,a,b,e,f,m,'red','--')
    draw(false_postion,a,b,e,f,m,'blue','dotted')
    draw(iteration_method,a,b,e,g,m,'green','-.')
    draw(newton,a,b,e,f,m,'purple',':')

    ##q1 = [i * 0.1 for i in range(-100, 100)] 
    ##w1 = [f(x) for x in q1]
    ##plt.plot(q1, w1,color='black')
    plt.grid()
    plt.show() 
