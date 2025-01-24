from lsm import least_square_method
import math
import matplotlib.pyplot as plt

if __name__ == "__main__":
    x = [0, 1, 2, 3]
    y = [1.05, 2.10, 3.85, 8.30]
    y = [math.log(yi) for yi in y]
    gaps = [[0]]
    degrees = [1]
    start = 0
    r = []
    count = 1
    plt.scatter(x, y, color='black', label='Data points')

    for degree in degrees:
        for gap in gaps:
            coefficients, ssr = least_square_method(x, y, degree,start,gap,1)
            print()
            print(f'{count} Coefficients for degree {degree}: {coefficients}/ Gap: {gap} / SSR: {ssr} ')
            count += 1
            r.append(ssr)
            x_f = []
            current = min(x)
            step=0.3
            while current < max(x):
                x_f.append(current)
                current += step
            y_f = []
            current = min(x)
            b, ln_A = coefficients[0], coefficients[1]
            A = math.exp(ln_A)
            x_f = []
            step=0.3
            while current < max(x):
                x_f.append(current)
                current += step            
            y_f= [A * math.exp(b * xi) for xi in x_f]
            plt.plot(x_f, y_f, label=f'Degree {degree} / Gap {gap}')
    plt.grid()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()