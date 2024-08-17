import matplotlib.pyplot as plt
import networkx as nx
from search_algorithms.dfs import depth_first_search
from search_algorithms.bfs import breadth_first_search
from search_algorithms.ucs import uniform_cost_search
from search_algorithms.a_star import a_star_search
from search_algorithms.best_first import best_first_search

# Function to visualize the maze using NetworkX and Matplotlib
def visualize_maze_graph(maze, path, start, goal):
    rows, cols = len(maze), len(maze[0])
    G = nx.grid_2d_graph(rows, cols)

    # Remove walls from the graph
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == '1':  # Wall
                G.remove_node((r, c))

    pos = {(r, c): (c, -r) for r, c in G.nodes()}  # Set position with (-r) for correct orientation
    fig, ax = plt.subplots()

    # Draw the grid graph
    nx.draw(G, pos, with_labels=False, node_size=300, node_color='white', edge_color='black', ax=ax)

    # Highlight the start, goal, and path
    nx.draw_networkx_nodes(G, pos, nodelist=[start], node_color='green', ax=ax, label='Start')
    nx.draw_networkx_nodes(G, pos, nodelist=[goal], node_color='red', ax=ax, label='Goal')
    nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='blue', ax=ax, label='Path')

    # Adding the legend
    plt.legend(loc='upper right')
    plt.show()

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
            visualize_maze_graph(maze, path, start, goal)
        else:
            print("No path found.")
        
        again = input("Do you want to solve another maze? (yes/no): ").strip().lower()
        if again != 'yes':
            break

if __name__ == "__main__":
    main()
