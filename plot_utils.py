import numpy as np
import matplotlib.pyplot as plt

def plot_surface(function, x_range = (-6,6), y_range=(-6,6), spacing=30):
    X, Y = create_mesh(x_range, y_range, spacing)
    Z = function(X, Y)
    ax = plt.axes(projection='3d')
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                    cmap='plasma', edgecolor='none')
    ax.set_title('surface')
    return ax

def create_mesh(x_range, y_range, spacing):
    x = np.linspace(x_range[0], x_range[1], spacing)
    y = np.linspace(y_range[0], y_range[1], spacing)
    return np.meshgrid(x, y)


def sample_function_1(x,y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))

def sample_function_2(x,y):
    return (x ** 2 -4)**2 + y ** 2

if __name__ == '__main__':
    ax = plot_surface(sample_function_2, (-3,3), (-4,4), 30)
    plt.show()
