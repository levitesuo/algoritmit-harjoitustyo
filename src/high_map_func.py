def height_mapping_function(height_diff):
    '''Given hight difference gives value for the cost of the edge.'''
    a = 500
    if height_diff < -0.1:
        return (height_diff * -5 + 0.5) * a + 1
    return (height_diff * 20 + 3) * a + 1
