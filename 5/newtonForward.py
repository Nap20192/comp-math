
def fact(n):
    f = 1;
    for i in range(2, n + 1):
        f *= i;
    return f;


def forward_diff(x, y,n,h, x0):
    p = (x0 - x[0]) / h
    for i in range(1,len(y)):
        y[i] = y[i] - y[i - 1];
    return y[0]

def newton_forward(x, y, n, x0, h):
    sum = 0;
    u = (x0 - x[0]) / h;
    for i in range(1, n):
        sum = sum + (forward_diff(x, y, i, h, x[0]) * u) / fact(i);
        u *= (u - x[i-1]);
    return sum;

