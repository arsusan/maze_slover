# Maze Solver Project Documentation

## Objective

The goal of this project is to solve a maze using various search algorithms. The maze is represented as a 2D list where '1' represents walls and '0' represents open paths.

## Project Structure

maze_solver/ <br>
│<br>
├── search_algorithms/<br>
│ ├── **init**.py<br>
│ ├── dfs.py<br>
│ ├── bfs.py<br>
│ ├── ucs.py<br>
│ ├── a_star.py<br>
│ └── best_first.py<br>
│<br>
├── main.py<br>
└── utils.py<br>

![alt text](image.png)

## Step-by-Step Guide

### 1. Create Project Directory

Create the main project directory and subdirectories for search algorithms.

```bash
mkdir maze_solver
cd maze_solver
mkdir search_algorithms
```

### 2. Initialize `__init__.py` in `search_algorithms`

Create an empty `__init__.py` file to make `search_algorithms` a package.

```bash
touch search_algorithms/__init__.py
```

### 3. Implement Search Algorithms

#### Depth-First Search (`dfs.py`)

**File:** `search_algorithms/dfs.py`

**Function:** `depth_first_search(maze, start, goal)`

**Description:** Implements the DFS algorithm to explore paths in the maze, returning the path from start to goal if found, otherwise returning `None`.

**Steps:**

1. Initialize a stack with the start position.
2. Iterate until the stack is empty.
3. Pop the top position from the stack.
4. Check if the current position is the goal.
5. Push all valid neighboring positions onto the stack.
6. Return the path if found, otherwise `None`.

#### Breadth-First Search (`bfs.py`)

**File:** `search_algorithms/bfs.py`

**Function:** `breadth_first_search(maze, start, goal)`

**Description:** Implements the BFS algorithm to explore paths in the maze, returning the shortest path from start to goal if found, otherwise returning `None`.

**Steps:**

1. Initialize a queue with the start position.
2. Iterate until the queue is empty.
3. Dequeue the front position from the queue.
4. Check if the current position is the goal.
5. Enqueue all valid neighboring positions onto the queue.
6. Return the path if found, otherwise `None`.

#### Uniform Cost Search (`ucs.py`)

**File:** `search_algorithms/ucs.py`

**Function:** `uniform_cost_search(maze, start, goal)`

**Description:** Implements the UCS algorithm to explore paths in the maze, returning the least-cost path from start to goal if found, otherwise returning `None`.

**Steps:**

1. Initialize a priority queue with the start position and cost.
2. Iterate until the queue is empty.
3. Dequeue the position with the lowest cost.
4. Check if the current position is the goal.
5. Enqueue all valid neighboring positions with their costs.
6. Return the path if found, otherwise `None`.

#### A\* Search (`a_star.py`)

**File:** `search_algorithms/a_star.py`

**Function:** `a_star_search(maze, start, goal)`

**Description:** Implements the A\* algorithm using the Manhattan distance as the heuristic to find the shortest path from start to goal.

**Steps:**

1. Initialize a priority queue with the start position and cost.
2. Iterate until the queue is empty.
3. Dequeue the position with the lowest cost plus heuristic.
4. Check if the current position is the goal.
5. Enqueue all valid neighboring positions with their costs plus heuristic.
6. Return the path if found, otherwise `None`.

#### Best-First Search (`best_first.py`)

**File:** `search_algorithms/best_first.py`

**Function:** `best_first_search(maze, start, goal)`

**Description:** Implements the Best-First Search algorithm using the Manhattan distance to expand the node that appears to be closest to the goal.

**Steps:**

1. Initialize a priority queue with the start position.
2. Iterate until the queue is empty.
3. Dequeue the position with the lowest heuristic value.
4. Check if the current position is the goal.
5. Enqueue all valid neighboring positions with their heuristic values.
6. Return the path if found, otherwise `None`.

### 4. Implement Utility Functions (`utils.py`)

**File:** `utils.py`

**Functions:**

- `is_valid_move(maze, position)`: Checks if a move is valid within the maze boundaries and not a wall.
- `visualize_maze(maze, path, start, goal)`: Visualizes the maze and the path found.

### 5. Create the Main Program (`main.py`)

**File:** `main.py`

```python
from search_algorithms.dfs import depth_first_search
from search_algorithms.bfs import breadth_first_search
from search_algorithms.ucs import uniform_cost_search
from search_algorithms.a_star import a_star_search
from search_algorithms.best_first import best_first_search
from utils import visualize_maze

def main():
    # Predefined maze for simplicity
    maze = [
        ['1', '1', '1', '1', '1', '1', '1'],
        ['1', '0', '0', '0', '0', '0', '1'],
        ['1', '0', '1', '1', '1', '0', '1'],
        ['1', '0', '1', '0', '0', '0', '1'],
        ['1', '0', '1', '0', '1', '0', '1'],
        ['1', '0', '0', '0', '1', '0', '1'],
        ['1', '1', '1', '1', '1', '1', '1']
    ]
    start = (1, 1)
    goal = (5, 5)

    algorithms = {
        "1": ("Depth-First Search", depth_first_search),
        "2": ("Breadth-First Search", breadth_first_search),
        "3": ("Uniform Cost Search", uniform_cost_search),
        "4": ("A* Search", a_star_search),
        "5": ("Best-First Search", best_first_search)
    }

    while True:
        print("Select a search algorithm:")
        for key, (name, _) in algorithms.items():
            print(f"{key}: {name}")
        choice = input("Enter the number of the algorithm: ").strip()

        if choice not in algorithms:
            print("Invalid choice. Please select a valid algorithm.")
            continue

        algorithm_name, algorithm_function = algorithms[choice]
        print(f"You selected: {algorithm_name}")

        # Solve the maze
        path = algorithm_function(maze, start, goal)

        if path:
            print("Path found:")
            visualize_maze(maze, path, start, goal)
        else:
            print("No path found.")

        again = input("Do you want to solve another maze? (yes/no): ").strip().lower()
        if again != 'yes':
            break

if __name__ == "__main__":
    main()
```

### Running the Project

To run the console-based maze solver:

```bash
python main.py
```

### Additional Notes

- Ensure all search algorithms are correctly implemented in their respective files.
- `utils.py` should contain necessary helper functions for validation and visualization.
- The main program (`main.py`) interacts with the user, allowing them to choose the search algorithm and visualize the results.

```

This Markdown file provides a comprehensive guide to setting up and implementing the maze solver project with search algorithms and utility functions.
```
