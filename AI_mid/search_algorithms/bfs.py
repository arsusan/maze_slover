from collections import deque

def breadth_first_search(maze, start, goal):
    queue = deque([(start, [start])])  # queue contains tuples of (current_position, path)
    visited = set()

    while queue:
        (current_position, path) = queue.popleft()
        if current_position in visited:
            continue
        visited.add(current_position)

        x, y = current_position
        if current_position == goal:
            return path  # return the path when the goal is reached

        # Get the possible moves (up, down, left, right)
        neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        for neighbor in neighbors:
            if is_valid_move(maze, neighbor) and neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return None  # return None if no path is found

def is_valid_move(maze, position):
    x, y = position
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == '0'
