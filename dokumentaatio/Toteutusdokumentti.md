
```
    └── src                    
        ├── get_grid.py
        ├── index.py
        |
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
        |   
        └── drawing_functions
            ├── draw_path.py
            ├── draw_pointmap.py
            └── draw_plots.py

```
## File docstring

### get_grid.py
- Has methods for generating maps for the algorithms.
1. get_grid provides a map based on perlin noise
    * A function layers two random perlin noises on top of each other creating a map that mimics realt terrain.
    * Takes as inputs dataresolution aka. the amount of datapoints on one side of the square map and random seed so that the conditions are recreatable.
2. get_shape provides a map based on shape func
    * by default gets gives a map that has a geometric hill in the center.

### index.py
- index runs the program
- Combines all the other methods and classes and executes them in the right order etc.

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
  