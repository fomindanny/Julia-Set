import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

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


def julia_set_animation(
        threshold: int, density: int, constant: complex,
        color_map="RdPu", file_name="julia_set.gif",
        frames=120, interval=40):
    """Julia Set animation.
    Saves an animation to the animation folder.
    """
    real_axis = np.linspace(-2, 2, density)
    imaginary_axis = np.linspace(-2, 2, density)
    circle_axis = np.linspace(0, 2*np.pi, frames)

    fig = plt.figure()
    fig.set_size_inches(10, 10)
    axes = plt.Axes(fig, [0, 0, 1, 1])
    axes.set_axis_off()
    fig.add_axes(axes)

    def animate(i):
        matrix = np.empty((density, density))
        current_constant = complex(
            constant * np.cos(circle_axis[i]),
            constant * np.sin(circle_axis[i]))

        for row in range(density):
            for col in range(density):
                point_of_interest = complex(
                    real_axis[row],
                    imaginary_axis[col])
                matrix[row, col] = iterations_until_diverge(
                    point_of_interest,
                    current_constant, threshold)

        interpolation_type = "bicubic"
        image = axes.imshow(
            matrix.T, interpolation=interpolation_type,
            cmap=color_map)

        return [image]

    figure_animation = animation.FuncAnimation(
        fig, animate, frames=frames,
        interval=interval, blit=True)
    file_path = "animations/" + file_name
    file_writer = "imagemagick"
    figure_animation.save(file_path, writer=file_writer)
