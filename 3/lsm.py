from gauss import gauss

def polynomial(x, coefficients, start, gap):
    s = 0
    i = 0
    p = start
    while i < len(coefficients):
        if p not in gap:
            s += coefficients[i] * x**p
            i += 1
        p += 1
    return s


def least_square_method(x, y, degree, start=0, degrees = [],i_var = 0):
    X = []
    n = len(x)

    for xi in x:
        t = []
        for i in range(start,degree+1):
            if i not in degrees:
                t.append(xi**i)
        X.append(t + [1] * i_var)


    r =len(X[0])


    Xt = []

    for i in range(len(X[0])):
        t = []
        for j in range(n):
            t.append(X[j][i])
        Xt.append(t)
            

 

    XtX = []

    for i in range(start, r+start ):
        t = []
        for j in range(start, r +start ):
            s = 0
            for k in range(n):
                s += Xt[i][k] * X[k][j]
            t.append(s)
        XtX.append(t)
    """
    for i in X:
        print (i)
    print()
    for i in XtX:
        print(i)
    for i in XtY:
        print(i)
    """

    XtY = []
    for i in range(start, r+start):
        s = 0
        for j in range(n):
            s += Xt[i][j] * y[j]
        XtY.append(s)
    

    coefficients = gauss(XtX, XtY)
    c = []
    for i in range(len(coefficients)):
        c.insert(0,coefficients[i])


    
    if start<0:
        print("c",c)
        y_pred = [polynomial(xi, c , start, degrees) for xi in x]
        residuals = [y[i] - y_pred[i] for i in range(n)]
        ssr = sum(residuals[i]**2 for i in range(n))
        return c,ssr

    else:
        print("coefficients",coefficients)
        y_pred = [polynomial(xi, coefficients , start, degrees) for xi in x]
        residuals = [y[i] - y_pred[i] for i in range(n)]
        ssr = sum(residuals[i]**2 for i in range(n))
        return coefficients,ssr