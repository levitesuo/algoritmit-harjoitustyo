# Toetutusdokumentti

Projektissa on toteutettu 3 eri reitinetsintä algoritmia. Pääpainona on onnlut Fringe search algoritmi jota vertaillaa a* algoritmiin. Dijkstra on tullut ns. vahingossa mukaan ja implementoitu antamalla a_star algoritmin heureettiseksi funktioksi 0.

## Ohjelman rakenne

```text
    └── src                    
        ├── index.py
        ├── show_map.py
        ├── algorithms
        |   ├── fringe_search.py
        |   ├── a_star.py
        |   |
        |   ├── functions
        |   |   ├── height_mapping_function.py
        |   |   └── heurestic_function.py
        |   |
        |   └── objects
        |       ├── node.py
        |       └── doubly_linked_list.py
        ├──services
        |   ├── algorithm_handler.py
        |   ├── generated_map_translator.py
        |   └── map_file_translator.py
        |
        ├── map_generation
        |   ├── get_shape.py
        |   ├── shape_functions.py
        |   └── maps
        |       └── ...
        |   
        └── drawing_functions
            ├── draw_path.py
            ├── draw_pointmap.py
            └── draw_plots.py
            

```

## File docstring

### index.py

- index runs the program
- Combines all the other methods and classes and executes them in the right order etc.

### show_map.py

- just a basic method for showing maps used in testing.

### algorithms

- Has all the methods and classes needed for the algorithms
- a_star.py
  - Method for executing the a* algo (And dijkstra if heuresticfunction is f(x, y) = 0)
- fringe_search.py
  - Method for executing fringe search algo

- #### functions

  - Holds the neccessary functions for executoin of the algorithms
  - height_mapping_function
    - determines the cost of moving from one cell to another based on their position and height difference
  - heurestic_function
    - Gives a heurestic estimate for the cost of the path
    (needed for a* and fringe_search)

- #### Objects

  - Holds the neccessary objects for executoin of the algorithms
  - doubly_linked_list
    - a doubly linked list object thet can be added to and deleted from in O(0) timecomplexity.
    - Necessary for fringe_search
- node
  - A simple node object.
  - The algorithms datamaps are comprised of these

### Services

  - algorithm handler holds a single method. It's a middleman in running the functions from index. 
    - calls drawing functions and prints everything to console.
  - generated_map_translator is the final piece in calling functions. Makes node_lists form datamaps and translates path cordinates back to readable ones.
  - map_file_translator does basicly the same as generated_map_translator, but for movingai maps. Holds also a TestNode object witch is a cloneof the node object made for those maps. Basicly a helper for basic tests.

### Map generation

- get_shape has a function that given a function f(x, y) = z generates a map of given dataresolutioin and data range.
- shape_functions holds multiple functions intended for use with get_shape. Most of them are there for ns. storage. The one that is usesd is layered_noise.
- maps is a directory holding multiple movingai maps and their solutions. Only one is used, but the rest are there for possible further implementation.

### Drawing functions

  - holds 3 functions responsible for the visuals
