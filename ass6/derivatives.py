import sys
from os.path import dirname, abspath
sys.path.append(abspath(dirname(__file__) + "../../"))
from ass5 import *
def find_index_of_closest_x(x,y,x0):
    return min(range(len(x)), key=lambda i: abs(x[i]-x0))

def numerical_derivative(x,y,n,x0,degree):
    i = find_index_of_closest_x(x,y,x0)
    h =x[1]-x[0]
    if degree == 1:
        return (newton_forward(x, y, n, x0 + h) - newton_forward(x, y, n, x0 -h)) / (2*h)
    elif degree == 2:
        return (newton_forward(x, y, n, x0 + h) - 2 * newton_forward(x, y, n, x0) + newton_forward(x, y, n, x0 - h)) / (h ** 2)
    elif degree == 3:
        return (newton_forward(x, y, n, x0 + h) - 3 * newton_forward(x, y, n, x0) + 3 * newton_forward(x, y, n, x0 - h) - newton_forward(x, y, n, x0 - 2 * h)) / (h ** 3)