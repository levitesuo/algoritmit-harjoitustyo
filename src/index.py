from random import randint, seed

from drawing_functions.draw_plain import draw_plain
from map_generation.get_shape import get_shape
from map_generation.shape_functions import layered_noise
from algorithms.fringe_search import fringe_search
from algorithms.a_star import a_star
from algorithms.functions.heurestic_function import heurestic_function
from services.algorithm_handler import algorithm_handler

# Num of datapoint per side
data_resolution = 100

# Using randon seed so sitsuations are recreatable
# The figures below are with datarange form 0, 1 and only 2 noises layered.
# Good demo seeds 189, 389 ( dataresolution 150 Shows the problem.) 510 dr 100
random_seed = randint(1, 1000)
print(f"RANDOM SEED: {random_seed}")
seed(random_seed)

# z is a  2d array where the values represent the hight
data_map = get_shape(data_resolution=data_resolution,
                     shape_func=lambda x, y: layered_noise(
                         random_seed=random_seed,
                         x=x,
                         y=y,
                         octaves=(1, 5, 10),
                         amplitudes=(1, 0.2, 0.05)),
                     data_range=(-1, 1))
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
    start=start,
    goal=goal,
    algorithm=lambda s, g, m: a_star(
        start=s, goal=g, node_list=m,
        heurestic_function=lambda x, y, z: 0),
    figure=plain
)

algorithm_handler(
    name="Fringe search",
    color="orange",
    data_map=data_map,
    start=start,
    goal=goal,
    algorithm=lambda s, g, m: fringe_search(
        start=s, goal=g, node_list=m,
        heurestic_function=heurestic_function
    ),
    figure=plain,
    is_fringe=True
)

algorithm_handler(
    name="a_ star",
    color="red",
    data_map=data_map,
    start=start,
    goal=goal,
    algorithm=lambda s, g, m: a_star(
        start=s, goal=g, node_list=m,
        heurestic_function=heurestic_function),
    figure=plain
)

plain.update_layout(autosize=True, template='plotly_dark')
plain.show()
