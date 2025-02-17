import math
from newtonForward import *
from integrals import trapezoidal, simpsons13,simpsons38
from derivatives import numerical_derivative


def Task1():
    x = [0, 5, 10, 15]
    y = [3, 14, 69, 228]
    x.append(20)
    y.append(newton_forward(x, y, len(y), x[-1]))
    print(x, y)
    a = []
    for i in range(len(x)):
        a.append(numerical_derivative(x, y, len(y), x[i], 1))
    sum = 0 
    print("initial acceleration ",a[0])
    
def Task2():
    x = [3, 5, 11, 27, 34]
    y= [-13, 23, 899, 17315, 35606]
    print(numerical_derivative(x,y,len(y),12,1))
def Task3():
    x = [1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
    y =[3.375, 7.000, 13.625, 24.000, 38.875, 59.000]
    print(numerical_derivative(x,y,len(y),1.5,1))
    print(numerical_derivative(x,y,len(y),1.5,2))
    print(numerical_derivative(x,y,len(y),1.5,3))

def Task4():
    x = [1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
    y =[0, 0.128, 0.544, 1.296, 2.432, 4.00]
    print(numerical_derivative(x,y,len(y),1.1,1))

def Task5():
    x = [1.00, 1.05, 1.10, 1.15, 1.20, 1.25, 1.30]
    y = [1.000, 1.025, 1.049, 1.072, 1.095, 1.118, 1.140]
    print(numerical_derivative(x,y,len(y),1.05,1))
    print(numerical_derivative(x,y,len(y),1.15,2))

def Task6():
    def f(x):
        return x**3
    print(trapezoidal(0, 1, f, 1000))
def Task7():
    def f1(x):
        return math.sin(x)
    def f2(x):
        return math.cos(x)**0.5
    print(simpsons13(0,math.pi, f1, 1000))
    print(simpsons13(0,math.pi/2, f2, 1000))
def Task8():
    def f1(x):
        return 1/(1+x**3)
    def f2(x):
        return math.sin(x)
    print(simpsons38(0,9, f1, 1000))
    print(simpsons38(0,math.pi/2, f2, 1000))
def Task9():
    def f(x):
        return 1/(1+x)
    print(trapezoidal(0, 1, f, 300))
    print(simpsons13(0, 1, f, 300))
    print(simpsons38(0, 1, f, 300))

if __name__ == "__main__":
    Task9()