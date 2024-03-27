class Adjacency_list:
    def __init__(self, noise_map):
        self.nodes = [[] for _ in range(len(noise_map)**2)]
