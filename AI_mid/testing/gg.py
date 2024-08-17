import heapq
import numpy as np
import matplotlib.pyplot as plt

def visualize_maze(maze, path=None):
    """Visualizes the maze and the solution path (if provided)."""

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Set the background color to white
    ax.set_facecolor('white')

    # Create a colormap for the maze
    cmap = plt.cm.gray_r
    cmap.set_bad(color='black')  # Color walls as black

    # Display the maze
    img = ax.imshow(maze, cmap=cmap)

    # If a path is provided, plot it
    if path:
        x, y = zip(*path)
        ax.plot(x, y, color='red', marker='o')

    # Remove axis ticks and labels
    ax.set_xticks([])
    ax.set_yticks([])

    plt.show()

def heuristic(node, goal):
    """Calculates the Manhattan distance heuristic."""
    x1, y1 = node
    x2, y2 = goal
    return abs(x1 - x2) + abs(y1 - y2)

def a_star_search(maze, start, goal):
    """Performs A* search to find the shortest path."""

    rows, cols = len(maze), len(maze[0])
    open_set = []
    heapq.heappush(open_set, (0, start))  # (f_score, node)
    came_from = {}
    g_score = {node: float('inf') for row in range(rows) for col in range(cols) for node in [(row, col)]}
    g_score[start] = 0
    f_score = {node: float('inf') for row in range(rows) for col in range(cols) for node in [(row, col)]}
    f_score[start] = heuristic(start, goal)

    while open_set:
        current = heapq.heappop(open_set)[1]

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        for neighbor in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            x, y = current
            new_x, new_y = x + neighbor[0], y + neighbor[1]
            if 0 <= new_x < rows and 0 <= new_y < cols and maze[new_x][new_y] != 1:
                tentative_g_score = g_score[current] + 1

                if tentative_g_score < g_score[(new_x, new_y)]:
                    came_from[(new_x, new_y)] = current
                    g_score[(new_x, new_y)] = tentative_g_score
                    f_score[(new_x, new_y)] = tentative_g_score + heuristic((new_x, new_y), goal)
                    heapq.heappush(open_set, (f_score[(new_x, new_y)], (new_x, new_y)))

    return None

def main():
    # Sample maze
    maze = [
        [0, 0, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0],
        [1, 1, 1, 0]
    ]

    start = (0, 0)
    goal = (3, 3)

    path = a_star_search(maze, start, goal)

    if path:
        visualize_maze(maze, path)
    else:
        print("No path found")

if __name__ == "__main__":
    main()
