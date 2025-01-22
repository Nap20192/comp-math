from gauss import gauss

def polynomial(x,k):
    y=0
    for i in range(len(k)):
        y += k[i]*x**i
    return y

def least_square_method(x, y, degree):
    n = len(x)
    
    X = [[xi**j for j in range(degree + 1)] for xi in x]
    for i in range(n):
        print(X[i])
    
    Xt = [[X[j][i] for j in range(n)] for i in range(degree + 1)]
    print("Xt")
    for i in range(degree + 1):
        print(Xt[i])
    
    XtX = [[sum(Xt[i][k] * X[k][j] for k in range(n)) for j in range(degree + 1)] for i in range(degree + 1)]
    for i in range(degree + 1):
        print(XtX[i])
    print("XtY")
    XtY = [sum(Xt[i][j] * y[j] for j in range(n)) for i in range(degree + 1)]
    for i in range(degree + 1):
        print(XtY[i])
    coefficients = gauss(XtX, XtY)
    
    y_pred = [polynomial(xi, coefficients) for xi in x]
    residuals = [y[i] - y_pred[i] for i in range(n)]
    ssr = sum(residuals[i]**2 for i in range(n))
    
    partial_derivatives = []
    for i in range(degree + 1):
        dS_dBeta = -2 * sum(X[j][i] * residuals[j] for j in range(n))
        partial_derivatives.insert(0,dS_dBeta)
    print(coefficients)
    return coefficients, ssr, partial_derivatives

def gaussian_elimination(A, b):
    n = len(b)
    for i in range(n):
        factor = A[i][i]
        for j in range(i, n):
            A[i][j] /= factor
        b[i] /= factor
        
        for k in range(n):
            if k != i:
                factor = A[k][i]
                for j in range(i, n):
                    A[k][j] -= factor * A[i][j]
                b[k] -= factor * b[i]
    
    return b



