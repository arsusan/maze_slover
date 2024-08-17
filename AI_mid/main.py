import matplotlib.pyplot as plt
import numpy as np
from search_algorithms.dfs import depth_first_search
from search_algorithms.bfs import breadth_first_search
from search_algorithms.ucs import uniform_cost_search
from search_algorithms.a_star import a_star_search
from search_algorithms.best_first import best_first_search

def visualize_maze(maze, path=None, start=None, goal=None):
    
    maze_np = np.array(maze).astype(int)

    # Create a color map
    cmap = plt.cm.colors.ListedColormap(['white', 'black'])

    fig, ax = plt.subplots()
    ax.imshow(maze_np, cmap=cmap, origin='upper')

    # Plot the start and goal positions
    if start:
        ax.scatter(start[1], start[0], color='green', label='Start')
    if goal:
        ax.scatter(goal[1], goal[0], color='red', label='Goal')

    # Plot the path if it exists
    if path:
        for position in path:
            ax.scatter(position[1], position[0], color='blue')

    ax.set_xticks([])
    ax.set_yticks([])
    plt.legend()
    plt.show()

def main():
    
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
    goal = (1, 5)
    
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
            print("Path found.")
            visualize_maze(maze, path, start, goal)
        else:
            print("No path found.")
            visualize_maze(maze, start=start, goal=goal)
        
        again = input("Do you want to solve another maze? (yes/no): ").strip().lower()
        if again != 'yes':
            break

if __name__ == "__main__":
    main()
