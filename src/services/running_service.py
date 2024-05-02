from random import randint, seed

from drawing_functions.draw_plain import draw_plain
from map_generation.node_list_generator import node_list_generator
from map_generation.get_shape import get_shape
from map_generation.shape_functions import layered_noise
from functions.fringe_search import fringe_search
from functions.a_star import a_star
from functions.heurestic import heurestic
from services.algorithm_handler import algorithm_handler


class StartingEngine:
    '''
    Class for setting the neccessary variables for the execution of algorithms.
    '''

    def __init__(self):
        # Num of datapoint per side
        self.data_resolution = None

        # Using randon seed so sitsuations are recreatable
        # The figures below are with datarange form 0, 1 and only 2 noises layered.
        # Good demo seeds 189, 389 ( dataresolution 150 Shows the problem.) 510 dr 100
        self.random_seed = None

        # Start and end cordinates. Set them in relaiton to data_resolution
        self.start = None
        self.goal = None

        # Octaves and amplitudes are variables that control the perlin noise generation
        self.octaves = None
        self.amplitudes = None

        # Variables for omitting the running of some or all algrorithms
        self.run_a_star = True
        self.run_dijkstra = True
        self.run_fringe_search = True

        # Variable for ommitting the drawing of the results.
        self.draw_results = True

    def execute(self):
        '''
        Executes and draws the algorithms.
        '''
        print(f"RANDOM_SEED: {self.random_seed}")
        print(f"start: {self.start}\tgoal: {self.goal} ")
        print(f"Octaves: {self.octaves}\nAmplitudes: {self.amplitudes}")
        print("\nResults:")

        # z is a  2d array where the values represent the hight
        grid = get_shape(data_resolution=self.data_resolution,
                         shape_func=lambda x, y: layered_noise(
                             random_seed=self.random_seed,
                             x=x,
                             y=y,
                             octaves=(1, 5, 10),
                             amplitudes=(1, 0.2, 0.05)),
                         data_range=(-1, 1))
        node_list = node_list_generator(grid=grid, use_two_d=False)
        plain = draw_plain(grid)

        # Running the algorithms, measuring their performance and visualizing them.
        if self.run_dijkstra:
            # Dijkstra implemented as a_star with the heuresticfunction always returning 0
            algorithm_handler(
                name="Dijkstra",
                color="green",
                grid=grid,
                node_list=node_list,
                start=self.start,
                goal=self.goal,
                algorithm=lambda s, g, m: a_star(
                    start=s, goal=g, node_list=m,
                    heurestic_function=lambda x, y, z: 0),
                figure=plain
            )
        if self.run_fringe_search:
            algorithm_handler(
                name="Fringe search",
                color="orange",
                grid=grid,
                node_list=node_list,
                start=self.start,
                goal=self.goal,
                algorithm=lambda s, g, m: fringe_search(
                    start=s, goal=g, node_list=m,
                    heurestic_function=heurestic
                ),
                figure=plain,
                is_fringe=True
            )
        if self.run_a_star:
            algorithm_handler(
                name="a_ star",
                color="red",
                grid=grid,
                node_list=node_list,
                start=self.start,
                goal=self.goal,
                algorithm=lambda s, g, m: a_star(
                    start=s, goal=g, node_list=m,
                    heurestic_function=heurestic),
                figure=plain
            )
        if self.draw_results:
            plain.update_layout(autosize=True, template='plotly_dark')
            plain.show()

    def set_octaves_from_string(self, string):
        '''
        Takes in a string in the format of 10, 22, 44 and sets self.octaves variable to a list [10, 22, 44].
        NOTE: len(self.amplitudes) must be equal to len(self.octaves). If the lengths differ remaning numbers will be generated.
        '''
        data = string.split(",")
        self.octaves = [int(num) for num in data]

    def set_amplitudes_from_string(self, string):
        '''
        Takes in a string in the format of 10, 22, 44 and sets self.amplitudes variable to a list [10, 22, 44]
        NOTE: len(self.amplitudes) must be equal to len(self.octaves). If the lengths differ remaning numbers will be generated.
        '''
        data = string.split(",")
        self.amplitudes = [float(num) for num in data]

    def set_start_from_string(self, string):
        data = string.split(",")
        self.start = (int(num) for num in data)

    def set_goal_from_string(self, string):
        data = string.split(",")
        self.goal = (int(num) for num in data)

    def init_empty_values(self):
        '''
        The vareables are intended to be set by the user. If not we will set the here.
        '''
        if not self.data_resolution:
            self.data_resolution = 75

        if not self.random_seed:
            self.random_seed = randint(1, 1000)
        seed(self.random_seed)

        if not self.start:
            self.start = (randint(1, self.data_resolution//2), 10)

        if not self.goal:
            self.goal = (randint(self.data_resolution//2,
                                 self.data_resolution-1), self.data_resolution-10)

        self._init_amplitudes_octaves()

    def _init_amplitudes_octaves(self):
        '''There must be the same amount of octaves and amplitudes. We make sure thats the case here.'''
        if len(self.octaves) != len(self.amplitudes):
            self.amplitudes = [value for value in self.amplitudes]
            self.octaves = [value for value in self.octaves]

            for i in range(len(self.octaves) - len(self.amplitudes)):
                self.octaves.append(1//self.amplitudes[-(1+i)])

            for i in range(len(self.amplitudes) - len(self.octaves)):
                self.amplitudes.append(1/self.octaves[-(1+i)])

        if not self.octaves:
            self.octaves = (1, 5, 10)

        if not self.amplitudes:
            self.amplitudes = (1, 5, 10)


app_engine = StartingEngine()
