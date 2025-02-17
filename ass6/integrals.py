def trapezoidal(a,b,f,n):
    h = (b-a)/n
    x = []
    y= []
    for i in range(n):
        x.append(a+i*h)
        y.append(f(x[i]))
    result = 0
    for i in range(n-1):
        result += y[i] + y[i+1]
    return result*h/2

def simpsons13(a,b,f,n):
    if n % 2 != 0:
        n += 1
        print("n is not even, increasing n to ", n)
    h = (b-a)/n
    x = []
    y = []
    for i in range(n):
        x.append(a+i*h)
        y.append(f(x[i]))
    result = 0
    for i in range(0,n-2,2):
        result += y[i] + 4*y[i+1] + y[i+2]
    return result*h/3

def simpsons38(a,b,f,n):
    if n % 3 != 0:
        n += 1
        print("n is not divisible by 3, increasing n to ",n)
    if n % 3 != 0:
        n += 1
        print("n is still not divisible by 3, increasing n to ",n)
        
    h = (b-a)/n
    x = []
    y = []
    for i in range(n):
        x.append(a+i*h)
        y.append(f(x[i]))
    result = 0
    for i in range(0,n-3,3):
        result += y[i] + 3*y[i+1] + 3*y[i+2] + y[i+3]
    return result*h*3/8
