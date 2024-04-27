from services.map_file_translator import map_file_translator
from algorithms.a_star import a_star
with open("/home/leevisuo/Code/algoritmit-harjiotusty-/src/tests/maps/AR0020SR.map", "r") as f:
    print(map_file_translator((24, 65), (43, 48), f.read(), a_star)['cost'])
# 65	24	48	43	26.04163055
