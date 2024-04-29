from services.map_file_translator import map_file_translator
from algorithms.a_star import a_star
from algorithms.fringe_search import fringe_search


def scene_to_list():
    with open("/home/leevisuo/Code/algoritmit-harjiotusty-/src/maps/AR0022SR.map.scen", "r") as f:
        rows = f.read().split("\n")
        data = [row.split() for row in rows]
        data.pop(0)
        data.pop()
        inputs = [((int(c[4]), int(c[5])), (int(c[6]), int(c[7])),
                   float(c[8])) for c in data]
        print(len(inputs))


if __name__ == "__main__":
    scene_to_list()
