from lsm import least_square_method
import matplotlib.pyplot as plt

if __name__ == "__main__":
    x = [6, 7, 7, 8, 8, 8, 9, 9, 10]
    y = [5, 5, 4, 5, 4, 3, 4, 3, 3]

    degrees = [1]
    plt.scatter(x, y, color='black', label='Data points')

    for degree in degrees:
        coefficients, ssr, partial_derivatives = least_square_method(x, y, degree)
        x_fit = list(range(min(x), max(x) + 1))
        y_fit = [sum(coefficients[j] * (xi ** j) for j in range(degree + 1)) for xi in x_fit]
        plt.plot(x_fit, y_fit, label=f'Degree {degree}')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()