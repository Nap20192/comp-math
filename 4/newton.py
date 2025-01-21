from scipy.misc import derivative

def newton_all_roots(a, b, e, f, m):
    roots = []
    x = a
    while x <= b:
        root, i, success = newton(x, e, f, m)
        if success and not any(abs(root - r) < 0.3 for r in roots):
            roots.append(root)
        x += 1  
    
    return roots

def newton(a, e, f, m):
    i = 0
    x = a  
    while i < m:
        d = derivative(f, x) 
        if d == 0:  
            return x, i, False
        x1 = x - f(x) / d  
        if abs(x1 - x) < e: 
            return x1, i, True
        x = x1  
        i += 1
    return x, i, False  

def f(x):
    return x**2-4
