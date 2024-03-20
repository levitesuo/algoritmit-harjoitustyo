def height_mapping_function(height_diff):
    '''Given hight difference gives value for the cost of the edge.'''
    a = 100
    if height_diff < -0.1:
        return height_diff * -5 * a + 0.5 + 1
    return height_diff * 20 * a + 3 + 1
