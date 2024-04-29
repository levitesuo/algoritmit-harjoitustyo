from services.algorithm_handler import algorithm_handler
from map_generation.get_shape import get_shape
from map_generation.shape_functions import layered_noise
from drawing_functions.draw_plain import draw_plain
from algorithms.a_star import a_star
from algorithms.functions.heurestic_function import heurestic_function


def show_map(i):
    m = get_shape(data_resolution=50,
                  shape_func=lambda x, y: layered_noise(
                      random_seed=i,
                      x=x, y=y,
                      octaves=(1, 5, 10),
                      amplitudes=(1, 0.2, 0.05)
                  ))
    plain = draw_plain(m)
    algorithm_handler(
        name="Dijkstra",
        color="green",
        data_map=m,
        start=(1, 1),
        goal=(49, 49),
        algorithm=lambda s, g, m: a_star(
            start=s, goal=g, node_list=m,
            heurestic_function=heurestic_function),
        figure=plain
    )

    plain.update_layout(autosize=True, template='plotly_dark')
    plain.show()


if __name__ == "__main__":
    show_map(int(input("What number of testmaps do you want to see? (1->)"))-1)
