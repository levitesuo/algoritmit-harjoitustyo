

def height_mapping_function(height_diff, data_resolution):
    '''Given hight difference gives value for the cost of the edge.'''
    return (abs(height_diff) * data_resolution/20) + 1
