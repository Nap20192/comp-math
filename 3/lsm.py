import numpy as np
from gauss import gauss
def polynomial(x, coefficients, start, gap):
    summ = 0
    i = 0
    p = start
    while i < len(coefficients):
        if p not in gap:
            summ += coefficients[i] * x**p
            i += 1
        p += 1
    return summ


def least_square_method(x, y, degree, start=0, degrees = []):
    X = []
    n = len(x)

    for xi in x:
        t = []
        for i in range(start,degree+1):
            if i not in degrees:
                print("i",i)
                t.append(xi**i)
        X.append(t)
    print("X")
    
    r =len(X[0])

    for i in range(n):
        print(X[i])

    print(len(X),len(degrees),n)
    Xt = []

    for i in range(len(X[0])):
        t = []
        for j in range(n):
            t.append(X[j][i])
        Xt.append(t)
            
    print("Xt")

    for i in range(len(Xt)):
        print(Xt[i])
    print("XtX")

    XtX = []

    for i in range(start, r+start ):
        t = []
        for j in range(start, r +start ):
            summ = 0
            for k in range(n):
                summ += Xt[i][k] * X[k][j]
            t.append(summ)
        XtX.append(t)

    for i in range(len(XtX)):
        print(XtX[i])
    XtY = []
    for i in range(start, r+start):
        summ = 0
        for j in range(n):
            summ += Xt[i][j] * y[j]
        XtY.append(summ)

    for i in range(len(XtY)):
        print(XtY[i])
    
    coefficients = gauss(XtX, XtY)
    c = []
    for i in range(len(coefficients)):
        c.insert(0,coefficients[i])

    y_pred = [polynomial(xi, coefficients , start, degrees) for xi in x]
    residuals = [y[i] - y_pred[i] for i in range(n)]
    ssr = sum(residuals[i]**2 for i in range(n))
    
    if start<0:
        print("c",c)
        return c

    else:
        print("coefficients",coefficients)
        return coefficients