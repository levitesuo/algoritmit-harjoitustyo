# Pathfinding in 3D Terrain

This project explores and compares the performance of A*, Dijkstra, and Fringe Search pathfinding algorithms. The goal is to find the most "energy-efficient" route through a hilly 3D environment, simulating challenges like planning a hiking route by avoiding steep inclines.

The 3D terrain maps are procedurally generated using layered Perlin noise, and the results, including the terrain and the calculated paths, are visualized in 3D using Plotly.

## Features

- **Pathfinding Algorithms**: Implements A*, Dijkstra, and Fringe Search.
- **Procedural 3D Map Generation**: Creates complex, realistic terrains using layered Perlin noise.
- **Interactive GUI**: A Tkinter-based user interface allows for easy configuration of map generation parameters, start/goal coordinates, and algorithm selection.
- **3D Visualization**: Renders the terrain and the paths found by the algorithms in an interactive 3D plot using Plotly.
- **Benchmark Testing**: Supports testing algorithms on standard 2D benchmark maps from `movingai`.
- **Comprehensive Testing**: Includes a suite of unit, integration, and performance tests to ensure correctness and measure performance.

## Getting Started

### Prerequisites

- Python 3.10 or higher
- [Poetry](https://python-poetry.org/docs/#installation) for dependency management.

### Installation & Running

1.  Clone the repository:
    ```bash
    git clone https://github.com/levitesuo/algoritmit-harjoitustyo.git
    ```

2.  Navigate to the project directory:
    ```bash
    cd algoritmit-harjoitustyo
    ```

3.  Install the dependencies using Poetry:
    ```bash
    poetry install
    ```

4.  Run the application using Invoke:
    ```bash
    poetry run invoke start
    ```

## Usage

Running `poetry run invoke start` will launch the application's GUI. From here, you can configure the simulation.

### Configuration Options

-   **Dataresolution**: A positive integer that defines the size of the map grid (e.g., `75` for a 75x75 map).
-   **Random seed**: A positive integer used to seed the random map generation for reproducible results.
-   **Start and Goal**: The `x,y` coordinates for the path's start and end points, provided as two integers separated by a comma (e.g., `10, 10`).
-   **Octaves**: A comma-separated list of floats that control the frequency of the Perlin noise layers.
-   **Amplitudes**: A comma-separated list of floats that control the height of the Perlin noise layers. The length of this list must match the length of the Octaves list.
-   **Algorithm Selection**: Use the checkboxes to enable or disable the execution of Dijkstra, A*, and Fringe Search.
-   **Draw Results**: A checkbox to enable or disable the final 3D visualization.

After configuring the parameters, click the "Start" button to run the simulation. The results, including algorithm execution time and path cost, will be printed to the console. If drawing is enabled, an interactive Plotly window will display the terrain and the computed paths.

## Testing

The project includes a comprehensive test suite. You can run the tests using the following Invoke commands from the project's root directory.

-   **Run unit and integration tests:**
    ```bash
    poetry run invoke test-skip-p
    ```

-   **Run only the performance tests:**
    ```bash
    poetry run invoke performance
    ```

-   **Run all tests with coverage:**
    ```bash
    poetry run invoke coverage
    ```

-   **Generate an HTML coverage report:**
    ```bash
    poetry run invoke coverage-report
    ```
    The report will be created in an `htmlcov/` directory.
