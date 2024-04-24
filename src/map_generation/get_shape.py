import numpy as np


def get_shape(data_resolution: int, shape_func: function(float, float), data_range=(-1, 1)):
    '''
        Returns a 2d array of a shape defined by the shape func and the datarange.

            Parameters:
                data_resolution (int): A decimal integer defines the number of datapoints on one side of the square.
                shape_func (function(x, y)): A function that takes in x and y and outputs a floating point value.
                datarange (tuple (start, end)): A tuple that outlines the start and end of the datarange.

            Returns:
                2d array (Array): A 2d array of floating point numbers.

    '''
    line_x = np.linspace(data_range[0], data_range[1], data_resolution)
    line_y = np.linspace(data_range[0], data_range[1], data_resolution)
    x, y = np.meshgrid(line_x, line_y)
    z = np.array([[shape_func(i, j) for i, j in zip(xrow, yrow)]
                 for xrow, yrow in zip(x, y)])
    return z
