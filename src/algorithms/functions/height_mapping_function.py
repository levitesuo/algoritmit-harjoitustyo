def linear_mapping_function(height_diff, data_resolution):
    '''Given hight difference gives value for the cost of the edge.'''
    return (abs(height_diff) * data_resolution) + 1


def exponential_mapping_function(height_diff, data_resolution):
    return (height_diff) ** 2 * data_resolution + 1


def height_mapping_function(height_diff, data_resolution):
    '''Given hight difference gives value for the cost of the edge.'''
    return linear_mapping_function(height_diff, data_resolution)
