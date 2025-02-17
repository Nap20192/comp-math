from newtonForward import newton_forward,diffs_table,missing
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

def f(x):
    result = 1
    for i in range(1, 20, 2): 
        result *= (2 * x + i)
    return result

if __name__ == '__main__':
    x = [3,4,5,6]
    y = [49.2,54.1,60,0]
    x0 = [6,7,8]
    n = len(x)
    coef = [1,-2,1,1]
    xx = [0,1,2,3,4,5]
    yy = []
    for i in xx:
        yy.append(polynomial(i,coef,0,[]))
    print(missing(y))


