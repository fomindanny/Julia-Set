import numpy as np
import matplotlib.pyplot as plt


def iterations_until_diverge(
        point_of_interest: complex, constant: complex,
        threshold: int) -> int:
    """Returns an amount of iterations until function diverges.
    Function is z(n + 1) = z ^ 2 + c.
    Function diverges when |z| > 4.
    """
    z = point_of_interest
    c = constant

    for iteration in range(threshold):
        z = z**2 + c
        if abs(z) > 4:
            break

    return iteration


def julia_set(
        threshold: int, density: int, constant: complex,
        color_map="RdPu", file_name="julia_set.png"):
    """Julia Set realisation.
    Saves an image to the images folder.
    """
    real_axis = np.linspace(-1.5, 1.5, density)
    imaginary_axis = np.linspace(-1.5, 1.5, density)
    matrix = np.empty((density, density))

    for row in range(density):
        for col in range(density):
            point_of_interest = complex(real_axis[row], imaginary_axis[col])
            matrix[row, col] = iterations_until_diverge(
                point_of_interest,
                constant, threshold)

    file_path = "images/" + file_name
    plt.imsave(file_path, matrix.T, cmap=color_map)
