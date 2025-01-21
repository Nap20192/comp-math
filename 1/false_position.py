def false_postion(a,b,e,f,m):
    if(f(a)*f(b) >= 0):
        return None
    i=0     
    while i < m:
        x = (a*f(b) - b*f(a)) / (f(b) - f(a))
        if abs(f(x)) < e:
            return x ,i, True
        if f(a) * f(x) < 0: 
            b = x
        else:  
            a = x
        i += 1
    return x,i, False