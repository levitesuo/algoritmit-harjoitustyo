from random import randint, seed

from drawing_functions.draw_plain import draw_plain
from map_generation.get_shape import get_shape
from map_generation.shape_functions import layered_noise
from algorithms.fringe_search import fringe_search
from algorithms.a_star import a_star
from algorithm_handler import algorithm_handler

# Num of datapoint per side
data_resolution = 100

# Using randon seed so sitsuations are recreatable
# Good demo seeds 189
random_seed = 189  # randint(1, 1000)
print(f"RANDOM SEED: {random_seed}")
seed(random_seed)

# z is a  2d array where the values represent the hight
data_map = get_shape(data_resolution=data_resolution,
                     shape_func=lambda x, y: layered_noise(random_seed, x, y),
                     data_range=(0, 1))
plain = draw_plain(data_map)

# Random start and goal
start = (randint(1, data_resolution//2), 10)
goal = (randint(data_resolution//2, data_resolution-1), data_resolution-10)

print(f"start: {start}   goal: {goal}")

# Running the algorithms, measuring their performance and visualizing them.
algorithm_handler(
    name="Dijkstra",
    color="green",
    data_map=data_map,
    algorithm=lambda: a_star(start, goal, data_map,
                             heurestic_function=lambda x, y, z: 0),
    figure=plain
)

algorithm_handler(
    name="Fringe search",
    color="orange",
    data_map=data_map,
    algorithm=lambda: fringe_search(start, goal, data_map),
    figure=plain,
    is_fringe=True
)

algorithm_handler(
    name="A star",
    color="red",
    data_map=data_map,
    algorithm=lambda: a_star(start, goal, data_map),
    figure=plain
)

""" algorithm_handler(
    name="A star non linear",
    color="blue",
    data_map=data_map,
    algorithm=lambda: a_star(
        start, goal, data_map, height_mapping_function=exponential_mapping_function),
    figure=plain
) """

plain.update_layout(autosize=True, template='plotly_dark')
plain.show()
